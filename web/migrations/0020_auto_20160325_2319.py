# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20160325_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discoteca',
            name='albumes',
        ),
        migrations.AddField(
            model_name='discoteca',
            name='albumes',
            field=models.ManyToManyField(default=None, to='web.Album'),
        ),
    ]
