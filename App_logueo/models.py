from django.db import models
from django.contrib.auth.models import  User
from ckeditor.fields import RichTextField

# Create your models here.

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="Avatares")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}- {self.imagen}"



class Nutricion(models.Model):
    autor=models.CharField(max_length=60)
    fecha=models.DateField()
    titulo=models.CharField(max_length=30)
    
    cuerpo=RichTextField(blank= True, null= True)

class MiPerfil(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=RichTextField(blank=True, null=True)
    email=models.EmailField(max_length=100)
    imagen=models.ImageField(upload_to="media", null=True)
