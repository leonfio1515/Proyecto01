from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from rangefilter.filter import DateRangeFilter

# Register your models here.
admin.site.site_header="Administrador"

class DescuentosAdmin(admin.ModelAdmin):
   list_display = (
       "usuario",
       "fecha_creado",
       "valor_descuento",
       "fecha_descuento",
       "nombre_descuento",
   )

   search_fields = (
       "usuario",
       "fecha_creado",
       "valor_descuento",
       "fecha_descuento",
       "nombre_descuento",
   )
   list_per_page = 10
   exclude = ("usuario", "fecha_creado","valor_descuento","fecha_descuento","nombre_descuento")


class PedidoLucesResource(resources.ModelResource):
    class Meta:
        model=PedidoLuces

class PedidoLucesAdmin(ImportExportActionModelAdmin):
    resource_class = PedidoLucesResource
    list_display = (
       "usuario",
       "Fecha_pedido",
       "Fecha_enviado",
       "AR111",
       "Dicroica_led",
       "Driver",
       "EMB",
       "Lampara",
       "Par30_fria",
       "Par30_calida",
       "Tacho",
       "Tubo_led",

   )
    search_fields = (
        "usuario",
        "Fecha_pedido",
        "AR111",
        "Dicroica_led",
        "Driver",
        "EMB",
        "Lampara",
        "Par30_fria",
        "Par30_calida",
        "Tacho",
        "Tubo_led",
    )
    list_editable = ("Fecha_enviado",)
    list_per_page = 10
    exclude = ("usuario", "Fecha_pedido")
    list_filter = (("Fecha_pedido", DateRangeFilter),)


class PedidoBolsasResource(resources.ModelResource):
    class Meta:
        model=PedidoBolsas

class PedidoBolsasAdmin(ImportExportActionModelAdmin):
    list_display = (
        "usuario",
        "Fecha_pedido",
        "Fecha_enviado",
        "Bolsa_chica",
        "Bolsa_media",
        "Bolsa_grande",
    )

    search_fields = (
        "usuario",
        "Fecha_pedido",
        "Bolsa_chica",
        "Bolsa_media",
        "Bolsa_grande",
    )
    list_editable = ("Fecha_enviado",)
    list_per_page = 10
    exclude = ("usuario", "Fecha_pedido")
    list_filter = (("Fecha_pedido", DateRangeFilter),)


class PedidoFarmaciaResource(resources.ModelResource):
    class Meta:
        model=PedidoFarmacia

class PedidoFarmaciaAdmin(ImportExportActionModelAdmin):
    list_display = (
        "usuario",
        "Fecha_pedido",
        "Fecha_enviado",
        "Ibuprofeno",
        "Leuco",
        "Iodofon",
        "Gasa",
        "Disan",
        "Curitas",
        "Algodon",
        "Alcohol_rectificado",
        "Alcohol_gel",
        "Agua_oxigenada",
    )

    search_fields = (
        "usuario",
        "Fecha_pedido",
        "Ibuprofeno",
        "Leuco",
        "Iodofon",
        "Gasa",
        "Disan",
        "Curitas",
        "Algodon",
        "Alcohol_rectificado",
        "Alcohol_gel",
        "Agua_oxigenada",
    )
    list_editable = ("Fecha_enviado",)
    list_per_page = 10
    exclude = ("usuario", "Fecha_pedido")
    list_filter = (("Fecha_pedido", DateRangeFilter),)


class PedidoPapeleriaResource(resources.ModelResource):
    class Meta:
        model=PedidoPapeleria

