# Generated by Django 4.0.3 on 2022-07-26 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelacioncliente',
            name='usuario',
            field=models.CharField(max_length=20),
        ),
    ]
