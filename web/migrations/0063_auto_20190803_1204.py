# Generated by Django 2.1 on 2019-08-03 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0062_auto_20190802_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadimage',
            name='act',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Actividad'),
        ),
        migrations.AlterField(
            model_name='album',
            name='discoteca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Discoteca'),
        ),
        migrations.AlterField(
            model_name='biografia',
            name='name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Artista'),
        ),
        migrations.AlterField(
            model_name='discoteca',
            name='name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Artista'),
        ),
        migrations.AlterField(
            model_name='image',
            name='bio',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Biografia'),
        ),
        migrations.AlterField(
            model_name='song',
            name='songs',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Biografia'),
        ),
        migrations.AlterField(
            model_name='video',
            name='videos',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Actividad'),
        ),
    ]