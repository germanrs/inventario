# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from escuela.models import Departamento, Municipio, Escuela, Persona
# Register your models here.

admin.site.register(Departamento)

admin.site.register(Municipio)

admin.site.register(Escuela)

admin.site.register(Persona)