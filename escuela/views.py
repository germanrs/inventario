# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView

from escuela.forms import PersonaForm, EscuelaForm, VisitaForm
from escuela.models import Persona, Escuela, Visita

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from laptop.models import Laptop

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

class VisitaCrear(CreateView):
	model = Visita
	form_class = VisitaForm
	template_name = 'escuela/crear_visita.html'
	success_url = reverse_lazy('escuela:listar_visita')

class VisitaListar(ListView):
	model = Visita
	template_name = 'escuela/listar_visita.html'

class VisitaEditar(UpdateView):
	model = Visita
	form_class = VisitaForm
	template_name = 'escuela/crear_visita.html'
	success_url = reverse_lazy('escuela:listar_listar')

class VisitaBorrar(DeleteView):
	model = Visita
	template_name = 'escuela/borrar_visita.html'
	success_url = reverse_lazy('escuela:listar_visita')

User = get_user_model()

class Reporte1(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'escuela/charts1.html')

class Reporte2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'escuela/charts2.html')

class Reporte3(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'escuela/charts3.html')	

class Reporte4(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'escuela/charts4.html')

class Reporte5(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'escuela/charts5.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_xo_1 = Laptop.objects.filter(modelo=1).count()
        qs_xo_2 = Laptop.objects.filter(modelo=2).count()
        qs_xo_3 = Laptop.objects.filter(modelo=3).count()
        qs_xo_4 = Laptop.objects.filter(modelo=4).count()
        qs_nl3 = Laptop.objects.filter(modelo=5).count()
#       qs_escuela_1 = Persona.objects.filter(escuela='1').count()
#       qs_escuela_2 = Persona.objects.filter(escuela='2').count()
#       qs_escuela_3 = Persona.objects.filter(escuela='3').count()
# 		qs_count = User.objects.all().count()
        data = {
            "labels": ["XO-1", "XO-1.5", "XO-1.75", "XO-4", "NL3"],
            "data": [qs_xo_1, qs_xo_2, qs_xo_3, qs_xo_4, qs_nl3],
        }
        return Response(data)