class PedidoPapeleriaAdmin(ImportExportActionModelAdmin):
    list_display = (
        "usuario",
        "Fecha_pedido",
        "Fecha_enviado",
        "Lapiceras",
        "Clips",
        "Lapiz",
        "Lapicera_mostrador",
        "Cinta_fina_1",
        "Cinta_fina_2",
        "Cinta_anchaT",
        "Cinta_impresa",
        "Etiqueta_60X40",
        "Marcador_perm_fino",
        "Marcador_fluor",
        "Medias",
        "Grapas",
        "PilasAA",
        "PilasAAA",
        "Precinto_cajon",
        "Precinto_sobre",
        "ResmaA4",
        "Resma_otro",
        "Ribbon",
        "Rollo_calc",
        "Rollo_fact",
        "Sobre_carta",
        "Tinta_calc",
        "Hilos",
        "Pistola",
        "Trincheta",
        "Tijera",
        "Etiqueta_60X150",
        "Goma",
        "Banda_elastica",
        "Marcador_perm_grueso",
        "Carpeta",
        "Tinta_sello",
        "Grapadora",
        "Etiqueta_color",
    )

    search_fields = (
        "usuario",
        "Fecha_pedido",
        "Lapiceras",
        "Clips",
        "Lapiz",
        "Lapicera_mostrador",
        "Cinta_fina_1",
        "Cinta_fina_2",
        "Cinta_anchaT",
        "Cinta_impresa",
        "Etiqueta_60X40",
        "Marcador_perm_fino",
        "Marcador_fluor",
        "Medias",
        "Grapas",
        "PilasAA",
        "PilasAAA",
        "Precinto_cajon",
        "Precinto_sobre",
        "ResmaA4",
        "Resma_otro",
        "Ribbon",
        "Rollo_calc",
        "Rollo_fact",
        "Sobre_carta",
        "Tinta_calc",
        "Hilos",
        "Pistola",
        "Trincheta",
        "Tijera",
        "Etiqueta_60X150",
        "Goma",
        "Banda_elastica",
        "Marcador_perm_grueso",
        "Carpeta",
        "Tinta_sello",
        "Grapadora",
        "Etiqueta_color",
    )
    list_editable = ("Fecha_enviado",)
    list_per_page = 10
    exclude = ("usuario", "Fecha_pedido")
    list_filter = (("Fecha_pedido", DateRangeFilter),)


class PedidoLimpiezaResource(resources.ModelResource):
    class Meta:
        model=PedidoLimpieza

class PedidoLimpiezaAdmin(ImportExportActionModelAdmin):
    list_display = (
        "usuario",
        "Fecha_pedido",
        "Fecha_enviado",
        "Plumero",
        "Insecticida",
        "Pulidor_cremoso",
        "Perfumol",
        "PH",
        "Panos_piso",
        "Limpia_vidrio",
        "Hipoclorito",
        "Jabon_liq",
        "Franela",
        "Esponja",
        "Detergente",
        "Cera_roja",
        "Cera_incolora",
        "Bolsas",
        "Lustramueble",
        "Des_ambiente",

    )

    search_fields = (
        "usuario",
        "Fecha_pedido",
        "Plumero",
        "Insecticida",
        "Pulidor_cremoso",
        "Perfumol",
        "PH",
        "Panos_piso",
        "Limpia_vidrio",
        "Hipoclorito",
        "Jabon_liq",
        "Franela",
        "Esponja",
        "Detergente",
        "Cera_roja",
        "Cera_incolora",
        "Bolsas",
        "Lustramueble",
        "Des_ambiente",

    )
    list_editable = ("Fecha_enviado",)
    list_per_page = 10
    exclude = ("usuario", "Fecha_pedido")
    list_filter = (("Fecha_pedido", DateRangeFilter),)


class PedidoDisenoResource(resources.ModelResource):
    class Meta:
        model=PedidoDiseno

class PedidoDisenoAdmin(ImportExportActionModelAdmin):
    list_display = (
        "usuario",
        "Fecha_pedido",
        "Fecha_enviado",
        "Tarjeta_presentacion",
        "Tarjeta_atencion",
        "Talon_cambio",
    )

    search_fields = (
        "usuario",
        "Fecha_pedido",
        "Tarjeta_presentacion",
        "Tarjeta_atencion",
        "Talon_cambio",
    )
    list_editable = ("Fecha_enviado",)
    list_per_page = 10
    exclude = ("usuario", "Fecha_pedido")
    list_filter = (("Fecha_pedido", DateRangeFilter),)


class PedidoReparacionesResource(resources.ModelResource):
    class Meta:
        model=PedidoReparaciones

