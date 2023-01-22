from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre + ""+ self.area + "" + str(self.email)


class Gimnasio(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    
    
    def __str__(self):
        return self.nombre +"" +str(self.direccion) +""+str(self.email)