from django import forms
from django.forms import ModelForm
from .models import Heroe


#   Formulario Basado den Modelos 
class HeroeForm(forms.ModelForm):
    class Meta:
        model = Heroe
        fields = '__all__'