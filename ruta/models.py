from django.db import models
from paquetes.models import Paquete
from nodo.models import Nodo  



class Ruta(models.Model):
    paquete = models.ForeignKey(
        Paquete,  # Referencia al modelo Paquete
        on_delete=models.CASCADE,  # Si se elimina el paquete, se elimina la ruta
    )
    @property
    def nodo_origen(self):
        return self.paquete.nodo_origen

    @property
    def nodo_destino(self):
        return self.paquete.nodo_destino
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la ruta

    def __str__(self):
        return f'Ruta de Paquete {self.paquete.id} - Origen: {self.nodo_origen.nombre} Destino: {self.nodo_destino.nombre}'