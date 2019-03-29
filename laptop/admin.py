# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.contrib import admin

from laptop.models import Laptop, Incidente, Componente

# https://simpleisbetterthancomplex.com/packages/2016/08/11/django-import-export.html
from import_export.admin import ImportExportModelAdmin

# Register your models here.

#admin.site.register(Laptop)

admin.site.register(Incidente)

admin.site.register(Componente)

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('id', 'serie', 'uuid', 'modelo')
admin.site.register(Laptop, LaptopAdmin)

#@admin.register(Laptop)
#class LaptopAdmin(ImportExportModelAdmin):
#    pass