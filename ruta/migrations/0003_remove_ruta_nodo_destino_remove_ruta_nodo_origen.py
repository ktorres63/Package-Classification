# Generated by Django 5.1.2 on 2024-10-20 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0002_remove_ruta_destino_remove_ruta_distancia_km_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='nodo_destino',
        ),
        migrations.RemoveField(
            model_name='ruta',
            name='nodo_origen',
        ),
    ]
