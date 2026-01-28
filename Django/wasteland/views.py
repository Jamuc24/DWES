# fallout/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Superviviente
from .serializers import SupervivienteSerializer
from .models import Objeto  
from .serializers import ObjetoSerializer 

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
        
        #Serializador propio de la vista
        serializer = SupervivienteSerializer(supervivientes, many=True)
        
        return Response(serializer.data)

# ============================================
# VISTA 2: SOLO PARA CREAR (POST)
# ============================================
class SupervivienteCreateView(APIView):
    """
    Vista SOLO para crear un nuevo superviviente (POST)
    """
    
    def post(self, request):
        """Crear un nuevo superviviente - CON SERIALIZADOR"""
        serializer = SupervivienteSerializer(data=request.data)
        
        if serializer.is_valid():
        
            superviviente = serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
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
        """Obtener un superviviente por ID - CON SERIALIZADOR"""
        try:
            superviviente = Superviviente.objects.get(usuario__id=pk)
            
            # ¡Solo 1 línea con serializador!
            serializer = SupervivienteSerializer(superviviente)  # SIN many=True
            
            return Response(serializer.data)
            
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
    
# ============================================
# VISTA 6: HECHA PARA LOS OBJETOS
# ============================================

class ObjetoListView(APIView):
    """ Vista para listar objetos (prueba del segundo serializador)"""
    
    def get(self, request):
        objetos = Objeto.objects.all()
        serializer = ObjetoSerializer(objetos, many=True)
        return Response(serializer.data)