# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render
from testproject.forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import urllib

def encoded_dict(in_dict):
    out_dict = {}
    for k, v in in_dict.iteritems():
        if isinstance(v, unicode):
            v = v.encode('utf8')
        elif isinstance(v, str):
            # Must be encoded in UTF-8
            v.decode('utf8')
        out_dict[k] = v
    return out_dict

def home(request):
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            social =  form.cleaned_data.get('social', None)
            data = {}
            if social == 'vk':
                # url = 'https://api.vk.com/method/execute.SendMessage'
                url = 'http://ataka.by/getnets/vk.php'
                # data['access_token'] = '33d76ddd513230a04b7cbe1eaa1ec1ec2e4621278f2c1cf3804cdb391e84164ce119f9cce0611e56fbaa2'
            elif social == 'fb':
                url = 'http://ataka.by/getnets/fb.php'
            elif social == 'tw':
                url = 'http://ataka.by/getnets/tw.php'
            elif social == 'tg':
                url = 'http://ataka.by/getnets/tg.php'
            elif social == 'em':
                url = 'http://ataka.by/getnets/em.php'

            data['user'] = form.cleaned_data.get('user', None)
            data['message'] = form.cleaned_data.get('message', None)
            utf_data = encoded_dict(data)
            enc_data = urllib.urlencode(utf_data)
            response = urllib.urlopen(url, enc_data)
            result = response.read()
            if result == '0':
                return HttpResponse("Сообщение отправлено")
            else:
                return HttpResponse("Ошибка отправки сообщения")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SendMessageForm()

    return render(request, 'home.html', {'form': form})


