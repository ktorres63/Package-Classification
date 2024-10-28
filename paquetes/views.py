from rest_framework import generics
from .models import Paquete
from .serializers import PaqueteSerializer

class PaqueteCreateView(generics.CreateAPIView):
    queryset = Paquete.objects.all()
    serializer_class = PaqueteSerializer

class PaqueteListView(generics.ListAPIView):
    queryset = Paquete.objects.all()
    serializer_class = PaqueteSerializer