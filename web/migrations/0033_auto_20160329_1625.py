# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_auto_20160329_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='EfemerideMes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(verbose_name='Mes')),
                ('texto', models.TextField(verbose_name='Efemerides')),
            ],
        ),
        migrations.RemoveField(
            model_name='efemeride',
            name='bio',
        ),
        migrations.AddField(
            model_name='efemeride',
            name='mes',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web.EfemerideMes'),
            preserve_default=False,
        ),
    ]