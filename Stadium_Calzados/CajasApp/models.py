from django.db import models
from .choices import *
from FuncionariosApp.models import *

# Create your models here.

class RetiraCliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    ci_cliente = models.IntegerField()
    articulo_cliente = models.CharField(max_length=17)
    sucursal_retiro = models.IntegerField(choices=sucursales)
    transaccion_visual = models.IntegerField()
    fecha_generado = models.DateField()

class ValeCreditelCdelaCasa(models.Model):
    ci_cliente=models.IntegerField()
    nombre_cliente=models.CharField(max_length=100)
    empresa_cliente=models.CharField(max_length=50)
    importe_cliente=models.IntegerField()
    fpago_cliente=models.IntegerField()

    fecha_registro=models.DateField(auto_now=True, auto_now_add=False)
    usuario = models.CharField(max_length=20,blank=True,null=True)
    num_cajera = models.IntegerField(blank=True, null=True)
    num_vta=models.IntegerField(blank=True,null=True)
    num_dev=models.IntegerField(blank=True,null=True)
    imp_facturado=models.IntegerField(blank=True,null=True)
    num_seña = models.IntegerField(blank=True, null=True)
    comentarios = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)

class ValeCorreo(models.Model):
    ci_cliente=models.IntegerField()
    nombre_cliente=models.CharField(max_length=100)
    importe_cliente=models.IntegerField()
    genero_cliente=models.CharField(max_length=20, choices=sexo)

    fecha_registro=models.DateField(auto_now=True, auto_now_add=False)
    usuario = models.CharField(max_length=20,blank=True,null=True)
    num_cajera = models.IntegerField(blank=True, null=True)
    num_vta=models.IntegerField(blank=True,null=True)
    num_dev=models.IntegerField(blank=True,null=True)
    comentarios = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=True)