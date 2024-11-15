from django.db import models
from usuarios.models import Usuario
from nodo.models import Nodo  


class Paquete(models.Model):
    id = models.AutoField(primary_key=True)        # ID del paquete (clave primaria)
    usuario = models.ForeignKey(
        Usuario,  # Referencia al modelo Usuario
        to_field='dni',  # Especificar que la clave foránea se relaciona con el campo 'dni'
        on_delete=models.CASCADE,  # Eliminar el paquete si el usuario se elimina
    )
    nodo_origen = models.ForeignKey(
        Nodo,  # Referencia al modelo Nodo
        related_name='paquetes_origen',  # Nombre relacionado para acceder desde Nodo
        on_delete=models.CASCADE,  # Eliminar el paquete si el nodo origen se elimina
    )
    nodo_destino = models.ForeignKey(
        Nodo,  # Referencia al modelo Nodo
        related_name='paquetes_destino',  # Nombre relacionado para acceder desde Nodo
        on_delete=models.CASCADE,  # Eliminar el paquete si el nodo destino se elimina
    )
    nodo_actual = models.ForeignKey(  # Campo para almacenar el nodo actual
        Nodo,
        related_name='paquetes_actuales',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Nodo actual en el que se encuentra el paquete"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación del paquete

    def __str__(self):
        return f'Paquete {self.id} - Usuario: {self.usuario.dni}'
