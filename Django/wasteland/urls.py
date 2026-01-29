# wasteland/urls.py - VERSIÓN BLOQUE 3 (ViewSets + Routers)
from django.urls import path, include
from .routers import router  # Importamos el router que creaste

urlpatterns = [
    # ¡SOLO ESTA LÍNEA REEMPLAZA TODAS LAS ANTERIORES!
    # Incluye TODAS las rutas generadas automáticamente por el router
    path('api/', include(router.urls)),
]