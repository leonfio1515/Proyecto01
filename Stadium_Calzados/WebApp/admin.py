from django.contrib import admin
from .models import *
# Register your models here.


class CancelacionClienteAdmin(admin.ModelAdmin):
   list_display = (
       "usuario",
       "Fecha",
       "Nombre",
       "CI",
       "Plataforma",
       "Medio_pago",
       "Pedido",
       "Fecha_cancela",
       "Fecha_recibido",
       "Importe",
       "Motivo",
       "Comentario",
   )

   search_fields = (
       "usuario",
       "Fecha",
       "Nombre",
       "CI",
       "Plataforma",
       "Medio_pago",
       "Pedido",
       "Fecha_cancela",
       "Fecha_recibido",
       "Importe",
       "Motivo",
       "Comentario",
   )


class CambiosMLAdmin(admin.ModelAdmin):
   list_display = (
       "usuario",
       "Fecha",
       "Nombre",
       "CI",
       "Pedido",
       "Fecha_compra",
       "Importe",
       "Comentario",
   )

   search_fields = (
       "usuario",
       "Fecha",
       "Nombre",
       "CI",
       "Pedido",
       "Fecha_compra",
       "Importe",
       "Comentario",
   )


admin.site.register(CancelacionCliente, CancelacionClienteAdmin)
admin.site.register(CambiosML, CambiosMLAdmin)
