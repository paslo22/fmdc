# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 05:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0034_auto_20160329_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='efemeridemes',
            options={'verbose_name': 'Efemeride por mes', 'verbose_name_plural': 'Efemerides por mes'},
        ),
    ]
