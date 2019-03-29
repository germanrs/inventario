# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from donante.forms import DonanteForm
from donante.models import Donante

# Create your views here.
class DonanteListar(ListView):
	model = Donante
	template_name = 'escuela/listar_donante.html'

class DonanteCrear(CreateView):
	model = Donante
	form_class = DonanteForm
	template_name = 'escuela/crear_donante.html'
	success_url = reverse_lazy('escuela:listar_donante')

class DonanteEditar(UpdateView):
	model = Donante
	form_class = DonanteForm
	template_name = 'escuela/crear_donante.html'
	success_url = reverse_lazy('escuela:listar_donante')

class DonanteBorrar(DeleteView):
	model = Donante
	template_name = 'escuela/borrar_donante.html'
	success_url = reverse_lazy('escuela:listar_donante')