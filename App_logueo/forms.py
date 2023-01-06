from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)


    class meta:
        model= User
        fields=["username", "emal", "password", "password2"]
        help_texts= {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email= forms.EmailField()
    password1=forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="confirme contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")


class meta:
    moder=User
    fields=["email", "password1", "password2", "first_name", "last_name"]



class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="imagen")



class nutriForm(forms.Form):
    autor=forms.CharField(max_length=30)
    fecha=forms.DateField()
    titulo=forms.CharField(max_length=30)
    imagen=forms.ImageField(label="imagen")
    cuerpo=forms.CharField(max_length=500)
    

