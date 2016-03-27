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

admin.site.register(Biografia,BiografiaAdmin)
admin.site.register(Artista)


class SongAlbumInline(admin.StackedInline):
	model = SongAlbum
	extra = 3
	exclude = ('link',)

class AlbumAdmin(admin.ModelAdmin):
	inlines = [
		SongAlbumInline,
	]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Discoteca)