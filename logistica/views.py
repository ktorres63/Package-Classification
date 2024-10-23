from rest_framework.views import APIView
from rest_framework.response import Response
from .services import dijkstra
from .models import Nodo

class RutaOptimaView(APIView):
    def get(self, request, *args, **kwargs):
        nodo_origen_id = request.query_params.get('origen')
        nodo_destino_id = request.query_params.get('destino')

        # Obtener los nodos
        nodo_origen = Nodo.objects.get(id=nodo_origen_id)
        nodo_destino = Nodo.objects.get(id=nodo_destino_id)

        # Aplicar Dijkstra para obtener distancias
        distancias = dijkstra(nodo_origen)

        # Devolver la distancia al nodo destino
        return Response({
            'distancia': distancias[nodo_destino]
        })