# Generated by Django 4.0.3 on 2022-07-27 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroQuebranto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('Fecha_registro', models.DateField()),
                ('Num_Cajera', models.CharField(max_length=20)),
                ('Nombre_Cajera', models.CharField(max_length=20)),
                ('Fecha_faltante', models.DateField()),
                ('Faltante', models.IntegerField()),
                ('Comentario', models.CharField(max_length=200)),
            ],
        ),
    ]
