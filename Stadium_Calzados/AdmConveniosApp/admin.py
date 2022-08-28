from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.


class CobranzasConveniosResource(resources.ModelResource):
    class Meta:
        model = CobranzasConvenios

class CobranzasConveniosAdmin(ImportExportActionModelAdmin):
   list_display = (
       "mes_cobro",
       "fecha_pago",
       "imp_pago",
       "sap_banco",
       "sap_convenios",

       "fecha_corte",
       "num_empresa",
       "nombre_empresa",
       "mes_resumen",
       "imp_cobrar",
       "medio_pago",
   )

   search_fields = (
       "mes_cobro",
       "fecha_corte",
       "num_empresa",
       "nombre_empresa",
       "mes_resumen",
       "imp_cobrar",
       "medio_pago",
   )
   list_per_page = 10
   exclude = ("fecha_pago", "imp_pago","sap_banco",)
   list_editable = ("sap_convenios",)
   list_filter = ("mes_cobro",)

admin.site.register(CobranzasConvenios, CobranzasConveniosAdmin)
