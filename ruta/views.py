from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Ruta, Paquete
from .serializers import RutaSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ObtenerRutaPorPaqueteYNodo(APIView):
    @swagger_auto_schema(
        operation_summary="ruta_api_get",
        operation_description="Obtengo la ruta a partir del id del paquete y del id del nodo.",
        responses={
            200: openapi.Response(
                description="Detalles de la ruta encontrada",
                examples={
                    "application/json": {
                        "ruta_id": 1,
                        "nodo_fin_id": 2,
                        "nodo_paquete_destino": 3
                    }
                }
            ),
            404: openapi.Response(
                description="Ruta no encontrada",
                examples={
                    "application/json": {
                        "detail": "Ruta no encontrada"
                    }
                }
            )
        }
    )
    def get(self, request, id_paquete, id_nodo_inicio):
        try:
            # Buscar la ruta que coincide con el paquete y nodo de inicio
            ruta = Ruta.objects.get(paquete_id=id_paquete, nodo_inicio_id=id_nodo_inicio)
        except Ruta.DoesNotExist:
            return Response({"detail": "Ruta no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        # Obtener el paquete asociado
        paquete = ruta.paquete

        
        # Retornar el ID de la ruta y nodo_fin_id
        return Response({
            "ruta_id": ruta.id,
            "nodo_fin_id": ruta.nodo_fin_id,
            "nodo_paquete_destino": paquete.nodo_destino.id if paquete and paquete.nodo_destino else None,
        }, status=status.HTTP_200_OK)

class ActualizarEstadoRuta(APIView):
    @swagger_auto_schema(
        operation_summary="ruta_api_update_by_Ids",
        operation_description=(
            "Este endpoint permite actualizar el estado de una ruta "
            "basándose en el ID del paquete y el ID del nodo de inicio."
        ),
    )
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
    @swagger_auto_schema(
        operation_summary="ruta_api_update",
        operation_description=(
            "Permite actualizar el estado de una ruta utilizando su ID. "
        ),
    )
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
    queryset = Ruta.objects.all().order_by('id')
    serializer_class = RutaSerializer

    @swagger_auto_schema(
        operation_summary="ruta_api_list",
        operation_description="Obtiene un listado de todas las rutas",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ObtenerUltimaRutaPorPaquete(APIView):

    @swagger_auto_schema(
        operation_summary="ruta_api_get_last_route",
        operation_description=(
            "Devuelve el ID de la última ruta generada para un paquete "
            "específico a partir de su ID."
        ),
        responses={
            200: openapi.Response(
                description="ID de la última ruta encontrada",
                examples={
                    "application/json": {
                        "id_ruta": 42
                    }
                }
            ),  
        }
    )
    def get(self, request, id_paquete):
        try:
            # Filtra las rutas por el paquete y obtiene la última creada
            ultima_ruta = Ruta.objects.filter(paquete_id=id_paquete).order_by('-id').first()

            if not ultima_ruta:
                return Response(
                    {"detail": "No se encontraron rutas para el paquete especificado"},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response({"id_ultima_ruta": ultima_ruta.id}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"detail": "Ocurrió un error inesperado", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )