# Generated by Django 4.0.5 on 2022-08-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministracionApp', '0010_sucursales_departamento_suc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursales',
            name='numero_suc',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
