from __future__ import unicode_literals

from django.db import models

class Biografia(models.Model):
	name = models.CharField('Nombre',max_length=70)
	text = models.TextField('Texto')

	def __str__(self):
		return self.name