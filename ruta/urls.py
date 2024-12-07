# en urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/<int:id_paquete>/<int:id_nodo_inicio>/', ObtenerRutaPorPaqueteYNodo.as_view(), name='ruta_por_paquete_y_nodo'),
    path('api/<int:id_paquete>/<int:id_nodo_inicio>/', ActualizarEstadoRuta.as_view(), name='actualizar_estado_ruta'),
    path('api/<int:id_ruta>', ActualizarEstadoPorRutaId.as_view(), name='actualizar-estado-por-ruta-id'),
    path('api/get/last-route/<int:id_paquete>',ObtenerUltimaRutaPorPaquete.as_view(), name='obtener-ultima-ruta'),

    path('api/list/', RutaListView.as_view(), name='ruta-list'),

]
