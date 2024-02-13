from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class ProductoAirsoft(models.Model):
    nombre_producto = models.TextField()
    tienda = models.TextField()
    ubicacion = models.TextField()
    edad_usuario = models.IntegerField()

    def __str__(self):
        return self.nombre_producto

"""
class AirsoftUser(AbstractUser):
    birth_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
"""