# Generated by Django 4.0.3 on 2022-07-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormulariosApp', '0003_rename_cantidad_bolsa_chica_pedidobolsas_bolsa chica_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Banda elastica',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Carpeta',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Cinta ancha transp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Cinta fina 1.25',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Cinta fina 2.5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Cinta impresa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Clips',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Etiqueta 60X150',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Etiqueta 60X40',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Etiqueta color',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Goma',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Grapadora',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Grapas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Hilos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Lapicera mostrador',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Lapiceras',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Lapiz',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Marcador fluor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Marcador perm Fino',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Marcador perm Grueso',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Medias',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='PilasAA',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='PilasAAA',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Pistola',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Precinto cajon',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Precinto sobre',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Resma A4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Resma otro',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Ribbon',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Rollo calculadora',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Rollo facturacion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Sobre carta',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Tijera',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Tinta calculadora',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Tinta sello',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidopapeleria',
            name='Trincheta',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
