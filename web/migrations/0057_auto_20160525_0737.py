# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-25 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0056_auto_20160525_0733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividadimage',
            options={'verbose_name': 'Imagen', 'verbose_name_plural': 'Imagenes'},
        ),
    ]