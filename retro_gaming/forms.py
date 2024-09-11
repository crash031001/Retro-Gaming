from django import forms

class Busqueda(forms.Form):
    query = forms.CharField(label='buscar')