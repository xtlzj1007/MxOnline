# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-25 20:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170225_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u9a8c\u8bc1\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '\u6ce8\u518c'), ('forget', '\u627e\u56de')], max_length=10, verbose_name='\u9a8c\u8bc1\u7c7b\u578b'),
        ),
    ]
