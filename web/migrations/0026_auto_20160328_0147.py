# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_auto_20160328_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.IntegerField(null=True, verbose_name='A\xf1o'),
        ),
    ]
