from django.db import models

# Create your models here.
class Guia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    experiencia = models.PositiveIntegerField()
    idiomas = models.TextField()
    especialidad = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.calificacion}"