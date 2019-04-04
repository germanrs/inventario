# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from escuela.models import Departamento, Municipio, Escuela, Persona, Visita

# https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Departamento)

admin.site.register(Municipio)

admin.site.register(Escuela)

#admin.site.register(Persona)

admin.site.register(Visita)

@admin.register(Persona)
class PersonaAdmin(ImportExportModelAdmin):
	list_display = ('id', 'nombre', 'apellido', 'telefono', 'laptop', 'escuela', 'grado' )
	pass
