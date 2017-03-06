# -*- encoding:utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend

from .models import UserProfile
from django.db.models import Q
from django.views.generic.base import View
from .froms import LoginForm, RegisterForm


# 重写用户认证
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))  # 使用并集查询
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 用户登陆
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            users = authenticate(username=user_name, password=pass_word)
            if users is not None:
                login(request, users)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {"msg": u"用户名或密码错误！"})
        else:
            return render(request, 'login.html', {"login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register_from = RegisterForm()
        return render(request, 'register.html', {'register_from': register_from})

# class LogoutView(View):
# logout(request)
