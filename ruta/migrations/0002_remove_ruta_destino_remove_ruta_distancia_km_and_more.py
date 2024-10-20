# Generated by Django 5.1.2 on 2024-10-20 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodo', '0001_initial'),
        ('paquetes', '0001_initial'),
        ('ruta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='destino',
        ),
        migrations.RemoveField(
            model_name='ruta',
            name='distancia_km',
        ),
        migrations.RemoveField(
            model_name='ruta',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='ruta',
            name='origen',
        ),
        migrations.RemoveField(
            model_name='ruta',
            name='tiempo_estimado_horas',
        ),
        migrations.AddField(
            model_name='ruta',
            name='nodo_destino',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rutas_destino', to='nodo.nodo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ruta',
            name='nodo_origen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rutas_origen', to='nodo.nodo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ruta',
            name='paquete',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='paquetes.paquete'),
            preserve_default=False,
        ),
    ]