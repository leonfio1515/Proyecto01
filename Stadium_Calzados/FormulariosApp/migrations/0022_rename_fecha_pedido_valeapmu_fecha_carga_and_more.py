# Generated by Django 4.0.5 on 2022-08-27 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormulariosApp', '0021_valeapmu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='valeapmu',
            old_name='fecha_pedido',
            new_name='fecha_carga',
        ),
        migrations.RenameField(
            model_name='valeconrad',
            old_name='fecha_pedido',
            new_name='fecha_carga',
        ),
    ]
