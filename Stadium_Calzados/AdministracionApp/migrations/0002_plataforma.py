# Generated by Django 4.0.5 on 2022-07-26 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministracionApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plataforma', models.CharField(choices=[('Stadium', 'Stadium'), ('Peppos', 'Peppos'), ('MissCarol', 'MissCarol'), ('Clarks', 'Clarks')], max_length=50)),
            ],
        ),
    ]