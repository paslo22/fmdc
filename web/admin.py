from django.contrib import admin
import nested_admin

from web.models import Actividad, ActividadImage, Image, ImageAlbum, Song, Biografia, \
    Artista, EfemerideMes, Discoteca, Album, Video, AlbumSong

from .forms import AdminSongForm


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
        for album in obj.albumes.all():
            print(album.name)
            print(request.FILES)
            for _, song in request.FILES.items():
                print(song)
                album_song = AlbumSong(
                    album=album,
                    link=song
                )
                album_song.save()
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
