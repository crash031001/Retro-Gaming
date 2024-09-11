from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import get_rating
# Create your models here.

class JUEGOS(models.Model):
    NOMBRE = models.CharField(max_length=250)
    DESCRIPCION = models.TextField(default="")
    IMAGEN = models.TextField(default="")
    CANT_JUGADORES = models.CharField(max_length=2)
    PESO = models.CharField(max_length=10)
    GENERO = models.CharField(max_length=20)
    FECHA = models.DateField()
    PREMIOS = models.TextField(default='')
    rating = models.CharField(max_length=3,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.NOMBRE
    
    def actualizar_rating(self):
        self.rating = get_rating(self.NOMBRE)
        self.save()