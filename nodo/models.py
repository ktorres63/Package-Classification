from django.db import models

class Nodo(models.Model):
    nombre = models.CharField(max_length=100)      # Nombre del nodo
    latitud = models.FloatField()                   # Latitud del nodo
    longitud = models.FloatField()                  # Longitud del nodo
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
