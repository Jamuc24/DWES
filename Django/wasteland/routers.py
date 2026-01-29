
from rest_framework.routers import DefaultRouter
from .views import SupervivienteViewSet, ObjetoViewSet

router = DefaultRouter()


router.register(r'supervivientes', SupervivienteViewSet, basename='superviviente')
router.register(r'objetos', ObjetoViewSet, basename='objeto')
