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