from django.urls import path
from .views import PaqueteListView, PaqueteCreateView

urlpatterns = [
    path('api/create', PaqueteCreateView.as_view(), name='paquete-create'),
    path('api/list/', PaqueteListView.as_view(), name='paquete-list'),

]
