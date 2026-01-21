# fallout/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Superviviente

# ============================================
# VISTA 1: SOLO PARA LISTAR (GET todos)
# ============================================
class SupervivienteListView(APIView):
    """
    Vista SOLO para listar todos los supervivientes (GET)
    """
    
    def get(self, request):
        """Obtener todos los supervivientes - JSON MANUAL"""
        supervivientes = Superviviente.objects.all()
        
        data = []
        for superviviente in supervivientes:
            superviviente_dict = {
                'id': superviviente.usuario.id,
                'nombre': superviviente.nombre,
                'apellido': superviviente.apellido,
                'numero_vault': superviviente.numero_vault,
                'nivel': superviviente.nivel,
                'caps': superviviente.caps,
                'salud': superviviente.salud,
                'radiacion': superviviente.radiacion,
                'fecha_creacion': superviviente.fecha_creacion,
                'fecha_actualizacion': superviviente.fecha_actualizacion,
                'esta_sano': superviviente.esta_sano,
                'nombre_mostrado': superviviente.nombre_mostrado,
                'necesita_medicina': superviviente.necesita_medicina,
            }
            data.append(superviviente_dict)
        
        return Response(data)


# ============================================
# VISTA 2: SOLO PARA CREAR (POST)
# ============================================
class SupervivienteCreateView(APIView):
    """
    Vista SOLO para crear un nuevo superviviente (POST)
    """
    
    def post(self, request):
        """Crear un nuevo superviviente - VALIDACIÓN MANUAL"""
        data = request.data
        
        errores = []
        
        # Validar campos requeridos
        if 'usuario' not in data:
            errores.append("El campo 'usuario' es requerido")
        elif not User.objects.filter(id=data['usuario']).exists():
            errores.append(f"El usuario con ID {data['usuario']} no existe")
        
        if 'nombre' not in data or not data['nombre']:
            errores.append("El campo 'nombre' es requerido")
            
        # Validar rango de salud
        if 'salud' in data:
            try:
                salud = int(data['salud'])
                if salud < 0 or salud > 100:
                    errores.append("La salud debe estar entre 0 y 100")
            except ValueError:
                errores.append("La salud debe ser un número entero")
        
        # Validar rango de radiación
        if 'radiacion' in data:
            try:
                radiacion = int(data['radiacion'])
                if radiacion < 0 or radiacion > 100:
                    errores.append("La radiación debe estar entre 0 y 100")
            except ValueError:
                errores.append("La radiación debe ser un número entero")
        
        # Validar rango de nivel
        if 'nivel' in data:
            try:
                nivel = int(data['nivel'])
                if nivel < 1 or nivel > 50:
                    errores.append("El nivel debe estar entre 1 y 50")
            except ValueError:
                errores.append("El nivel debe ser un número entero")
        
        if errores:
            return Response(
                {"errores": errores},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            usuario = User.objects.get(id=data['usuario'])
            
            if Superviviente.objects.filter(usuario=usuario).exists():
                return Response(
                    {"error": "Ya existe un superviviente para este usuario"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            superviviente = Superviviente.objects.create(
                usuario=usuario,
                nombre=data.get('nombre', ''),
                apellido=data.get('apellido', ''),
                numero_vault=data.get('numero_vault', '101'),
                nivel=int(data.get('nivel', 1)),
                caps=int(data.get('caps', 100)),
                salud=int(data.get('salud', 100)),
                radiacion=int(data.get('radiacion', 0)),
            )
            
            response_data = {
                'id': superviviente.usuario.id,
                'nombre': superviviente.nombre,
                'apellido': superviviente.apellido,
                'numero_vault': superviviente.numero_vault,
                'nivel': superviviente.nivel,
                'caps': superviviente.caps,
                'salud': superviviente.salud,
                'radiacion': superviviente.radiacion,
                'fecha_creacion': superviviente.fecha_creacion,
                'esta_sano': superviviente.esta_sano,
                'nombre_mostrado': superviviente.nombre_mostrado,
                'necesita_medicina': superviviente.necesita_medicina,
                'mensaje': 'Superviviente creado exitosamente'
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        except User.DoesNotExist:
            return Response(
                {"error": "El usuario especificado no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


# ============================================
# VISTA 3: SOLO PARA DETALLE (GET por ID)
# ============================================
class SupervivienteDetailView(APIView):
    """
    Vista SOLO para obtener un superviviente específico (GET por ID)
    """
    
    def get(self, request, pk):
        """Obtener un superviviente por ID - JSON MANUAL"""
        try:
            # Buscar por el id del usuario (porque Superviviente usa usuario como PK)
            superviviente = Superviviente.objects.get(usuario__id=pk)
            
            # Construir respuesta manualmente
            data = {
                'id': superviviente.usuario.id,
                'nombre': superviviente.nombre,
                'apellido': superviviente.apellido,
                'numero_vault': superviviente.numero_vault,
                'nivel': superviviente.nivel,
                'caps': superviviente.caps,
                'salud': superviviente.salud,
                'radiacion': superviviente.radiacion,
                'fecha_creacion': superviviente.fecha_creacion,
                'fecha_actualizacion': superviviente.fecha_actualizacion,
                'esta_sano': superviviente.esta_sano,
                'nombre_mostrado': superviviente.nombre_mostrado,
                'necesita_medicina': superviviente.necesita_medicina,
            }
            
            return Response(data)
            
        except Superviviente.DoesNotExist:
            return Response(
                {"error": "Superviviente no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )


# ============================================
# VISTA 4: SOLO PARA ACTUALIZAR (PUT)
# ============================================
class SupervivienteUpdateView(APIView):
    """
    Vista SOLO para actualizar un superviviente existente (PUT)
    """
    
    def put(self, request, pk):
        """Actualizar un superviviente existente"""
        try:
            superviviente = Superviviente.objects.get(usuario__id=pk)
        except Superviviente.DoesNotExist:
            return Response(
                {"error": "Superviviente no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        data = request.data
        
        # Validación manual
        errores = []
        
        # Validar campos si están presentes
        if 'salud' in data:
            try:
                salud = int(data['salud'])
                if salud < 0 or salud > 100:
                    errores.append("La salud debe estar entre 0 y 100")
                else:
                    superviviente.salud = salud
            except ValueError:
                errores.append("La salud debe ser un número entero")
        
        if 'radiacion' in data:
            try:
                radiacion = int(data['radiacion'])
                if radiacion < 0 or radiacion > 100:
                    errores.append("La radiación debe estar entre 0 y 100")
                else:
                    superviviente.radiacion = radiacion
            except ValueError:
                errores.append("La radiación debe ser un número entero")
        
        if 'nivel' in data:
            try:
                nivel = int(data['nivel'])
                if nivel < 1 or nivel > 50:
                    errores.append("El nivel debe estar entre 1 y 50")
                else:
                    superviviente.nivel = nivel
            except ValueError:
                errores.append("El nivel debe ser un número entero")
        
        # Actualizar otros campos si están presentes
        if 'nombre' in data:
            superviviente.nombre = data['nombre']
        
        if 'apellido' in data:
            superviviente.apellido = data['apellido']
        
        if 'numero_vault' in data:
            superviviente.numero_vault = data['numero_vault']
        
        if 'caps' in data:
            try:
                caps = int(data['caps'])
                superviviente.caps = caps
            except ValueError:
                errores.append("Los caps deben ser un número entero")
        
        # Si hay errores, devolverlos
        if errores:
            return Response(
                {"errores": errores},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Guardar los cambios
        superviviente.save()
        
        # Construir respuesta
        response_data = {
            'id': superviviente.usuario.id,
            'nombre': superviviente.nombre,
            'apellido': superviviente.apellido,
            'numero_vault': superviviente.numero_vault,
            'nivel': superviviente.nivel,
            'caps': superviviente.caps,
            'salud': superviviente.salud,
            'radiacion': superviviente.radiacion,
            'fecha_creacion': superviviente.fecha_creacion,
            'fecha_actualizacion': superviviente.fecha_actualizacion,
            'esta_sano': superviviente.esta_sano,
            'nombre_mostrado': superviviente.nombre_mostrado,
            'necesita_medicina': superviviente.necesita_medicina,
            'mensaje': 'Superviviente actualizado exitosamente'
        }
        
        return Response(response_data)


# ============================================
# VISTA 5: SOLO PARA ELIMINAR (DELETE)
# ============================================
class SupervivienteDeleteView(APIView):
    """
    Vista SOLO para eliminar un superviviente (DELETE)
    """
    
    def delete(self, request, pk):
        """Eliminar un superviviente"""
        try:
            superviviente = Superviviente.objects.get(usuario__id=pk)
        except Superviviente.DoesNotExist:
            return Response(
                {"error": "Superviviente no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Obtener el nombre antes de eliminar para el mensaje
        nombre_mostrado = superviviente.nombre_mostrado
        
        # Eliminar el superviviente
        superviviente.delete()
        
        return Response(
            {"mensaje": f"Superviviente '{nombre_mostrado}' eliminado exitosamente"},
            status=status.HTTP_200_OK
        )