# Generated by Django 5.1.2 on 2024-11-09 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodo', '0002_nodo_alias'),
        ('ruta', '0007_alter_ruta_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruta',
            name='tiempo',
        ),
        migrations.AddField(
            model_name='ruta',
            name='duracion',
            field=models.FloatField(default=1, help_text='Tiempo estimado en minutos u horas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ruta',
            name='estado',
            field=models.IntegerField(choices=[(0, 'No trabajado'), (1, 'Recibido'), (2, 'En tránsito'), (3, 'Entregado'), (4, 'Entregado al cliente')], default=0),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='nodo_fin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutas_fin', to='nodo.nodo'),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='nodo_inicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutas_inicio', to='nodo.nodo'),
        ),
    ]
