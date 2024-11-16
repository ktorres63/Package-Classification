from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ruta, Paquete
from .serializers import RutaSerializer

class ObtenerRutaPorPaqueteYNodo(APIView):
    def get(self, request, id_paquete, id_nodo_inicio):
        try:
            # Buscar la ruta que coincide con el paquete y nodo de inicio
            ruta = Ruta.objects.get(paquete_id=id_paquete, nodo_inicio_id=id_nodo_inicio)
        except Ruta.DoesNotExist:
            return Response({"detail": "Ruta no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        # Retornar el ID de la ruta y nodo_fin_id
        return Response({"ruta_id": ruta.id, "nodo_fin_id": ruta.nodo_fin_id}, status=status.HTTP_200_OK)

class ActualizarEstadoRuta(APIView):
    def put(self, request, id_paquete, id_nodo_inicio):
        try:
            ruta = Ruta.objects.get(paquete_id=id_paquete, nodo_inicio_id=id_nodo_inicio)
        except Ruta.DoesNotExist:
            return Response({"detail": "Ruta no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        # Obtener el nuevo estado
        estado = request.data.get("estado")
        if estado not in dict(Ruta.ESTADO_CHOICES).keys():
            return Response({"detail": "Estado no válido"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Actualizar el estado de la ruta
        ruta.estado = estado
        ruta.save()

        ruta.actualizar_nodo_actual()

        # Serializar la ruta actualizada
        serializer = RutaSerializer(ruta)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ActualizarEstadoPorRutaId(APIView):
    def put(self, request, id_ruta):
        try:
            ruta = Ruta.objects.get(id=id_ruta)
        except Ruta.DoesNotExist:
            return Response({"detail": "Ruta no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        estado = request.data.get("estado")
        if estado not in dict(Ruta.ESTADO_CHOICES).keys():
            return Response({"detail": "Estado no válido"}, status=status.HTTP_400_BAD_REQUEST)
        
        ruta.estado = estado
        ruta.save()

        # Llamar al método para actualizar nodo_actual del paquete
        ruta.actualizar_nodo_actual()

        serializer = RutaSerializer(ruta)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RutaListView(generics.ListAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
