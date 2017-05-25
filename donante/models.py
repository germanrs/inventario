# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from escuela.models import Escuela

# Create your models here.
class Donante(models.Model):
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length=30)
	telefono = models.CharField(max_length=10)
	email = models.EmailField(max_length=30,blank=True)
	escuela = models.ForeignKey(Escuela, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return '{} {}'.format(self.nombre, self.escuela,)
		
