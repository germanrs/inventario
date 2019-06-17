# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

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
	uuid = models.CharField(max_length=36)
	modelo = models.CharField(max_length=1, choices=MODELOS_XO)

	def __str__(self):
		return self.serie

	def modelo_detalle(self):
		return dict(Laptop.MODELOS_XO)[self.modelo]

	#def get_persona(self):
	#	Try:
	#		return Persona.objects.get(pk=self.forenea)
	#	except:
	#		return None

	class Meta:
		ordering = ('id',)

class Componente(models.Model):
	nombre = models.CharField(max_length=15)

	def __str__(self):
		return self.nombre

class Incidente(models.Model):
	TIPO_INCIDENTE_LAPTOP = (
		('1', 'Revision'),
		('2', 'Defecto'),
		('3', 'Daño'),
	)
	PRIORIDAD_INCIDENTE_LAPTOP = (
		('1', 'Urgente'),
		('2', 'Mayor'),
		('3', 'Menor'),
	)
	created_at = models.DateTimeField(auto_now_add=True)
	descripcion = models.CharField(max_length=50)
	detalle = models.TextField(blank=True)
	solucion = models.TextField(blank=True)
	laptop = models.ForeignKey(Laptop, blank=True)
	componente = models.ManyToManyField(Componente, blank=False)
	tipo_incidente = models.CharField(max_length=1, choices=TIPO_INCIDENTE_LAPTOP, default=1)
	prioridad_incidente = models.CharField(max_length=1, choices=PRIORIDAD_INCIDENTE_LAPTOP, default=3)
	# True - Reparado
	# False - Pendiente reparacion
	estado = models.BooleanField(default=False)

	def f_creacion(self):
		return self.created_at.strftime('%B %d %Y')

	def __str__(self):
		return '{} {} {} {}'.format(self.created_at, self.descripcion, self.detalle, self.laptop, self.componente)

	def tipo_incidente_detalle(self):
		return dict(Incidente.TIPO_INCIDENTE_LAPTOP)[self.tipo_incidente]

	def prioridad_incidente_detalle(self):
		return dict(Incidente.PRIORIDAD_INCIDENTE_LAPTOP)[self.prioridad_incidente]

	def estado_incidente_detalle(self):
		if self.estado == True:
			return 'Reparado'
		else:
			return 'Pendiente'
