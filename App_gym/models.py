from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre + "especializado en " + self.area + "podes contactarlo al " +self.email


class Gimnasio(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre+""+str(self.direccion)+""+self.email


