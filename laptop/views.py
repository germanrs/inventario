# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView, CreateView

from laptop.forms import LaptopForm, IncidenteForm
from laptop.models import Laptop, Incidente

# Create your views here.
def index(request):
	return render(request, 'base/base.html')

class LaptopListar(ListView):
	model = Laptop
	template_name = 'laptop/listar_laptop.html'

class LaptopCrear(CreateView):
	model = Laptop
	form_class = LaptopForm
	template_name = 'laptop/crear_laptop.html'
	success_url = reverse_lazy('laptop:laptop_listar')

class IncidenteListar(ListView):
	model = Incidente
	template_name = 'laptop/listar_incidente.html'

class IncidenteCrear(CreateView):
	model = Incidente
	form_class = IncidenteForm
	template_name = 'laptop/crear_incidente.html'
	success_url = reverse_lazy('laptop:incidente_listar')