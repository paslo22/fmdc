# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
import re
from django.db import models
from django.conf import settings
from datetime import datetime,date
from copy import copy
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.encoding import python_2_unicode_compatible
from .validators import validate_file_extension

@python_2_unicode_compatible
class Artista(models.Model):
	name = models.CharField('Nombre',max_length=70)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name='Artista'
		verbose_name_plural='Artistas'

@python_2_unicode_compatible
class Biografia(models.Model):
	name = models.OneToOneField(Artista)
	text = models.TextField('Texto')
	text_org = models.TextField('Texto')

	def __str__(self):
		return self.name.name

	def htmlText(self,txt):
		texto = u'<p class="text-justify">'
		texto+= txt.replace(u'\n', u'</p><p class="text-justify">')
		texto+= u'\r</p>'
		texto = texto.replace(u'<p class="text-justify">\r</p>',u'')
		return texto

	def save(self, *args, **kwargs):
		self.text = self.htmlText(self.text_org)
		super(Biografia, self).save(*args, **kwargs)

	class Meta:
		ordering = ['name']
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

	def save(self, *args, **kwargs):
		pattern = re.compile(ur'^\[audio:([\w\/\.]+)\]$', re.UNICODE)
		url = static(settings.MEDIA_URL+'archive/Biografias/'+re.match(pattern,self.link_org).group(1))
		self.link = ur'<audio controls><source src="'+url+'" type="audio/mpeg">Su explorador es antiguo\. Actualicelo para reproducir audios\.</audio>'
		super(Song,self).save(*args, **kwargs)

	class Meta:	
		verbose_name='Cancion'
		verbose_name_plural='Canciones'
@python_2_unicode_compatible
class Image(models.Model):
	bio = models.ForeignKey(Biografia, default=None)
	image = models.ImageField('Imagen',upload_to='images/', default='')
	description = models.CharField('Descripcion',max_length=200,blank=True)

	def __str__(self):
		return self.description

	class Meta:
		verbose_name='Imagen'
		verbose_name_plural='Imagenes'

@python_2_unicode_compatible
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
		self.texto = self.texto_org.replace('\n','').replace('\r','').replace('"','&quot;')
		super(EfemerideMes,self).save(*args,**kwargs)
		if (self.efemeride_set.all()!=[]):
			self.efemeride_set.all().delete()
		pattern = re.compile(ur"""dia:([0-9]+) *\[(.+?)\]""",flags=re.UNICODE)
		pattern2 = re.compile(ur"""([0-9]+) *\| *([\W\D .]+)""",flags=re.UNICODE)
		for (dia, efemeride) in re.findall(pattern,self.texto):
			for (anio, efe) in re.findall(pattern2,efemeride):
				efem = Efemeride()
				efem.date = datetime.date(int(anio),self.monthNumber,int(dia))
				efem.event = efe
				efem.mes = self
				efem.save()

@python_2_unicode_compatible
class Efemeride(models.Model):
	mes = models.ForeignKey(EfemerideMes)
	date = models.DateField('Fecha')
	event = models.CharField('Efemeride',max_length=300)

	def __str__(self):
		return self.date.strftime('Efemeride del %d, %b')

	class Meta:
		verbose_name='Efemeride'
		verbose_name_plural='Efemerides'

@python_2_unicode_compatible
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
	year = models.IntegerField('Año (Periodo inicio)', null=True,blank=True)
	yearEnd = models.IntegerField('Año (Periodo final)', null=True,blank=True)
	songString = models.TextField('Listado de canciones',blank=True)
	songString_org = models.TextField('Listado de canciones',blank=True)

	def formatHelper(self,matchobj):
		url = static(settings.MEDIA_URL+'archive/Discografias/'+matchobj.group(1))
		return ur'<audio controls preload="none"><source src="'+url+'" type="audio/mpeg">Su explorador es antiguo\. Actualicelo para reproducir audios\.</audio>'
		
	def save(self,*args,**kwargs):
		p = re.compile(ur'\[audio:([\w\/\.]+)\]', re.UNICODE)
		self.songString = re.sub(p,self.formatHelper,self.songString_org)
		self.songString = self.songString.replace('\n',r'<br>')
		super(Album,self).save(*args,**kwargs)

	class Meta:
		verbose_name='Album'
		verbose_name_plural='Albumes'

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class ImageAlbum(models.Model):
	alb = models.ForeignKey(Album, default=None)
	image = models.ImageField('Imagen',upload_to='images/', default='')
	description = models.CharField('Descripcion',max_length=200,blank=True)

	def __str__(self):
		return self.description

	class Meta:
		verbose_name='Imagen'
		verbose_name_plural='Imagenes'

@python_2_unicode_compatible
class Actividad(models.Model):
	title = models.CharField('Título', max_length=100)
	description = models.TextField('Descripción', max_length=2000)
	fecha = models.DateField('Fecha', default=date.today)


	def __str__(self):
		return self.title

	def htmlText(self,txt):
		texto = u'<p class="text-justify">'
		texto+= txt.replace(u'\n', u'</p><p class="text-justify">')
		texto+= u'\r</p>'
		texto = texto.replace(u'<p class="text-justify">\r</p>',u'')
		return texto

	class Meta:
		verbose_name='Actividad'
		verbose_name_plural='Actividades'
	

@python_2_unicode_compatible
class Video(models.Model):
	name = models.CharField(max_length=100)
	videos = models.ForeignKey(Actividad, default=None)
	link = models.FileField('Video', upload_to='videos/', validators=[validate_file_extension] ,default='')

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class ActividadImage(models.Model):
	name = models.CharField(max_length=100)
	act = models.ForeignKey(Actividad, default=None)
	link = models.ImageField('Imagen',upload_to='images/', default='')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Imagen'
		verbose_name_plural='Imagenes'