# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20160325_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biografia',
            name='songs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Song'),
        ),
    ]
