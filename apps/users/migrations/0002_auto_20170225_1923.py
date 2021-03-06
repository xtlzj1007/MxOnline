# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-25 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gendere',
            field=models.CharField(choices=[('male', '\u7537'), ('female', '\u5973')], max_length=6, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u624b\u673a\u53f7'),
        ),
    ]
