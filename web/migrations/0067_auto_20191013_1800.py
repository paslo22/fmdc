# Generated by Django 2.2.3 on 2019-10-13 21:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0066_auto_20191013_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='link',
            field=models.FileField(default='', upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['.mp4'])], verbose_name='Video'),
        ),
    ]
