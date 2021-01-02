from django.db import models

# Create your models here.


class Tablaagenda(models.Model):
    nombre = models.CharField("Nombre", max_length=255, blank=True, null=True)
    apellido = models.CharField("Apellido", max_length=255, blank=True, null=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.nombre