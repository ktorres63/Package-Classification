from django.db import models
from paquetes.models import Paquete
from nodo.models import Nodo  



class Ruta(models.Model):
    paquete = models.ForeignKey(
        Paquete,  # Referencia al modelo Paquete
        on_delete=models.CASCADE,  # Si se elimina el paquete, se elimina la ruta
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
    def __str__(self):
        return f'Ruta Paquete {self.paquete.id} - Inicio: {self.nodo_inicio} Fin: {self.nodo_fin}'