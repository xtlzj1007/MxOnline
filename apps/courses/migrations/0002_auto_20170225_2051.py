# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-25 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseRespirce',
            new_name='CourseResource',
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '\u521d\u7ea7'), ('zj', '\u4e2d\u7ea7'), ('gj', '\u9ad8\u7ea7')], max_length=100, verbose_name='\u96be\u5ea6'),
        ),
    ]
