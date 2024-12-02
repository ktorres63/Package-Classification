from django.urls import path
from .views import *

urlpatterns = [
    path('api/create/', PaqueteCreateView.as_view(), name='paquete-create'),
    path('api/list/', PaqueteListView.as_view(), name='paquete-list'),
    path('api/retrive/<int:id_paquete>/', PaqueteDetailView.as_view(), name='paquete-detail'),
    path('api/track/<int:id_paquete>/', PaqueteUbicacionActualView.as_view(), name='ubicacion_actual_paquete'),
]
