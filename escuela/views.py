# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from escuela.forms import PersonaForm, EscuelaForm, VisitaForm
from escuela.models import Persona, Escuela, Visita

# Create your views here.
class PersonaListar(ListView):
	model = Persona
	template_name = 'escuela/listar_persona.html'
	context_object_name = 'personas'  # Default: object_list
	paginate_by = 10
	queryset = Persona.objects.all()

class PersonaCrear(CreateView):
	model = Persona
	form_class = PersonaForm
	template_name = 'escuela/crear_persona.html'
	success_url = reverse_lazy('escuela:listar_persona')

class PersonaEditar(UpdateView):
	model = Persona
	form_class = PersonaForm
	template_name = 'escuela/crear_persona.html'
	success_url = reverse_lazy('escuela:listar_persona')

class PersonaBorrar(DeleteView):
	model = Persona
	template_name = 'escuela/borrar_persona.html'
	success_url = reverse_lazy('escuela:listar_persona')

class EscuelaListar(ListView):
	model = Escuela
	template_name = 'escuela/listar_escuela.html'

class EscuelaCrear(CreateView):
	model = Escuela
	form_class = EscuelaForm
	template_name = 'escuela/crear_escuela.html'
	success_url = reverse_lazy('escuela:listar_escuela')

class VisitaListarA(ListView):
	model = Visita
	template_name = 'escuela/listar_visita.html'

class VisitaListarB(ListView):
    model = Visita
    template_name = 'escuela/listar_visitaa.html'

class VisitaCrear(CreateView):
	model = Visita
	form_class = VisitaForm
	template_name = 'escuela/crear_visita.html'
	success_url = reverse_lazy('escuela:listar_visita')
