# Generated by Django 4.0.5 on 2022-08-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormulariosApp', '0018_pedidouniforme'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidouniforme',
            name='fecha_enviado',
            field=models.DateField(blank=True, null=True),
        ),
    ]
