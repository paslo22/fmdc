from django.contrib import admin

from .models import *

class ImageInline(admin.StackedInline):
	model = Image
	extra = 1

class EfemerideInline(admin.StackedInline):
	model = Efemeride
	extra = 1

class SongInline(admin.StackedInline):
	model = Song
	extra = 1
	exclude = ('link',)

class BiografiaAdmin(admin.ModelAdmin):
	inlines = [
		SongInline,
		ImageInline,
		EfemerideInline,
	]
	exclude = ('text',)
	search_fields=('name__name',)

admin.site.register(Biografia,BiografiaAdmin)
admin.site.register(Artista)

# class SongAlbumInline(admin.StackedInline):
# 	model = SongAlbum
# 	extra = 3
# 	exclude = ('link',)

# class AlbumAdmin(admin.ModelAdmin):
# 	inlines = [
# 		SongAlbumInline,
# 	]

# admin.site.register(Album, AlbumAdmin)

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