# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from laptop.models import Laptop

# Create your models here.
class Departamento(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre

class Municipio(models.Model):
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre

class Escuela(models.Model):
	nombre = models.CharField(max_length=30)
	departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
	municipio = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE)
	direccion = models.CharField(max_length=30)
	telefono = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre

class Persona(models.Model):
	ROL_E =(
		('K', 'Preescolar'),
		('1', '1-Primer'),
		('2', '2-Segundo'),
		('3', '3-Tercer'),
		('4', '4-Cuarto'),
		('5', '5-Quinto'),
		('6', '6-Sexto'),
		('D', 'Docente'),
		('P', 'Director'),
		('V', 'Voluntario'),
	)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	telefono = models.CharField(max_length=10)
	laptop = models.OneToOneField(Laptop,null=True, blank=True, on_delete=models.CASCADE)
	escuela = models.ForeignKey(Escuela,null=True, blank=True, on_delete=models.CASCADE)
	grado = models.CharField(max_length=1, choices=ROL_E, blank=True)

	def __str__(self):
		return '{} {} {} {}'.format(self.nombre, self.laptop, self.escuela, self.grado)

	def grado_detalle(self):
		return dict(Persona.ROL_E)[self.grado]

class Visita(models.Model):
	T_VISITA = (
		('1', 'Educativa'),
		('2', 'Tecnico'),
		('3', 'Logistico'),
		)
	titulo = models.CharField(max_length=30)
	fecha = models.DateField()
	escuela = models.ForeignKey(Escuela, null=True, blank=False, on_delete=models.CASCADE)
	tipo_visita = models.CharField(max_length=1, choices=T_VISITA, blank=False)
	objetivo = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=250)
	avances = models.CharField(max_length=100)

	def __str__(self):
		return '{} {} {}'.format(self.fecha, self.titulo, self.escuela, self.tipo_visita, )

	def visita_detalle(self):
		return dict(tipo_visita.T_VISITA)[self.tipo_visita]

#class Conectividad(models.Model):


