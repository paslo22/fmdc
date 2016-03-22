from __future__ import unicode_literals
import re
from django.db import models

class Biografia(models.Model):
	name = models.CharField('Nombre',max_length=70)
	text = models.TextField('Texto')

	def __str__(self):
		return self.name

	def htmlText(self,txt):
		texto = '<p>'
		texto+= txt.replace('\n', '</p><p>')
		texto+= '\r</p>'
		texto = texto.replace('<p>\r</p>','')
		texto = texto.replace('<p>IM\xc1GENES\r</p>','<h3>Imagenes</h3>')
		texto = texto.replace('<p>MUSICAS\r</p>','<h3>Musicas</h3>')
		texto = re.sub(r'<p>\[audio:(?P<path>[a-zA-Z0-9/\.]+)\|titles=[a-zA-Z0-9]+\]\r</p>',r'<audio controls><source src="\1" type="audio/mpeg">Your browser does not support the audio element.</audio>',texto)
		return texto

	def save(self, *args, **kwargs):
		self.name = self.name
		self.text = self.htmlText(self.text)
		super(Biografia, self).save(*args, **kwargs)