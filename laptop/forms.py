from django import forms

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