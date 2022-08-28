from django.contrib import admin
from .models import *

# Register your models here.


class LucesAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_luces",
       "imagen_luces",
       "medida_luces",
   )

   search_fields = (
       "nombre_luces",
       "imagen_luces",
       "medida_luces",
   )

class BolsasAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_bolsas",
       "codigoSAP_bolsas",
       "medida_bolsas",
   )

   search_fields = (
       "nombre_bolsas",
       "codigoSAP_bolsas",
       "medida_bolsas",
   )

class PapeleriaAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_papeleria",
       "codigoSAP_papeleria",
       "medida_papeleria",
   )

   search_fields = (
       "nombre_papeleria",
       "codigoSAP_papeleria",
       "medida_papeleria",
   )

class FarmaciaAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_farmacia",
       "codigoSAP_farmacia",
       "medida_farmacia",
   )

   search_fields = (
       "nombre_farmacia",
       "codigoSAP_farmacia",
       "medida_farmacia",
   )

class LimpiezaAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_limpieza",
       "codigoSAP_limpieza",
       "medida_limpieza",
   )

   search_fields = (
       "nombre_limpieza",
       "codigoSAP_limpieza",
       "medida_limpieza",
   )

class DisenoAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_diseno",
       "codigoSAP_diseno",
       "medida_diseno",
   )

   search_fields = (
       "nombre_diseno",
       "codigoSAP_diseno",
       "medida_diseno",
   )

class ReparacionesAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_servicio",
       "Empresa",
       "Telefono",
       "Email",

   )

   search_fields = (
       "nombre_servicio",
       "Empresa",
       "Telefono",
       "Email",
   )

class NoticiasAdmin(admin.ModelAdmin):
   list_display = (
       "Nombre",
       "Tema",
       "Descripcion",
       "Noticia",
       "Imagen",
       "fecha_noticia",
   )

   search_fields = (
       "Nombre",
       "Tema",
       "Descripcion",
       "Noticia",
       "Imagen",
       "fecha_noticia",
   )

admin.site.register(Luces, LucesAdmin)
admin.site.register(Bolsas, BolsasAdmin)
admin.site.register(Papeleria, PapeleriaAdmin)
admin.site.register(Farmacia, FarmaciaAdmin)
admin.site.register(Limpieza, LimpiezaAdmin)
admin.site.register(Diseno, DisenoAdmin)
admin.site.register(Reparaciones, ReparacionesAdmin)
admin.site.register(Noticias, NoticiasAdmin)
