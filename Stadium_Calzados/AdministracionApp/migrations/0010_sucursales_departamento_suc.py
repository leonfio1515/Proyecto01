# Generated by Django 4.0.5 on 2022-08-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministracionApp', '0009_sucursales'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursales',
            name='departamento_suc',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]