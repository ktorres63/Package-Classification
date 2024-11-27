from rest_framework import generics
from .models import Paquete
from .serializers import PaqueteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from nodo.models import Nodo  



class PaqueteCreateView(generics.CreateAPIView):
    queryset = Paquete.objects.all()
    serializer_class = PaqueteSerializer

class PaqueteListView(generics.ListAPIView):
    queryset = Paquete.objects.all()
    serializer_class = PaqueteSerializer


class PaqueteUbicacionActualView(APIView):
    """
    Vista para obtener la ubicación actual de un paquete según su id.
    """
    def get(self, request, id_paquete):
        try:
            # Obtiene el paquete según el id proporcionado
            paquete = Paquete.objects.get(id=id_paquete)
            
            # Verifica si el paquete tiene un nodo actual asignado
            if paquete.nodo_actual:
                ubicacion_actual = paquete.nodo_actual.nombre  # O el campo relevante del nodo
            else:
                ubicacion_actual = "No asignado"
            
            # Retorna la ubicación actual
            return Response({"paquete_id": paquete.id, "ubicacion_actual": ubicacion_actual}, status=status.HTTP_200_OK)
        
        except Paquete.DoesNotExist:
            # Retorna un error si el paquete no existe
            return Response({"detail": "Paquete no encontrado"}, status=status.HTTP_404_NOT_FOUND)