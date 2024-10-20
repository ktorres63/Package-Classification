from rest_framework import serializers
from .models import Usuario  

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['dni', 'nombres','apellidos', 'email']  # Añade los campos que deseas

    def create(self, validated_data):
        usuario = Usuario(**validated_data)
        usuario.save()  # Guarda el nuevo usuario
        return usuario