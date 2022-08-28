# Generated by Django 4.0.3 on 2022-07-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticulosApp', '0006_alter_reparaciones_nombre_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='reparaciones',
            name='email_contacto',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='reparaciones',
            name='nombre_empresa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reparaciones',
            name='tel_contacto',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]