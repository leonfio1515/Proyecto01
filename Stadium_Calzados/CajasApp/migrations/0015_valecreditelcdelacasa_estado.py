# Generated by Django 4.0.5 on 2022-08-28 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CajasApp', '0014_valecreditelcdelacasa_num_cajera_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='valecreditelcdelacasa',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
