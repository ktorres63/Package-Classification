from rest_framework import serializers
from .models import Nodo 

class NodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nodo
        fields = ['nombre', 'latitud','longitud', 'fecha_creacion']  # Añade los campos que deseas

    def create(self, validated_data):
        nodo = Nodo(**validated_data)
        nodo.save()  
        return nodo

