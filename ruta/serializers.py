# en un archivo llamado serializers.py dentro de tu aplicación
from rest_framework import serializers
from .models import Ruta

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = ['estado']  # Solo permitimos modificar el campo 'estado'
