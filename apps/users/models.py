# -*- encoding:utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 用户信息表
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称")
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gendere = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), verbose_name=u"性别")
    address = models.CharField(max_length=100, default=u'', verbose_name=u"地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机号")
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100, verbose_name=u"头像")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


# 邮箱验证信息表
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.CharField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', u"注册"), ('forget', u"找回")), verbose_name=u"验证类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'验证时间')  # now 后必要有括号，实例化时才生成时间

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


# 轮播图库
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name="轮播图")
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

