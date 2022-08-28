# Generated by Django 4.0.3 on 2022-07-24 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormulariosApp', '0005_rename_dicroica led_pedidoluces_dicroica_led_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidobolsas',
            old_name='Bolsa chica',
            new_name='Bolsa_chica',
        ),
        migrations.RenameField(
            model_name='pedidobolsas',
            old_name='Bolsa grande',
            new_name='Bolsa_grande',
        ),
        migrations.RenameField(
            model_name='pedidobolsas',
            old_name='Bolsa media',
            new_name='Bolsa_media',
        ),
        migrations.RenameField(
            model_name='pedidobolsas',
            old_name='Fecha pedido',
            new_name='Fecha_pedido',
        ),
        migrations.RenameField(
            model_name='pedidodiseno',
            old_name='Fecha pedido',
            new_name='Fecha_pedido',
        ),
        migrations.RenameField(
            model_name='pedidodiseno',
            old_name='Talon cambio',
            new_name='Talon_cambio',
        ),
        migrations.RenameField(
            model_name='pedidodiseno',
            old_name='Tarjeta At cliente',
            new_name='Tarjeta_atencion',
        ),
        migrations.RenameField(
            model_name='pedidodiseno',
            old_name='Tarjeta presentacion',
            new_name='Tarjeta_presentacion',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='Agua oxigenada',
            new_name='Agua_oxigenada',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='Alcohol gel',
            new_name='Alcohol_gel',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='Alcohol rectificado',
            new_name='Alcohol_rectificado',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='Fecha pedido',
            new_name='Fecha_pedido',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='Cera incolora',
            new_name='Cera_incolora',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='Cera roja',
            new_name='Cera_roja',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='Desodorante ambiente',
            new_name='Des_ambiente',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='Fecha pedido',
            new_name='Fecha_pedido',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='Jabon liquido',
            new_name='Jabon_liq',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='Limpia vidrio',
            new_name='Limpia_vidrio',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='Paño piso',
            new_name='Panos_piso',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='Pulidor cremoso',
            new_name='Pulidor_cremoso',
        ),
        migrations.RenameField(
            model_name='pedidoluces',
            old_name='fecha_pedido_luces',
            new_name='Fecha_pedido',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Banda elastica',
            new_name='Banda_elastica',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Cinta ancha transp',
            new_name='Cinta_anchaT',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Cinta fina 1.25',
            new_name='Cinta_fina_1',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Cinta fina 2.5',
            new_name='Cinta_fina_2',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Cinta impresa',
            new_name='Cinta_impresa',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Etiqueta 60X150',
            new_name='Etiqueta_60X150',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Etiqueta 60X40',
            new_name='Etiqueta_60X40',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Etiqueta color',
            new_name='Etiqueta_color',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Fecha pedido',
            new_name='Fecha_pedido',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Lapicera mostrador',
            new_name='Lapicera_mostrador',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Marcador fluor',
            new_name='Marcador_fluor',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Marcador perm Fino',
            new_name='Marcador_perm_fino',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Marcador perm Grueso',
            new_name='Marcador_perm_grueso',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Precinto cajon',
            new_name='Precinto_cajon',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Precinto sobre',
            new_name='Precinto_sobre',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Resma A4',
            new_name='ResmaA4',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Resma otro',
            new_name='Resma_otro',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Rollo calculadora',
            new_name='Rollo_calc',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Rollo facturacion',
            new_name='Rollo_fact',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Sobre carta',
            new_name='Sobre_carta',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Tinta calculadora',
            new_name='Tinta_calc',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='Tinta sello',
            new_name='Tinta_sello',
        ),
    ]
