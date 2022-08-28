# Generated by Django 4.0.7 on 2022-08-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormulariosApp', '0013_alter_descuentos_valor_descuento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuentos',
            name='fecha_creado',
            field=models.DateField(auto_now=True, verbose_name='Fecha_creado'),
        ),
        migrations.AlterField(
            model_name='pedidoreparaciones',
            name='Servicio',
            field=models.TextField(blank=True, choices=[('Aire acondicionado', 'Aire acondicionado'), ('Sanitario', 'Sanitario'), ('Electricidad', 'Electricidad'), ('Vidriero', 'Vidriero'), ('Albañileria', 'Albañileria')], max_length=200, null=True),
        ),
    ]
