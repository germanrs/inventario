from django import forms

from escuela.models import Persona, Escuela

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