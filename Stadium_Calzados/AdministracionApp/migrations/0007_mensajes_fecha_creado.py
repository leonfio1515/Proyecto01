# Generated by Django 4.0.5 on 2022-08-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministracionApp', '0006_mensajes_respuesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajes',
            name='fecha_creado',
            field=models.DateField(auto_now=True, verbose_name='Fecha creado'),
        ),
    ]
