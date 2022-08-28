from django.contrib import admin
from .models import *
# Register your models here.


class FuncionariosAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_funcionario",
       "apellido_funcionario",
       "cedula_funcionario",
       "numero_funcionario",
       "cargo_funcionario",
       "sexo_funcionario",
       "fecha_ingreso",
       "estado_funcionario",
   )

   search_fields = (
       "nombre_funcionario",
       "apellido_funcionario",
       "cedula_funcionario",
       "numero_funcionario",
       "cargo_funcionario",
       "sexo_funcionario",
       "fecha_ingreso",
       "estado_funcionario",
   )


class SucursalesAdmin(admin.ModelAdmin):
   list_display = (
       "nombre_sucursales",
   )

   search_fields = (
       "nombre_sucursales",
   )

admin.site.register(Funcionarios, FuncionariosAdmin)
admin.site.register(Sucursales, SucursalesAdmin)
