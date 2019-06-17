# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Donante(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=90)
	telefono = models.CharField(max_length=10)
	email = models.EmailField(max_length=30)
	# escuela = models.ForeignKey(Escuela, null=True, blank=True, on_delete=models.CASCADE)
	# donacion = models.FloatField(default=0, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)
		
