from django.contrib import admin

from .models import Biografia, Image, Efemeride

class ImageInline(admin.StackedInline):
	model = Image

class EfemerideInline(admin.StackedInline):
	model = Efemeride

class BiografiaAdmin(admin.ModelAdmin):
	inlines = [
		ImageInline,
		EfemerideInline,
	]
	exclude = ('text',)

admin.site.register(Biografia,BiografiaAdmin)