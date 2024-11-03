# en urls.py
from django.urls import path
from .views import RutaUpdateEstadoView

urlpatterns = [
    path('api/<int:id>/', RutaUpdateEstadoView.as_view(), name='ruta-update-estado'),
]
