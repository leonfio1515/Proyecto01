# Generated by Django 4.0.5 on 2022-08-28 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdmConveniosApp', '0004_alter_cobranzasconvenios_imp_bonificacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobranzasconvenios',
            name='sap_convenios',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]