# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_auto_20160325_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.IntegerField(default=0, verbose_name='Anio'),
            preserve_default=False,
        ),
    ]
