# Generated by Django 4.0.5 on 2022-08-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormulariosApp', '0017_pedidocambio_fecha_enviado'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoUniforme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('fecha_pedido', models.DateField(auto_now=True)),
                ('num_fun', models.IntegerField()),
                ('ci_fun', models.IntegerField()),
                ('talle_camisa', models.CharField(max_length=20)),
                ('talle_pantalon', models.CharField(max_length=20)),
                ('talle_abrigo', models.CharField(max_length=20)),
                ('area_trabajo', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=20)),
            ],
        ),
    ]
