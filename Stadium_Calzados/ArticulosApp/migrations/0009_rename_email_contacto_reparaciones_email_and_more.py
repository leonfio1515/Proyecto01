# Generated by Django 4.0.3 on 2022-07-24 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArticulosApp', '0008_alter_reparaciones_tel_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reparaciones',
            old_name='email_contacto',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='reparaciones',
            old_name='nombre_empresa',
            new_name='Empresa',
        ),
        migrations.RenameField(
            model_name='reparaciones',
            old_name='tel_contacto',
            new_name='Telefono',
        ),
    ]