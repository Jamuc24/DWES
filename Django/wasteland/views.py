# Herramientas que importamos
from rest_framework.viewsets import ModelViewSet
from .models import Superviviente, Objeto
from .serializers import SupervivienteSerializer, ObjetoSerializer

class SupervivienteViewSet(ModelViewSet):
    """
    ¡Esta sola clase hace TODAS estas cosas automáticamente!
    - GET /api/supervivientes/       → Lista todos
    - POST /api/supervivientes/      → Crea uno nuevo
    - GET /api/supervivientes/1/     → Muestra el #1
    - PUT /api/supervivientes/1/     → Actualiza completamente el #1
    - PATCH /api/supervivientes/1/   → Actualiza parcialmente el #1
    - DELETE /api/supervivientes/1/  → Elimina el #1
    """
    queryset = Superviviente.objects.all() 
    serializer_class = SupervivienteSerializer 

class ObjetoViewSet(ModelViewSet):
    """
    Lo mismo pero para Objetos (armas, armaduras, etc.)
    """
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer