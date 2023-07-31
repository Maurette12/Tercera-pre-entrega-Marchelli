from django import forms


class FutbolistaFormulario(forms.Form):
    nombre=forms.CharField(required=True, maxlength=64)
    apellido=forms.CharField(required=True, maxlength=64)
    posicion=forms.IntegerField(required=True, max_value=50000)