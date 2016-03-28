# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
import re
from django.db import models
from django.conf import settings
from copy import copy
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.encoding import python_2_unicode_compatible

class Artista(models.Model):
	name = models.CharField('Nombre',max_length=70)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Artista'
		verbose_name_plural='Artistas'


class Biografia(models.Model):
	name = models.OneToOneField(Artista)
	text = models.TextField('Texto')
	text_org = models.TextField('Texto original')

	def __str__(self):
		return self.name.name

	def htmlText(self,txt):
		texto = '<p class="text-justify">'
		texto+= txt.replace('\n', '</p><p class="text-justify">')
		texto+= '\r</p>'
		texto = texto.replace('<p class="text-justify">\r</p>','')
		return texto

	def save(self, *args, **kwargs):
		self.text = self.htmlText(self.text_org)
		super(Biografia, self).save(*args, **kwargs)

	class Meta:
		verbose_name='Biografia'
		verbose_name_plural='Biografias'

@python_2_unicode_compatible
class Song(models.Model):
	songs = models.ForeignKey(Biografia, default=None)
	name = models.CharField('Nombre',max_length=70)
	extraInfo = models.TextField('Informacion extra',blank=True)
	link = models.CharField('Enlace',max_length=100)
	link_org = models.CharField('Enlace',max_length=100)

	def __str__(self):
		return self.name

	def formatHelper(self,matchobj):
		url = static(settings.MEDIA_URL+'archive/Biografias/'+matchobj.group('path'))
		return r'<audio controls><source src="'+url+'" type="audio/mpeg">Su explorador es antiguo\. Actualicelo para reproducir audios\.</audio>'

	def save(self, *args, **kwargs):
		self.link = re.sub(r'^\[audio:(?P<path>[a-zA-Z0-9/\.]+)\]$',self.formatHelper,self.link_org)
		super(Song,self).save(*args, **kwargs)

	class Meta:	
		verbose_name='Cancion'
		verbose_name_plural='Canciones'

class Image(models.Model):
	bio = models.ForeignKey(Biografia, default=None)
	image = models.ImageField('Imagen',upload_to='images/', default='')
	description = models.CharField('Descripcion',max_length=70,blank=True)

	class Meta:
		verbose_name='Imagen'
		verbose_name_plural='Imagenes'

class Efemeride(models.Model):
	bio = models.ForeignKey(Biografia, default=None)
	date = models.DateField('Fecha')
	event = models.CharField('Efemeride',max_length=100)

	class Meta:
		verbose_name='Efemeride'
		verbose_name_plural='Efemerides'

class Discoteca(models.Model):
	name = models.OneToOneField(Artista)

	def __str__(self):
		return "Discoteca de " + unicode(self.name)

@python_2_unicode_compatible
class Album(models.Model):
	discoteca = models.ForeignKey(Discoteca)
	name = models.CharField('Nombre', max_length=100)
	tapa = models.ImageField('Tapa', upload_to='images/', default='', blank=True)
	lamina = models.ImageField('Lamina', upload_to='images/', default='', blank=True)
	year = models.IntegerField('Año', null=True,blank=True)
	songString = models.TextField(blank=True)
	songString_org = models.TextField('Listado de canciones',blank=True)

	def save(self,*args,**kwargs):

		super(Album,self).save(*args,**kwargs)

	class Meta:
		verbose_name='Album'
		verbose_name_plural='Albumes'

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class SongAlbum(models.Model):
	album = models.ForeignKey(Album, default=None)
	name = models.CharField('Nombre',max_length=70)
	extraInfo = models.TextField('Informacion extra',blank=True)
	link = models.CharField('Enlace',max_length=100)
	link_org = models.CharField('Enlace',max_length=100)

	def __str__(self):
		return self.name

	def formatHelper(self,matchobj):
		url = static(settings.MEDIA_URL+matchobj.group('path'))
		return r'<audio controls><source src="'+url+'" type="audio/mpeg">Su explorador es antiguo\. Actualicelo para reproducir audios\.</audio>'

	def save(self, *args, **kwargs):
		self.link = re.sub(r'^\[audio:(?P<path>[a-zA-Z0-9/\.]+)\]$',self.formatHelper,self.link_org)
		super(Song,self).save(*args, **kwargs)

	class Meta:	
		verbose_name='Cancion'
		verbose_name_plural='Canciones'
