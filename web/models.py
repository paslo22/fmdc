from __future__ import unicode_literals
import re
from django.db import models
from copy import copy
from django.contrib.staticfiles.templatetags.staticfiles import static

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

	def formatHelper(self,matchobj):
		url = static('web/archive/Biografias/'+matchobj.group('path'))
		return r'<audio controls><source src="'+url+'" type="audio/mpeg">Su explorador es antiguo\. Actualicelo para reproducir audios\.</audio>'

	def htmlText(self,txt):
		texto = '<p class="text-justify">'
		texto+= txt.replace('\n', '</p><p class="text-justify">')
		texto+= '\r</p>'
		texto = texto.replace('<p class="text-justify">\r</p>','')
		texto = texto.replace('<p class="text-justify">IM\xc1GENES\r</p>','')
		texto = re.sub(r'<p class="text-justify">MUSICAS?\r</p>','<h3>Musicas</h3>',texto)
		texto = re.sub(r'<p class="text-justify">\[audio:(?P<path>[a-zA-Z0-9/\.]+)(\|titles=[a-zA-Z0-9]+)?\]\r</p>',self.formatHelper,texto)
		return texto

	def save(self, *args, **kwargs):
		self.text_org = self.text_org
		self.text = self.htmlText(self.text_org)
		super(Biografia, self).save(*args, **kwargs)

	class Meta:
		verbose_name='Biografia'
		verbose_name_plural='Biografias'

class Image(models.Model):
	bio = models.ForeignKey(Biografia, default=None)
	image = models.ImageField('Imagen',upload_to='images/', default='')
	description = models.CharField('Descripcion',max_length=70)

	class Meta:
		verbose_name='Imagen'
		verbose_name_plural='Imagenes'

class Efemeride(models.Model):
	bio = models.ForeignKey(Biografia, default=None)
	date = models.DateField('Fecha')
	event = models.TextField('Efemeride')

	class Meta:
		verbose_name='Efemeride'
		verbose_name_plural='Efemerides'