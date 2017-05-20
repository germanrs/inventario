from django import forms

from django.contrib.admin import widgets

from escuela.models import Persona, Escuela, Visita

class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona

		fields = [
			'nombre',
			'apellido',
			'telefono',
			'laptop',
			'escuela',
			'grado',
		]

		labels = {
			'nombre': 'Nombre:',
			'apellido': 'Apellido:',
			'telefono': 'Telefono:',
			'laptop': 'XO:',
			'escuela': 'Escuela:',
			'grado': 'Grado:',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control'}),
			'laptop': forms.Select(attrs={'class': 'form-control'}),
			'escuela': forms.Select(attrs={'class': 'form-control'}),
			'grado': forms.Select(attrs={'class': 'form-control'}),
		}

class EscuelaForm(forms.ModelForm):

	class Meta:
		model = Escuela

		fields = [
			'nombre',
			'departamento',
			'municipio',
			'direccion',
			'telefono',
		]

		labels = {
			'nombre': 'Nombre: ',
			'departamento': 'Departamento',
			'municipio': 'Municipio',
			'direccion': 'Direccion',
			'telefono': 'Telefono',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'departamento': forms.Select(attrs={'class': 'form-control'}),
			'municipio': forms.Select(attrs={'class': 'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
		}

class VisitaForm(forms.ModelForm):

	class Meta:
		model = Visita

		fields = [
			'titulo',
			'fecha', 
			'escuela',
			'tipo_visita',
			'objetivo',
			'descripcion',
			'avances',
		]

		labels = {
			'titulo': 'Titulo de la visita',
			'fecha': 'Fecha de la visita', 
			'escuela': 'Escuela',
			'tipo_visita': 'Tipo de visita',
			'objetivo': 'Objetivo de la visita',
			'descripcion': 'Descripcion de la visita',
			'avances': 'Avances encontrados',
		}

		widgets = {
			'titulo':  forms.TextInput(attrs={'class':'form-control'}),
			'fecha':  forms.DateInput(format='%d/%m/%Y'),
			'escuela': forms.Select(attrs={'class':'form-control'}),
			'tipo_visita': forms.Select(attrs={'class':'form-control'}),
			'objetivo': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'avances': forms.TextInput(attrs={'class':'form-control'}),
			
		}