from __future__ import unicode_literals
import re
from django.db import models
from copy import copy
from django.contrib.staticfiles.templatetags.staticfiles import static

class Biografia(models.Model):
	name = models.CharField('Nombre',max_length=70)
	text = models.TextField('Texto')
	text_org = models.TextField('Texto original')

	def __str__(self):
		return self.name

	def formatHelper(self,matchobj):
		url = static('web/archive/Biografias/'+matchobj.group('path'))
		return r'<audio controls><source src="'+url+'" type="audio/mpeg">Su explorador es antiguo\. Actualicelo para reproducir audios\.</audio>'

	def htmlText(self,txt):
		texto = '<p>'
		texto+= txt.replace('\n', '</p><p>')
		texto+= '\r</p>'
		texto = texto.replace('<p>\r</p>','')
		texto = texto.replace('<p>IM\xc1GENES\r</p>','')
		texto = re.sub(r'<p>MUSICAS?\r</p>','<h3>Musicas</h3>',texto)
		texto = re.sub(r'<p>\[audio:(?P<path>[a-zA-Z0-9/\.]+)\|titles=[a-zA-Z0-9]+\]\r</p>',self.formatHelper,texto)
		return texto

	def save(self, *args, **kwargs):
		self.name = self.name
		self.text_org = self.text_org
		self.text = self.htmlText(self.text_org)
		super(Biografia, self).save(*args, **kwargs)

	class Meta:
		verbose_name='Biografia'
		verbose_name_plural='Biografias'

class Image(models.Model):
	bio = models.ForeignKey(Biografia, default=None)
	image = models.ImageField('Imagen',upload_to='images/', default='')

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