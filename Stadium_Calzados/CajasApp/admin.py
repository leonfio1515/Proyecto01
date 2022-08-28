from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.



class RetiraClienteAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_cliente",
       "ci_cliente",
       "articulo_cliente",
       "sucursal_retiro",
       "transaccion_visual",
       "fecha_generado",
   )

   search_fields = (
       "nombre_cliente",
       "ci_cliente",
       "articulo_cliente",
       "sucursal_retiro",
       "transaccion_visual",
       "fecha_generado",
   )


class ValeCreditelCdelaCasaResource(resources.ModelResource):
    class Meta:
        model = ValeCreditelCdelaCasa

class ValeCreditelCdelaCasaAdmin(ImportExportActionModelAdmin):
   list_display = (
       "ci_cliente",
       "nombre_cliente",
       "empresa_cliente",
       "importe_cliente",
       "fpago_cliente",
       "fecha_registro",
       "estado",
   )

   search_fields = (
       "ci_cliente",
       "nombre_cliente",
       "empresa_cliente",
       "importe_cliente",
       "fpago_cliente",
       "estado",
   )


class ValeCorreoResource(resources.ModelResource):
    class Meta:
        model = ValeCorreo


class ValeCorreoAdmin(ImportExportActionModelAdmin):
   list_display = (
       "ci_cliente",
       "nombre_cliente",
       "importe_cliente",
       "fecha_registro",
       "estado",
   )

   search_fields = (
       "ci_cliente",
       "nombre_cliente",
       "importe_cliente",
       "fecha_registro",
       "estado",
   )

admin.site.register(RetiraCliente, RetiraClienteAdmin)
admin.site.register(ValeCreditelCdelaCasa, ValeCreditelCdelaCasaAdmin)
admin.site.register(ValeCorreo, ValeCorreoAdmin)
