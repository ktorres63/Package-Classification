from django.urls import path
from .views import UsuarioCreateView

urlpatterns = [
    path('api/create/', UsuarioCreateView.as_view(), name='usuario-create'),
]