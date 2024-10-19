from django.db import models

# Create your models here.
class Ruta(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la ruta
    origen = models.CharField(max_length=255)   # Ciudad o lugar de origen
    destino = models.CharField(max_length=255)  # Ciudad o lugar de destino
    distancia_km = models.FloatField()           # Distancia en kilómetros
    tiempo_estimado_horas = models.FloatField()  # Tiempo estimado en horas
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la ruta

    def __str__(self):
        return f'{self.nombre} ({self.origen} - {self.destino})'