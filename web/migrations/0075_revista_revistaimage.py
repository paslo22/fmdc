# Generated by Django 2.1.15 on 2021-04-20 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0074_auto_20201016_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('tapa', models.ImageField(default='', upload_to='images/', verbose_name='Tapa revista')),
            ],
            options={
                'verbose_name': 'Revista',
                'verbose_name_plural': 'Revistas',
            },
        ),
        migrations.CreateModel(
            name='RevistaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ImageField(default='', upload_to='images/', verbose_name='Imagen')),
                ('revista', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_revista', to='web.Revista')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
            },
        ),
    ]
