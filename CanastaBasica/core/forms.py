from django import forms
from .models import Encuest

class EncuestForm(forms.ModelForm):

	class Meta:
		model = Encuest
		fields = {
		'dep',
		'muni',
        'prod',
        'price',
		}
		labels = {
		'dep': 'Nombre del departamento',
        'muni': 'Nombre del municipio',
        'prod': 'Nombre del producto',
		'price': 'Precio',
		}

		widgets = {
		'dep': forms.Select(attrs={'class':'form-control'}),
        'muni': forms.Select(attrs={'class':'form-control'}),
        'prod': forms.Select(attrs={'class':'form-control'}),
		'price': forms.NumberInput(attrs={'class':'form-control'}),
		}
