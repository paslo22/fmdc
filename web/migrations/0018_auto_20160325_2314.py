# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20160325_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songalbum',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.SongAlbum'),
        ),
    ]
