import heapq
from .models import Nodo, Ruta

def dijkstra(nodo_inicial):
    # Obtener todos los nodos y construir el grafo
    nodos = Nodo.objects.all()
    grafo = construir_grafo(nodos)  # Función para crear el grafo desde los nodos y rutas

    # Diccionario para las distancias más cortas
    distancias = {nodo: float('infinity') for nodo in nodos}
    distancias[nodo_inicial] = 0

    # Cola de prioridad para Dijkstra
    pq = [(0, nodo_inicial)]  # (distancia, nodo)

    while pq:
        distancia_actual, nodo_actual = heapq.heappop(pq)

        # Ignorar si ya hemos encontrado una ruta más corta
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Explorar los vecinos (nodos conectados)
        for vecino, peso in grafo[nodo_actual]:
            distancia = distancia_actual + peso

            # Si encontramos una ruta más corta
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(pq, (distancia, vecino))

    return distancias

def construir_grafo(nodos):
    grafo = {}
    for nodo in nodos:
        rutas = Ruta.objects.filter(origen=nodo)  # Rutas que salen de este nodo
        grafo[nodo] = [(ruta.destino, ruta.distancia) for ruta in rutas]
    return grafo
