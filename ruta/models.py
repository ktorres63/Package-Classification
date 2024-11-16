from django.db import models
from paquetes.models import Paquete
from nodo.models import Nodo

class Ruta(models.Model):
    
    # Estado de la ruta, usando un campo IntegerField con choices
    ESTADO_CHOICES = [
        (0, 'Pendiente'),
        (1, 'Recibido en origen'),
        (2, 'En tránsito'),
        (3, 'Llegó a destino'),
        (4, 'Entregado al destinatario'),
    ]

    # ID autoincremental para la ruta
    id = models.AutoField(primary_key=True)
    
    # Relación con el paquete
    paquete = models.ForeignKey(
        Paquete, 
        on_delete=models.CASCADE,  # Si el paquete es eliminado, también lo será la ruta
    )
    
    # Relación con el nodo de inicio
    nodo_inicio = models.ForeignKey(
        Nodo,  
        related_name='rutas_inicio',  # Nombre inverso para acceder a las rutas desde el nodo de inicio
        on_delete=models.CASCADE,  
    )
    
    # Relación con el nodo de destino
    nodo_fin = models.ForeignKey(
        Nodo,  
        related_name='rutas_fin',  # Nombre inverso para acceder a las rutas desde el nodo de fin
        on_delete=models.CASCADE,  
    )
    
    # Tiempo estimado de la ruta (por ejemplo, en horas o minutos)
    duracion = models.FloatField(help_text="Tiempo estimado en minutos u horas")

    estado = models.IntegerField(choices=ESTADO_CHOICES, default=0)  # El estado por defecto será 'No trabajado'
    
    def actualizar_nodo_actual(self):
        """
        Actualiza el nodo_actual del paquete asociado según el estado de la ruta.
        """
        paquete = self.paquete

        if self.estado == 0:  # Pendiente
            paquete.nodo_actual = self.nodo_inicio
        elif self.estado in [1, 2]:  # Recibido o en tránsito
            paquete.nodo_actual = self.nodo_inicio
        elif self.estado == 3:  # Llegó a destino
            paquete.nodo_actual = self.nodo_fin
        elif self.estado == 4:  # Entregado al destinatario
            paquete.nodo_actual = None  # Ya no está en ningún nodo activo
        
        paquete.save()


    def __str__(self):
        return f'Ruta {self.id} - Paquete {self.paquete.id} - Desde {self.nodo_inicio} Hasta {self.nodo_fin} - Estado: {self.get_estado_display()}'
    
    