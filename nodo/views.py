from django.shortcuts import render
from rest_framework import generics
from .models import Nodo
from .serializers import NodoSerializer

class NodoCreateView(generics.CreateAPIView):
    queryset = Nodo.objects.all()
    serializer_class = NodoSerializer

class NodoListView(generics.ListAPIView):
    queryset = Nodo.objects.all()
    serializer_class = NodoSerializer