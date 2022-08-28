# Generated by Django 4.0.3 on 2022-07-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticulosApp', '0005_reparaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparaciones',
            name='nombre_servicio',
            field=models.CharField(choices=[('Aire acondicionado', 'Aire acondicionado'), ('Sanitario', 'Sanitario'), ('Electricidad', 'Electricidad'), ('Vidriero', 'Vidriero'), ('Albañileria', 'Albañileria')], max_length=50),
        ),
    ]
