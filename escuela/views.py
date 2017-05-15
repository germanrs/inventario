# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView, CreateView

from escuela.forms import PersonaForm, EscuelaForm
from escuela.models import Persona, Escuela

# Create your views here.
class PersonaListar(ListView):
	model = Persona
	template_name = 'escuela/listar_persona.html'

class PersonaCrear(CreateView):
	model = Persona
	form_class = PersonaForm
	template_name = 'escuela/crear_persona.html'
	success_url = reverse_lazy('escuela:listar_persona')

class EscuelaListar(ListView):
	model = Escuela
	template_name = 'escuela/listar_escuela.html'

class EscuelaCrear(CreateView):
	model = Escuela
	form_class = EscuelaForm
	template_name = 'escuela/crear_escuela.html'
	success_url = reverse_lazy('escuela:listar_escuela')