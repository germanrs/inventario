# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from escuela.models import Departamento, Municipio, Escuela, Persona, Visita
from laptop.models import Laptop

# https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html
from import_export.admin import ImportExportModelAdmin

from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget


# Register your models here.

admin.site.register(Departamento)

admin.site.register(Municipio)

admin.site.register(Escuela)

admin.site.register(Visita)

class PersonaResource(resources.ModelResource):
    laptop = fields.Field(
        column_name='laptop',
        attribute='laptop',
        widget=ForeignKeyWidget(Laptop, 'serie'))

    escuela = fields.Field(
    	column_name='escuela',
    	attribute='escuela',
    	widget=ForeignKeyWidget(Escuela, 'nombre'))

    class Meta:
    	# fields = ('id', 'nombre', 'apellido', 'telefono', 'laptop', 'escuela', 'grado',)
        model = Persona

class PersonaAdmin(ImportExportModelAdmin):
	resource_class = PersonaResource
	list_display = ('id', 'nombre', 'apellido', 'telefono', 'laptop', 'escuela', 'grado')
	pass

admin.site.register(Persona, PersonaAdmin)
