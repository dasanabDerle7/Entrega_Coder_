from django import forms

class cursoFormulario(forms.Form):
    curso=forms.CharField()
    camada=forms.IntegerField()


class profesorFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=40)
 

