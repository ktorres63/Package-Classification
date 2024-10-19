from django.db import models

# Create your models here.
class Usuario(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)