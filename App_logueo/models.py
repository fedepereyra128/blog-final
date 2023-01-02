from django.db import models
from django.contrib.auth.models import  User

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
    imagen=models.ImageField(upload_to="media", null= True)
    cuerpo=models.CharField(max_length=150)

