from django.db import models
from paquetes.models import Paquete
from nodo.models import Nodo  

class Ruta(models.Model):
    paquete = models.ForeignKey(
        Paquete, 
        on_delete=models.CASCADE,  
    )

    nodo_inicio = models.ForeignKey(
        Nodo,  
        related_name='ruta_inicio',  
        on_delete=models.CASCADE,  
    )

    nodo_fin = models.ForeignKey(
        Nodo,  
        related_name='ruta_fin', 
        on_delete=models.CASCADE,  
    )
    tiempo = models.FloatField() #peso del nodo
    estado = models.FloatField()

    # 0: No trabajado
    # 1: Recibido
    # 2: Transito
    # 3: Entregado
    # 4: Entregado al cliente

    def __str__(self):
        return f'Ruta Paquete {self.paquete.id} - Inicio: {self.nodo_inicio} Fin: {self.nodo_fin} Tiempo: {self.tiempo}'
   