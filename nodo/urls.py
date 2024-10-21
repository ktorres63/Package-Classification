from django.urls import path
from .views import NodoCreateView,NodoListView

urlpatterns = [
    path('api/create/',NodoCreateView.as_view(), name='nodo-create'),
    path('api/list/', NodoListView.as_view(), name='nodo-list'),


]