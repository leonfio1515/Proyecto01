# Generated by Django 4.0.5 on 2022-08-27 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormulariosApp', '0023_chequeuniforme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chequeuniforme',
            old_name='comentario',
            new_name='comentarios',
        ),
    ]