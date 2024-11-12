# en urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('api/<int:id_paquete>/<int:id_nodo_inicio>/', ActualizarEstadoRuta.as_view(), name='actualizar_estado_ruta'),
    path('api/list/', RutaListView.as_view(), name='ruta-list'),

]
