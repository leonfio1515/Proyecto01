# Generated by Django 4.0.3 on 2022-07-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArticulosApp', '0004_alter_luces_nombre_luces'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reparaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=50)),
            ],
        ),
    ]
