# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-13 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0060_auto_20160526_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='description',
            field=models.TextField(max_length=20000, verbose_name='Descripci\xf3n'),
        ),
    ]