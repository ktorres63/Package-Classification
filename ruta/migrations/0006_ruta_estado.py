# Generated by Django 5.1.2 on 2024-10-26 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0005_ruta_tiempo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='estado',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
