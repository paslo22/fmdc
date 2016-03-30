from django.contrib import admin

from .models import *

class ImageInline(admin.StackedInline):
	model = Image
	extra = 1

class SongInline(admin.StackedInline):
	model = Song
	extra = 1
	exclude = ('link',)

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

class AlbumInline(admin.StackedInline):
	model = Album
	extra = 3

class DiscotecaAdmin(admin.ModelAdmin):
	inlines = [
		AlbumInline,
	]
	search_fields=('name__name',)
	raw_id_fields=('name',)

admin.site.register(Discoteca,DiscotecaAdmin)