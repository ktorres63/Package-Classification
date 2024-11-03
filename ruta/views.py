from django.shortcuts import render
from rest_framework import generics
from .models import Ruta
from .serializers import RutaSerializer

class RutaUpdateEstadoView(generics.UpdateAPIView):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    lookup_field = 'id'  # Este campo usa el id de la Ruta en la URL para actualizar

