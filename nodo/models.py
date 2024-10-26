from django.db import models

class Nodo(models.Model):
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=6)       
    latitud = models.FloatField()                 
    longitud = models.FloatField()                  
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
