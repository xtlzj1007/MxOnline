# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-26 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(1, '\u8bfe\u7a0b'), (2, '\u8bfe\u7a0b\u673a\u6784'), (3, '\u8001\u5e08')]),
        ),
    ]
