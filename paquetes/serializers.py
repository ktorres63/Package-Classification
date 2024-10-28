# serializers.py
from rest_framework import serializers
from .models import Paquete

class PaqueteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paquete
        fields = ['id', 'usuario', 'nodo_origen', 'nodo_destino', 'fecha_creacion']
        read_only_fields = ['id', 'fecha_creacion']
