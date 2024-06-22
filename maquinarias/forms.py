from django import forms
from .models import Maquinaria

class MaquinariaForm(forms.ModelForm):
    class Meta:
        model = Maquinaria
        fields = ['nombre', 'imagen', 'caracteristicas']
