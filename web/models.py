# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
import re
from django.db import models
from django.conf import settings
import datetime
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
	text_org = models.TextField('Texto')

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
	link = models.CharField('Enlace',max_length=300)
	link_org = models.CharField('Enlace',max_length=300)

	def __str__(self):
		return self.name

	def formatHelper(self,matchobj):
		url = static(settings.MEDIA_URL+'archive/Biografias/'+matchobj.group('path'))
		return r'<audio controls><source src="'+url+'" type="audio/mpeg">Su explorador es antiguo\. Actualicelo para reproducir audios\.</audio>'

	def save(self, *args, **kwargs):
		self.link = re.sub(r'^\[audio:(?P<path>[a-zA-Z0-9/\.]+)\]$',self.formatHelper,self.link_org,flags=re.UNICODE)
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

class EfemerideMes(models.Model):
	month = models.CharField('Mes',max_length=10)
	monthNumber = models.IntegerField()
	texto = models.TextField('Efemerides')
	texto_org = models.TextField('Efemerides')

	def __str__(self):
		return self.month

	def monthFromString(self,x):
		return {
			'Enero': 1,
			'Febrero': 2,
			'Marzo': 3,
			'Abril': 4,
			'Mayo': 5,
			'Junio': 6,
			'Julio': 7,
			'Agosto': 8,
			'Septiembre': 9,
			'Octubre': 10,
			'Noviembre': 11,
			'Diciembre': 12
		}.get(x)

	class Meta:
		verbose_name='Efemeride por mes'
		verbose_name_plural='Efemerides por mes'

	def save(self,*args,**kwargs):
		self.monthNumber = self.monthFromString(self.month)
		self.texto = self.texto_org.replace('\n','').replace('\r','')
		super(EfemerideMes,self).save(*args,**kwargs)
		if (self.efemeride_set.all()!=[]):
			self.efemeride_set.all().delete()
		pattern = re.compile(ur"""dia:([0-9]+)\[([\w |\-\u2013()\u201c\u201d,]+)\]""",flags=re.UNICODE)
		pattern2 = re.compile(ur"""([0-9]+) +\| +([\W\D \-\u2013()\u201c\u201d,]+)""",flags=re.UNICODE)
		for (dia, efemeride) in re.findall(pattern,self.texto):
			for (anio, efe) in re.findall(pattern2,efemeride):
				efem = Efemeride()
				efem.date = datetime.date(int(anio),self.monthNumber,int(dia))
				efem.event = efe
				efem.mes = self
				efem.save()

class Efemeride(models.Model):
	mes = models.ForeignKey(EfemerideMes)
	date = models.DateField('Fecha')
	event = models.CharField('Efemeride',max_length=300)

	def __str__(self):
		return self.date.strftime('Efemeride del %d, %b')

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
	songString = models.TextField('Listado de canciones',blank=True)

	def save(self,*args,**kwargs):
		super(Album,self).save(*args,**kwargs)
		if (self.songalbum_set.all()!=[]):
			self.songalbum_set.all().delete()
		pattern = re.compile(ur'(?:\[tituloPrincipal:([\w/\. ]+)\])?\[nombre:([\w\d/\.\-() ]+)\](?:\[infoExtra:([\w/\.\-() ]+)\])?\[audio:([\w/\.]+)\]',flags=re.UNICODE)
		strSinBreaklines = self.songString.replace('\n','').replace('\r','')
		for (titulo,nombre,infoExtra,path) in re.findall(pattern,strSinBreaklines):
			song = SongAlbum()
			song.album = self
			song.tituloPrincipal = titulo
			song.name = nombre
			song.infoExtra = infoExtra
			url = static(settings.MEDIA_URL+'archive/Discografias/'+path)
			song.link = r'<audio controls preload="none"><source src="'+url+'" type="audio/mpeg">Su explorador es antiguo\. Actualicelo para reproducir audios\.</audio>'
			song.save()

	class Meta:
		verbose_name='Album'
		verbose_name_plural='Albumes'

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class SongAlbum(models.Model):
	album = models.ForeignKey(Album, default=None)
	tituloPrincipal = models.CharField('Titulo principal', max_length=100, null=True, blank=True)
	name = models.CharField('Nombre',max_length=300)
	infoExtra = models.TextField('Informacion extra',null=True,blank=True)
	link = models.CharField('Enlace',max_length=300)

	def __str__(self):
		return self.name

	def formatHelper(self,matchobj):
		url = static(settings.MEDIA_URL+matchobj.group('path'))
		return r'<audio controls><source src="'+url+'" type="audio/mpeg">Su explorador es antiguo\. Actualicelo para reproducir audios\.</audio>'

	class Meta:	
		verbose_name='Cancion'
		verbose_name_plural='Canciones'
