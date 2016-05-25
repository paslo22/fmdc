from django.contrib import admin
import nested_admin

from .models import *

class ImageInline(admin.StackedInline):
	model = Image
	extra = 1
	classes = ('grp-collapse grp-open',)
	inline_classes = ('grp-collapse grp-open',)

class SongInline(admin.StackedInline):
	model = Song
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
	search_fields=('name__name',)
	raw_id_fields=('name',)

admin.site.register(Biografia,BiografiaAdmin)

class EfemerideMesAdmin(admin.ModelAdmin):
	exclude = ('monthNumber','texto')

admin.site.register(EfemerideMes,EfemerideMesAdmin)

class ArtistaAdmin(admin.ModelAdmin):
	search_fields=('name',)

admin.site.register(Artista,ArtistaAdmin)

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
	extra = 3
	exclude = ('songString',)
	classes = ('grp-collapse grp-open',)
	inline_classes = ('grp-collapse grp-open',)

class VideoInline(nested_admin.NestedStackedInline):
	model = Video
	classes = ('grp-collapse grp-open',)
	inline_classes = ('grp-collapse grp-open',)	

class ActividadImageInline(nested_admin.NestedStackedInline):
	model = ActividadImage
	classes = ('grp-collapse grp-open',)
	inline_classes = ('grp-collapse grp-open',)

class DiscotecaAdmin(nested_admin.NestedModelAdmin):
	inlines = [
		AlbumInline,
	]
	search_fields=('name__name',)
	raw_id_fields=('name',)


admin.site.register(Discoteca,DiscotecaAdmin)

class ActividadAdmin(admin.ModelAdmin):
	inlines = [
		VideoInline,
		ActividadImageInline,
	]
	exclude = ('text',)
	search_fields=('title__title',)
	

admin.site.register(Actividad, ActividadAdmin)
