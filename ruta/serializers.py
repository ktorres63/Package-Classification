from rest_framework import serializers
from .models import Ruta

class RutaSerializer(serializers.ModelSerializer):
    # Esto asegurará que los campos relacionados se serialicen por sus nombres o IDs
    nodo_inicio = serializers.StringRelatedField()  # o usa PrimaryKeyRelatedField() si prefieres ID
    nodo_fin = serializers.StringRelatedField()  # o usa PrimaryKeyRelatedField() si prefieres ID
    paquete = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Ruta
        fields = ['id', 'paquete', 'nodo_inicio', 'nodo_fin', 'duracion', 'estado']
