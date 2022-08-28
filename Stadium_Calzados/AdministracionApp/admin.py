from django.contrib import admin
from .models import *
# Register your models here.

class MedioPagoAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_pago",
   )

   search_fields = (
       "nombre_pago",
   )

class PlataformaAdmin(admin.ModelAdmin):
   list_display = (
       "plataforma",
   )

   search_fields = (
       "plataforma",
   )

class MotivoDevAdmin(admin.ModelAdmin):
   list_display = (
       "motivoDevolucion",
   )

   search_fields = (
       "motivoDevolucion",
   )


class MensajesAdmin(admin.ModelAdmin):
   list_display = (
       "nombre",
       "asunto",
       "mensaje",
   )

   search_fields = (
       "nombre",
       "asunto",
       "mensaje",
   )

class PromocionesAdmin(admin.ModelAdmin):
   list_display = (
       "medio_promo",
       "valor_promo",
       "descripcion_promo",
       "imagen_promo",
       "fecha_inicio",
       "fecha_fin",
       "alcance_promo",
       "estado_promo",
   )

   search_fields = (
       "medio_promo",
       "valor_promo",
       "fecha_inicio",
       "fecha_fin",
       "estado_promo",
   )


class SucursalesAdmin(admin.ModelAdmin):
   list_display = (
       "numero_suc",
       "direccion_suc",
       "departamento_suc",
   )

   search_fields = (
       "numero_suc",
       "direccion_suc",
       "departamento_suc",
   )

admin.site.register(MediosPago, MedioPagoAdmin)
admin.site.register(Plataforma, PlataformaAdmin)
admin.site.register(MotivoDev, MotivoDevAdmin)
admin.site.register(Mensajes, MensajesAdmin)
admin.site.register(Sucursales, SucursalesAdmin)
admin.site.register(Promociones, PromocionesAdmin)
