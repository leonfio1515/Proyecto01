# Generated by Django 4.0.3 on 2022-07-24 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticulosApp', '0003_bolsas_medida_bolsas_diseno_medida_diseno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luces',
            name='nombre_luces',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
