# Generated by Django 4.0.5 on 2022-07-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manuales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manual', models.FileField(upload_to='media/')),
                ('nombre_manual', models.CharField(max_length=50)),

            ],
        ),
    ]
