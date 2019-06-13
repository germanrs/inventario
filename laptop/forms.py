from django import forms
from django.forms import ModelForm

from laptop.models import Laptop, Incidente

class LaptopForm(forms.ModelForm):
	class Meta:
		model = Laptop
		fields = [
			'serie',
			'uuid',
			'modelo',
		]
		labels = {
			'serie': 'Numero de serie XO',
			'uuid': 'UUID de la XO',
			'modelo': 'Modelo de la XO',
		}
		widgets = {
			'serie': forms.TextInput(attrs={'class':'form-control'}),
			'uuid': forms.TextInput(attrs={'class': 'form-control'}),
			'modelo': forms.Select(attrs={'class': 'form-control'}),
		}

class IncidenteForm(forms.ModelForm):
	class Meta:
		model = Incidente

		fields = [
			'descripcion',
			'laptop',
			'detalle',
			'componente',
			'tipo_incidente',
			'prioridad_incidente',
			'solucion',
			'estado',
		]
		labels = {
			'descripcion': 'Descripcion',
			'laptop': 'Laptop',
			'detalle': 'Detalle',
			'componente': 'Componentes',
			'tipo_incidente': 'Tipo incidente',
			'prioridad_incidente': 'Prioridad incidente',
			'solucion': 'Solucion',
			'estado': 'Raparada',
		}
		widgets = {
			'descripcion': forms.TextInput(attrs={
				'class':'form-control'
				}),
			'laptop': forms.Select(attrs={
				'class': 'selectpicker',
				'data-live-search':'true'
				}),
			'detalle': forms.Textarea(attrs={
				'rows': '4',
				'placeholder': 'Describa los detalles del problema en la laptop.'
				}),
			'solucion': forms.Textarea(attrs={
				'rows': '4',
				'placeholder': 'Describa los detalles de la repacion realizada a la laptop.'
				}),			
			'componente': forms.CheckboxSelectMultiple(attrs={
				'class': 'column-checkbox'
				}),
			'tipo_incidente': forms.Select(attrs={
				'class': 'form-control'
				}),
			'prioridad_incidente': forms.Select(attrs={
				'class': 'form-control'
				}),
			'estado': forms.CheckboxInput(),
		}