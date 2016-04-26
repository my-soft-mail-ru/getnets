# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

class SendMessageForm(forms.Form):
    OPTIONS = (
        ("vk", "ВКонтакте"),
        ("tw", "Twitter"),
        ("tg", "Telegram"),
        ("em", "E-mail"),
    )
    social = forms.ChoiceField(label='Выберите сеть', choices=OPTIONS)
    user = forms.CharField(label='Пользователь', max_length=130) # initial='310167402'
    # message = forms.CharField(label='Сообщение', max_length=500)
    message = forms.CharField(label='Сообщение',widget=forms.Textarea)
