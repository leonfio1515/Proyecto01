# Generated by Django 4.0.5 on 2022-08-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmCajasApp', '0003_errores_alter_registroquebranto_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errores',
            name='comentario',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='errores',
            name='grupo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]