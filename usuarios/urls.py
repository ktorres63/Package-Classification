from django.urls import path
from .views import UsuarioCreateView, UsuarioListView

urlpatterns = [
    path('api/create/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('api/list/', UsuarioListView.as_view(), name='usuario-list'),

]