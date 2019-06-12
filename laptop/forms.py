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
		]
		labels = {
			'descripcion': 'Descripcion',
			'laptop': 'Laptop',
			'detalle': 'Detalle',
			'componente': 'Componente',
		}
		widgets = {
			'descripcion': forms.TextInput(attrs={
				'class':'form-control'
				}),

			'laptop': forms.Select(attrs={
				'class': 'selectpicker',
				'data-live-search':'true'
				}),
			'detalle': forms.Textarea(),

			'componente': forms.CheckboxSelectMultiple(),
		}

		# widget=SelectMultiple(attrs={
  #               'class':'form-control selectpicker',
  #               'multiple data-actions-box':'true',
  #               'data-live-search':'true',
  #               'multiple title':'--- Please select ---',
  #               'multiple data-selected-text-format':'count > 2'
  #           }),