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
    
def create(self, validated_data):
        """
        Sobrescribimos el método create para manejar la creación de usuario
        si no se proporciona uno
        """
        # Si no viene usuario en los datos validados, creamos uno automático
        if 'usuario' not in validated_data:
            from django.contrib.auth.models import User
            import time
            
            # Generar nombre de usuario único basado en timestamp
            timestamp = int(time.time())
            username = f"jugador_{timestamp}"
            
            # Crear usuario automático
            usuario = User.objects.create_user(
                username=username,
                password='temp_password_123',  # Contraseña temporal
                email=f'{username}@ejemplo.com'
            )
            
            # Añadir el usuario a los datos validados
            validated_data['usuario'] = usuario
        
        # Llamar al create original de ModelSerializer (guarda el Superviviente)
        return super().create(validated_data)

class ObjetoSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Objeto (armas, armaduras, medicina, etc.)"""
    class Meta:
        model = Objeto
        fields = '__all__'
    
    def validate_valor(self, value):
        """El valor no puede ser negativo"""
        if value < 0:
            raise serializers.ValidationError("El valor no puede ser negativo")
        return value
