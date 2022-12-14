# Generated by Django 4.0.5 on 2022-08-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmCajasApp', '0005_rename_fecha_registro_registroquebranto_fecha_registro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresPromotora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('fecha_registro', models.DateField(auto_now=True)),
                ('num_orden', models.IntegerField()),
                ('fecha_orden', models.DateField()),
                ('importe', models.IntegerField()),
                ('plan', models.CharField(max_length=5)),
                ('promo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PresRetop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('fecha_registro', models.DateField(auto_now=True)),
                ('num_comercio', models.IntegerField()),
                ('fecha_orden', models.DateField()),
                ('importe', models.IntegerField()),
                ('plan', models.CharField(max_length=5)),
            ],
        ),
    ]
