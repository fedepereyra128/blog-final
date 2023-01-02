from django import forms

class ProfesorForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    area=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=50)



class GimnasioForm(forms.Form):
    nombre=forms.CharField(max_length=30)
    direccion=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=50)



    