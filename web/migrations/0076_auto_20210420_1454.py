# Generated by Django 2.1.15 on 2021-04-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0075_revista_revistaimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revistaimage',
            name='link',
            field=models.ImageField(default='', upload_to='images/', verbose_name='Revista Imagen'),
        ),
    ]
