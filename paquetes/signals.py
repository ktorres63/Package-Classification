from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Paquete
from nodo.models import Nodo
from ruta.models import Ruta
from services.graph import grafo
import networkx as nx
from django.db import transaction

@receiver(post_save, sender=Paquete)
def crear_ruta_para_paquete(sender, instance, created, **kwargs):
    if created:
        try:
            with transaction.atomic():
                nodo_inicio = instance.nodo_origen
                nodo_fin = instance.nodo_destino
                grafo_actual = grafo()

                # Calcular la ruta más corta entre nodo_inicio y nodo_fin
                ruta_mas_corta = nx.shortest_path(
                    grafo_actual, source=nodo_inicio.alias, target=nodo_fin.alias, weight='weight'
                )

                tiempo_total = 0  # Inicializa el tiempo total

                # Almacenar las rutas en la base de datos
                for i in range(len(ruta_mas_corta) - 1):
                    nodo_origen = ruta_mas_corta[i]
                    nodo_destino = ruta_mas_corta[i + 1]

                    # Obtener los nodos desde la base de datos
                    nodo_origen_bd = Nodo.objects.get(alias=nodo_origen)
                    nodo_destino_bd = Nodo.objects.get(alias=nodo_destino)

                    peso = grafo_actual[nodo_origen][nodo_destino]['weight']
                    tiempo_total += peso

                    Ruta.objects.create(
                        paquete=instance,
                        nodo_inicio=nodo_origen_bd,
                        nodo_fin=nodo_destino_bd,
                        duracion=peso,
                        estado=0  # Estado inicial
                    )

                print(f"Tiempo total de la ruta de {nodo_inicio} a {nodo_fin}: {tiempo_total}")

        except nx.NetworkXNoPath:
            print(f"No hay ruta disponible entre {nodo_inicio} y {nodo_fin}.")
        except Nodo.DoesNotExist:
            print("Error: Uno de los nodos no existe en la base de datos.")