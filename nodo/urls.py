from django.urls import path
from .views import NodoCreateView,NodoListView

urlpatterns = [
    path('api/list/', NodoListView.as_view(), name='nodo-list'),
]