# Generated by Django 4.0.3 on 2022-07-26 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelacionCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Nombre', models.CharField(max_length=50)),
                ('CI', models.IntegerField()),
                ('Plataforma', models.CharField(max_length=50)),
                ('Medio_pago', models.CharField(max_length=50)),
                ('Pedido', models.IntegerField()),
                ('Fecha_cancela', models.DateField()),
                ('Fecha_recibido', models.DateField()),
                ('Importe', models.IntegerField()),
                ('Motivo', models.CharField(max_length=50)),
                ('Comentario', models.TextField(max_length=200)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
