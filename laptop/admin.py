# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from laptop.models import Laptop, Incidente, Componente
# Register your models here.

admin.site.register(Laptop)

admin.site.register(Incidente)

admin.site.register(Componente)