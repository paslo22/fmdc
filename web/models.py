from __future__ import unicode_literals
import re
from django.db import models
from django.contrib.staticfiles.templatetags.staticfiles import static

class Biografia(models.Model):
	name = models.CharField('Nombre',max_length=70)
	text = models.TextField('Texto')

	def __str__(self):
		return self.name

	def formatHelper(self,matchobj):
		url = static('web/archive/'+matchobj.group('path'))
		return r'<audio controls><source src="'+url+'" type="audio/mpeg">Su explorador es antiguo\. Actualicelo para reproducir audios\.</audio>'

	def htmlText(self,txt):
		texto = '<p>'
		texto+= txt.replace('\n', '</p><p>')
		texto+= '\r</p>'
		texto = texto.replace('<p>\r</p>','')
		texto = texto.replace('<p>IM\xc1GENES\r</p>','<h3>Imagenes</h3>')
		texto = texto.replace('<p>MUSICAS\r</p>','<h3>Musicas</h3>')
		texto = re.sub(r'<p>\[audio:(?P<path>[a-zA-Z0-9/\.]+)\|titles=[a-zA-Z0-9]+\]\r</p>',self.formatHelper,texto)
		return texto

	def save(self, *args, **kwargs):
		self.name = self.name
		self.text = self.htmlText(self.text)
		super(Biografia, self).save(*args, **kwargs)