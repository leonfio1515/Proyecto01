from django.contrib import admin
from .models import *
from FormulariosApp.models import ValeApmu,ValeConrad
# Register your models here.


class QuebrantosAdmin(admin.ModelAdmin):
   list_display = (
       "usuario",
       "fecha_registro",
       "sucursal",
       "fecha_faltante",
       "num_cajera",
       "nombre_cajera",
       "num_boleta",
       "importe_faltante",
       "comentario",
   )

   search_fields = (
       "usuario",
       "fecha_registro",
       "sucursal",
       "fecha_faltante",
       "num_cajera",
       "nombre_cajera",
       "num_boleta",
       "importe_faltante",
       "comentario",
   )


class ManualesAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_manual",
   )

   search_fields = (
       "nombre_manual",
   )

class ErroresAdmin(admin.ModelAdmin):
   list_display = (
       "usuario",
       "Fecha_registro",
       "sucursal",
       "fecha_error",
       "num_cajera",
       "num_boleta",
       "grupo",
       "comentario",
   )

   search_fields = (
       "usuario",
       "Fecha_registro",
       "sucursal",
       "fecha_error",
       "num_cajera",
       "num_boleta",
       "grupo",
       "comentario",
   )


class RetopAdmin(admin.ModelAdmin):
   list_display = (
       "usuario",
       "fecha_registro",
       "num_comercio",
       "fecha_orden",
       "importe",
       "plan",
   )

   search_fields = (
       "usuario",
       "fecha_registro",
       "num_comercio",
       "fecha_orden",
       "importe",
       "plan",
   )

class PromotoraAdmin(admin.ModelAdmin):
   list_display = (
       "usuario",
       "fecha_registro",
       "num_orden",
       "fecha_orden",
       "importe",
       "plan",
       "promo",
   )

   search_fields = (
       "usuario",
       "fecha_registro",
       "num_orden",
       "fecha_orden",
       "importe",
       "plan",
       "promo",
   )

class CreditosDAdmin(admin.ModelAdmin):
   list_display = (
       "usuario",
       "fecha_registro",
       "num_orden",
       "fecha_orden",
       "importe",
       "plan",
   )

   search_fields = (
       "usuario",
       "fecha_registro",
       "num_orden",
       "fecha_orden",
       "importe",
       "plan",
   )


class ValeConradDAdmin(admin.ModelAdmin):
   list_display = (
       "usuario",
       "fecha_carga",
       "fecha_vta",
       "num_vale",
       "nombre_fun",
       "num_vta",
       "num_dev",
   )

   search_fields = (
       "usuario",
       "fecha_carga",
       "fecha_vta",
       "num_vale",
       "nombre_fun",
       "num_vta",
       "num_dev",
   )


class ValeApmuDAdmin(admin.ModelAdmin):
   list_display = (
       "usuario",
       "fecha_carga",
       "num_vale",
       "nombre_fun",
       "apellido_fun",
       "num_fun",
       "fecha_vta",
       "num_dev",
       "comentarios",
   )

   search_fields = (
       "usuario",
       "fecha_carga",
       "num_vale",
       "nombre_fun",
       "apellido_fun",
       "num_fun",
       "fecha_vta",
       "num_dev",
       "comentarios",
   )


admin.site.register(RegistroQuebranto, QuebrantosAdmin)
admin.site.register(Manuales, ManualesAdmin)
admin.site.register(Errores, ErroresAdmin)
admin.site.register(PresRetop, RetopAdmin)
admin.site.register(PresPromotora, PromotoraAdmin)
admin.site.register(PresCreditosD, CreditosDAdmin)
admin.site.register(ValeConrad, ValeConradDAdmin)
admin.site.register(ValeApmu, ValeApmuDAdmin)
