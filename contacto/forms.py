from django import forms

class FormularioContacto(forms.Form):
    
    nombre = forms.CharField(label='nombre',required=True,max_length=80)
    email = forms.CharField(label='email',required=True)

    contenido = forms.CharField(label='Contenido',widget=forms.Textarea)


