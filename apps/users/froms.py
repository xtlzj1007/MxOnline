# -*- encoding:utf-8 -*-
__author__ = 'zuojie'
__date__ = '17-3-2 下午9:13'

from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)  # required必填字段
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()
