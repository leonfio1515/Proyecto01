# Generated by Django 4.0.3 on 2022-07-27 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CobranzasConv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Numero', models.IntegerField()),
                ('Importe_resumen', models.IntegerField()),
                ('Mes_resumen', models.CharField(max_length=50)),
                ('Bonificacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmpresasConvenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Numero', models.IntegerField()),
                ('Codigo_SAP', models.CharField(max_length=50)),
                ('Fecha_corte', models.IntegerField()),
                ('Bonificacion', models.ImageField(upload_to='')),
                ('Medio_pago', models.CharField(choices=[('Itau', 'Itau'), ('Brou', 'Brou'), ('Santander', 'Santander'), ('Scotiabank', 'Scotiabank'), ('Cheque', 'Cheque'), ('Efectivo', 'Efectivo')], max_length=50)),
            ],
        ),
    ]
