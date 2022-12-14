# Generated by Django 4.0.3 on 2022-07-24 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormulariosApp', '0002_pedidopapeleria_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedidobolsas',
            old_name='cantidad_bolsa_chica',
            new_name='Bolsa chica',
        ),
        migrations.RenameField(
            model_name='pedidobolsas',
            old_name='cantidad_bolsa_grande',
            new_name='Bolsa grande',
        ),
        migrations.RenameField(
            model_name='pedidobolsas',
            old_name='cantidad_bolsa_media',
            new_name='Bolsa media',
        ),
        migrations.RenameField(
            model_name='pedidobolsas',
            old_name='fecha_pedido_bolsas',
            new_name='Fecha pedido',
        ),
        migrations.RenameField(
            model_name='pedidodiseno',
            old_name='fecha_pedido_diseno',
            new_name='Fecha pedido',
        ),
        migrations.RenameField(
            model_name='pedidodiseno',
            old_name='cantidad_talon_cambio',
            new_name='Talon cambio',
        ),
        migrations.RenameField(
            model_name='pedidodiseno',
            old_name='cantidad_tarj_atencion',
            new_name='Tarjeta At cliente',
        ),
        migrations.RenameField(
            model_name='pedidodiseno',
            old_name='cantidad_tarj_presentacion',
            new_name='Tarjeta presentacion',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='cantidad_agua_oxigenada',
            new_name='Agua oxigenada',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='cantidad_alcohol_gel',
            new_name='Alcohol gel',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='cantidad_alcohol_rectificado',
            new_name='Alcohol rectificado',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='cantidad_algodon',
            new_name='Algodon',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='cantidad_curitas',
            new_name='Curitas',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='cantidad_disan',
            new_name='Disan',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='fecha_pedido_farmacia',
            new_name='Fecha pedido',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='cantidad_gasa',
            new_name='Gasa',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='cantidad_iodofon',
            new_name='Ibuprofeno',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='cantidad_ibuprofeno',
            new_name='Iodofon',
        ),
        migrations.RenameField(
            model_name='pedidofarmacia',
            old_name='cantidad_leuco',
            new_name='Leuco',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_bolsas',
            new_name='Bolsas',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_cera_inc',
            new_name='Cera incolora',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_cera_roja',
            new_name='Cera roja',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_des_ambiente',
            new_name='Desodorante ambiente',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_detergente',
            new_name='Detergente',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_esponja',
            new_name='Esponja',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='fecha_pedido_limpieza',
            new_name='Fecha pedido',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_franela',
            new_name='Franela',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_hipoclorito',
            new_name='Hipoclorito',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_insecticida',
            new_name='Insecticida',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_jabon_liq',
            new_name='Jabon liquido',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_limpia_vidrio',
            new_name='Limpia vidrio',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_lustramueble',
            new_name='Lustramueble',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_panos_piso',
            new_name='PH',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_perfumol',
            new_name='Pa??o piso',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_ph',
            new_name='Perfumol',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_plumero',
            new_name='Plumero',
        ),
        migrations.RenameField(
            model_name='pedidolimpieza',
            old_name='cantidad_pulidor_cremoso',
            new_name='Pulidor cremoso',
        ),
        migrations.RenameField(
            model_name='pedidoluces',
            old_name='cantidad_ar111',
            new_name='AR111',
        ),
        migrations.RenameField(
            model_name='pedidoluces',
            old_name='cantidad_driver',
            new_name='Driver',
        ),
        migrations.RenameField(
            model_name='pedidoluces',
            old_name='cantidad_emb',
            new_name='EMB',
        ),
        migrations.RenameField(
            model_name='pedidoluces',
            old_name='fecha_pedido_precios',
            new_name='Fecha pedido',
        ),
        migrations.RenameField(
            model_name='pedidoluces',
            old_name='cantidad_lampara',
            new_name='Lampara',
        ),
        migrations.RenameField(
            model_name='pedidoluces',
            old_name='cantidad_par30_calida',
            new_name='Par30 - calida',
        ),
        migrations.RenameField(
            model_name='pedidoluces',
            old_name='cantidad_par30_fria',
            new_name='Par30 - fria',
        ),
        migrations.RenameField(
            model_name='pedidoluces',
            old_name='cantidad_tacho',
            new_name='Tacho',
        ),
        migrations.RenameField(
            model_name='pedidoluces',
            old_name='cantidad_tubo_led',
            new_name='Tubo led',
        ),
        migrations.RenameField(
            model_name='pedidopapeleria',
            old_name='fecha_pedido_papeleria',
            new_name='Fecha pedido',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='Pilas AAA',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_cinta_anchaT',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_cinta_fina1',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_cinta_fina2',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_cinta_impresa',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_clips',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_etiqueta_60x40',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_grapas',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_lapiceras',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_lapiceras_mostra',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_lapiz',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_marcador_fluor',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_marcador_perm_fino',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_medias',
        ),
        migrations.RemoveField(
            model_name='pedidopapeleria',
            name='cantidad_pilasAA',
        ),
    ]
