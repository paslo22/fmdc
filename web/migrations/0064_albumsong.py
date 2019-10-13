# Generated by Django 2.2.3 on 2019-10-13 20:19

from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0063_auto_20190803_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.FileField(upload_to=web.models.album_song_path)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='canciones', to='web.Album')),
            ],
        ),
    ]