class PedidoReparacionesAdmin(ImportExportActionModelAdmin):
    list_display = (
        "usuario",
        "Fecha_pedido",
        "Servicio",
        "Asunto",
        "Estado",
        "Fecha_resuelto",
        "Comentario_resuelto",
    )

    search_fields = (
        "usuario",
        "Fecha_pedido",
        "Servicio",
        "Asunto",
        "Estado",
        "Fecha_resuelto",
        "Comentario_resuelto",
    )
    list_editable = ("Fecha_resuelto",)
    list_per_page = 10
    exclude = ("usuario","Fecha_pedido")
    list_filter = (("Fecha_pedido", DateRangeFilter),)

class PedidoCambioAdmin(ImportExportActionModelAdmin):
    list_display = (
        "usuario",
        "fecha_pedido",
        "fecha_enviado",
        "monedas_1",
        "monedas_2",
        "monedas_5",
        "monedas_10",
        "billetes_20",
        "billetes_50",
        "billetes_100",
        "billetes_200",
    )

    search_fields = (
        "usuario",
        "fecha_pedido",
        "fecha_enviado",
        "monedas_1",
        "monedas_2",
        "monedas_5",
        "monedas_10",
        "billetes_20",
        "billetes_50",
        "billetes_100",
        "billetes_200",
    )
    list_editable = ("fecha_enviado",)
    list_per_page = 10
    exclude = ("usuario","fecha_pedido",)
    list_filter = (("Fecha_pedido", DateRangeFilter),)

class PedidoUniformeAdmin(ImportExportActionModelAdmin):
    list_display = (
        "usuario",
        "fecha_pedido",
        "fecha_enviado",
        "num_fun",
        "ci_fun",
        "sexo",
        "area_trabajo",
        "talle_camisa",
        "talle_pantalon",
        "talle_abrigo",
    )

    search_fields = (
        "usuario",
        "fecha_pedido",
        "fecha_enviado",
        "num_fun",
        "ci_fun",
        "sexo",
        "area_trabajo",
        "talle_camisa",
        "talle_pantalon",
        "talle_abrigo",
    )
    list_editable = ("fecha_enviado",)
    list_per_page = 10
    exclude = ("usuario","fecha_pedido",)
    list_filter = (("Fecha_pedido", DateRangeFilter),)

class ChequeUniformeAdmin(ImportExportActionModelAdmin):
    list_display = (
        "usuario",
        "fecha_registro",
        "estado_autorizacion",
        "fecha_resolucion",
        "ci_fun",
        "num_fun",
        "nombre_fun",
        "cargo_fun",
        "articulo",
        "comentarios",
    )

    search_fields = (
        "usuario",
        "fecha_registro",
        "estado_autorizacion",
        "fecha_resolucion",
        "ci_fun",
        "num_fun",
        "nombre_fun",
        "cargo_fun",
        "articulo",
        "comentarios",
    )
    list_editable = ("estado_autorizacion", "fecha_resolucion",)
    list_filter = ("estado_autorizacion", ("fecha_registro",DateRangeFilter),)
    list_per_page = 10
    exclude = (
        "usuario",
        "fecha_registro",
        "estado_autorizacion",
        "fecha_resolucion",
        "ci_fun",
        "num_fun",
        "nombre_fun",
        "cargo_fun",
        "articulo",
        "comentarios",
    )
    
admin.site.register(Descuentos, DescuentosAdmin)
admin.site.register(PedidoLuces, PedidoLucesAdmin)
admin.site.register(PedidoBolsas, PedidoBolsasAdmin)
admin.site.register(PedidoFarmacia, PedidoFarmaciaAdmin)
admin.site.register(PedidoPapeleria, PedidoPapeleriaAdmin)
admin.site.register(PedidoLimpieza, PedidoLimpiezaAdmin)
admin.site.register(PedidoDiseno, PedidoDisenoAdmin)
admin.site.register(PedidoReparaciones, PedidoReparacionesAdmin)
admin.site.register(PedidoCambio, PedidoCambioAdmin)
admin.site.register(PedidoUniforme, PedidoUniformeAdmin)
admin.site.register(ChequeUniforme, ChequeUniformeAdmin)
