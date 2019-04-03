# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from laptop.forms import LaptopForm, IncidenteForm
from laptop.models import Laptop, Incidente
from escuela.models import Persona

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
	return render(request, 'base/base2.html')

class LaptopListar(ListView):
	model = Laptop
	template_name = 'laptop/listar_laptop.html'
	context_object_name = 'laptops'  # Default: object_list
	paginate_by = 10
	queryset = Laptop.objects.all()

#class LaptopListar(DetailView):

#	model = Laptop

#	template_name = 'laptop/listar_laptop.html'

#	def get_context_data(self, **kwargs):
#		context = super(LaptopListar, self).get_context_data(**kwargs)

#		return context

class LaptopCrear(CreateView):
	model = Laptop
	form_class = LaptopForm
	template_name = 'laptop/crear_laptop.html'
	success_url = reverse_lazy('laptop:listar_laptop')

class LaptopEditar(UpdateView):
	model = Laptop
	form_class = LaptopForm
	template_name = 'laptop/crear_laptop.html'
	success_url = reverse_lazy('laptop:listar_laptop')

class LaptopBorrar(DeleteView):
	model = Laptop
	template_name = 'laptop/borrar_laptop.html'
	success_url = reverse_lazy('laptop:listar_laptop')

class IncidenteListar(ListView):
	model = Incidente
	template_name = 'laptop/listar_incidente.html'
	context_object_name = 'incidentes'  # Default: object_list
	paginate_by = 10
	queryset = Incidente.objects.all()

class IncidenteCrear(CreateView):
	model = Incidente
	form_class = IncidenteForm
	template_name = 'laptop/crear_incidente.html'
	success_url = reverse_lazy('laptop:listar_incidente')

class IncidenteEditar(UpdateView):
	model = Incidente
	form_class = IncidenteForm
	template_name = 'laptop/crear_incidente.html'
	success_url = reverse_lazy('laptop:listar_incidente')

class IncidenteBorrar(DeleteView):
	model = Incidente
	template_name = 'laptop/borrar_incidente.html'
	success_url = reverse_lazy('laptop:listar_incidente')
