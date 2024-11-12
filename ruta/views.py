from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ruta, Paquete
from .serializers import RutaSerializer

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

        # Actualizar el nodo_actual del paquete en función del estado de la ruta
        paquete = ruta.paquete

        if estado == 0:  # Pendiente
            paquete.nodo_actual = ruta.nodo_inicio
        elif estado in [1, 2]:  # Recibido o en tránsito
            paquete.nodo_actual = ruta.nodo_inicio
        elif estado == 3:  # Llegó a destino
            paquete.nodo_actual = ruta.nodo_fin
        elif estado == 4:  # Entregado al destinatario
            paquete.nodo_actual = None  # Ya no está en ningún nodo activo
        paquete.save()

        # Serializar la ruta actualizada
        serializer = RutaSerializer(ruta)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RutaListView(generics.ListAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
