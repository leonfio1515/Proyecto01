# Generated by Django 4.0.3 on 2022-08-10 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormulariosApp', '0012_alter_descuentos_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuentos',
            name='valor_descuento',
            field=models.CharField(max_length=5),
        ),
    ]
