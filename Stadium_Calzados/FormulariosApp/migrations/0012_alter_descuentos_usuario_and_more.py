# Generated by Django 4.0.3 on 2022-08-10 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FormulariosApp', '0011_remove_pedidobolsas_fecha_creado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuentos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pedidobolsas',
            name='Fecha_pedido',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidodiseno',
            name='Fecha_pedido',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidofarmacia',
            name='Fecha_pedido',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidolimpieza',
            name='Fecha_pedido',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidoluces',
            name='Fecha_pedido',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidopapeleria',
            name='Fecha_pedido',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidoreparaciones',
            name='Fecha_pedido',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
