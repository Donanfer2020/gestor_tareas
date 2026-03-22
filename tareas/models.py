from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return self.nombre