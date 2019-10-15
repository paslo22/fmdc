import os

from django.contrib import admin
from django.conf import settings
import nested_admin

from web.models import Actividad, ActividadImage, Image, ImageAlbum, Song, Biografia, \
    Artista, EfemerideMes, Discoteca, Album, Video, AlbumSong

from .forms import AdminSongForm
from .helpers import get_or_create_folder_path, copy_tmp_file_into_destination


def album_song_path(album):
    discoteca_name = album.discoteca.name.name
    path = f'archive/Discografias/{discoteca_name}/{album.name}'
    return path

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1   
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)


class SongInline(admin.StackedInline):
    model = Song
    form = AdminSongForm
    extra = 1
    exclude = ('link', 'song_string',)
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)


class AlbumSongInline(admin.StackedInline):
    model = AlbumSong
    form = AdminSongForm
    extra = 1
    exclude = ('link',)
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class BiografiaAdmin(admin.ModelAdmin):
    inlines = [
        SongInline,
        ImageInline,
    ]
    exclude = ('text',)
    search_fields = ('name__name',)
    raw_id_fields = ('name',)


admin.site.register(Biografia, BiografiaAdmin)


class EfemerideMesAdmin(admin.ModelAdmin):
    exclude = ('monthNumber', 'texto')


admin.site.register(EfemerideMes, EfemerideMesAdmin)


class ArtistaAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Artista, ArtistaAdmin)


class ImageAInline(nested_admin.NestedStackedInline):
    model = ImageAlbum
    extra = 1
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)


class AlbumInline(nested_admin.NestedStackedInline):
    inlines = [
        ImageAInline,
    ]
    model = Album
    form = AdminSongForm
    extra = 3
    exclude = ('songString',)
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class VideoInline(nested_admin.NestedStackedInline):
    model = Video
    extra = 1
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)


class ActividadImageInline(nested_admin.NestedStackedInline):
    model = ActividadImage
    extra = 1
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)


class DiscotecaAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        AlbumInline,
    ]
    search_fields = ('name__name',)
    raw_id_fields = ('name',)

    def save_model(self, request, obj, form, change):
        for index, album in enumerate(obj.albumes.all()):
            album_position = f'albumes-{index}-song'
            album_songs = request.FILES.getlist(album_position)
            #if album_songs:
                #AlbumSong.objects.filter(album=album).delete()
            
            for album_song in album_songs:
                name = album_song.name.split(".")[0]
                link = album_song_path(album=album)
                relative_path_file = f'{link}/{album_song.name}'
                if AlbumSong.objects.filter(link=relative_path_file):
                    continue

                full_path_folder = settings.MEDIA_ROOT + link
                get_or_create_folder_path(path=full_path_folder)
                full_path_file = f'{full_path_folder}/{album_song.name}'
                copy_tmp_file_into_destination(
                    tmp_file=album_song,
                    destination_file=full_path_file
                )

                AlbumSong.objects.create(
                    name=name,
                    album=album,
                    link=relative_path_file
                )
        super().save_model(request, obj, form, change)

admin.site.register(Discoteca, DiscotecaAdmin)


class ActividadAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        VideoInline,
        ActividadImageInline,
    ]
    exclude = ('text',)
    search_fields = ('title__title',)


admin.site.register(Actividad, ActividadAdmin)
