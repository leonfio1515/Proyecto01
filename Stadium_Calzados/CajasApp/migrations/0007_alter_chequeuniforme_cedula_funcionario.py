# Generated by Django 4.0.3 on 2022-07-21 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FuncionariosApp', '0002_rename_apellido_fun_funcionarios_apellido_funcionario_and_more'),
        ('CajasApp', '0006_alter_chequeuniforme_cedula_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chequeuniforme',
            name='cedula_funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FuncionariosApp.funcionarios'),
        ),
    ]
