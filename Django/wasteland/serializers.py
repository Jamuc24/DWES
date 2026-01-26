# wasteland/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Superviviente, Perfil, Ubicacion, Objeto, Inventario, Mision, MisionAsignada

class UserSerializer(serializers.ModelSerializer):
    """Serializador para el modelo User de Django"""
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['id']

class SupervivienteSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Superviviente"""
    
    usuario_info = UserSerializer(source='usuario', read_only=True)
    esta_sano = serializers.BooleanField(read_only=True)
    nombre_mostrado = serializers.CharField(read_only=True)
    necesita_medicina = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Superviviente
        fields = [
            #Datos del usuario de Django
            'usuario', 'usuario_info',
            
            #Datos que ponemos al crear el superviviente
            'nombre', 'apellido', 'numero_vault', 'nivel', 'caps',
            'salud', 'radiacion',
            
            #Datos que se ponen solos
            'fecha_creacion', 'fecha_actualizacion',
            
            #Datos procedentes de funciones
            'esta_sano', 'nombre_mostrado', 'necesita_medicina'
        ]
        read_only_fields = ['fecha_creacion', 'fecha_actualizacion']
    
    def validate_salud(self, value):
        """Validación personalizada para salud"""
        if value < 0 or value > 100:
            raise serializers.ValidationError("La salud debe estar entre 0 y 100")
        return value
    
    def validate_radiacion(self, value):
        """Validación personalizada para radiación"""
        if value < 0 or value > 100:
            raise serializers.ValidationError("La radiación debe estar entre 0 y 100")
        return value
    
    def validate_nivel(self, value):
        """Validación personalizada para nivel"""
        if value < 1 or value > 50:
            raise serializers.ValidationError("El nivel debe estar entre 1 y 50")
        return value