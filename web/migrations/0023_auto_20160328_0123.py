# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_auto_20160328_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discoteca',
            name='albumes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Album'),
        ),
    ]
