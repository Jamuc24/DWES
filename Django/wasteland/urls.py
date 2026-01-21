# fallout/urls.py
from django.urls import path
from .views import (
    SupervivienteListView,
    SupervivienteCreateView,
    SupervivienteDetailView,
    SupervivienteUpdateView,
    SupervivienteDeleteView
)

urlpatterns = [
    # GET: Listar todos los supervivientes
    path('api/supervivientes/', SupervivienteListView.as_view(), name='superviviente-list'),
    
    # POST: Crear un nuevo superviviente
    path('api/supervivientes/crear/', SupervivienteCreateView.as_view(), name='superviviente-create'),
    
    # GET: Ver un superviviente específico
    path('api/supervivientes/<int:pk>/', SupervivienteDetailView.as_view(), name='superviviente-detail'),
    
    # PUT: Actualizar un superviviente específico
    path('api/supervivientes/<int:pk>/actualizar/', SupervivienteUpdateView.as_view(), name='superviviente-update'),
    
    # DELETE: Eliminar un superviviente específico
    path('api/supervivientes/<int:pk>/eliminar/', SupervivienteDeleteView.as_view(), name='superviviente-delete'),
]