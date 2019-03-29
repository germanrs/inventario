from django import forms

from donante.models import Donante

class DonanteForm(forms.ModelForm):

	class Meta:
		model = Donante

		fields = [
			'nombre',
			'direccion',
			'telefono',
			'email',
			'escuela',
			'donacion',
		]

		labels = {
			'nombre': 'Nombre',
			'direccion': 'Direccion',
			'telefono': 'Telefono',
			'email': 'Email',
			'escuela': 'Escuela',
			'donacion': 'Donacion'
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'escuela': forms.Select(attrs={'class': 'form-control'}),
			'donacion': forms.TextInput(attrs={'class': 'form-control'}),
		}