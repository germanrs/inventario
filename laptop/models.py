# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Laptop(models.Model):
	MODELOS_XO =(
		('1', 'XO1'),
		('2', 'XO1.5'),
		('3', 'XO1.75'),
		('4', 'XO4'),
		('5', 'NL3'),
	)

	serie = models.CharField(max_length=11)
	uuid = models.CharField(max_length=32)
	modelo = models.CharField(max_length=1, choices=MODELOS_XO)

	def __str__(self):
		return self.serie

	def modelo_detalle(self):
		return dict(Laptop.MODELOS_XO)[self.modelo]

	class Meta:
		ordering = ('id',)

class Componente(models.Model):
	nombre = models.CharField(max_length=15)

	def __str__(self):
		return self.nombre

class Incidente(models.Model):
	descripcion = models.CharField(max_length=30)
	laptop = models.ForeignKey(Laptop, blank=True)
	componente = models.ManyToManyField(Componente, blank=True)

	def __str__(self):
		return '{} {} {}'.format(self.descripcion, self.laptop, self.componente)

