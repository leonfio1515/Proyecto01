from time import strftime
from django.db import models
from .choices import *

# Create your models here.
class EmpresasConvenio(models.Model):
    nombre_convenio=models.CharField(max_length=50,name="Nombre")
    num_convenio = models.IntegerField(name="Numero")
    codigoSAP_convenio = models.CharField(max_length=50, name="Codigo_SAP")
    fecha_corte_convenio = models.IntegerField(name="Fecha_corte")
    bonificacion_convenio = models.ImageField(name="Bonificacion")
    medio_pago_convenio = models.CharField(
        max_length=50, choices=medio_pago, name="Medio_pago")

class CobranzasConvenios(models.Model):
    mes_cobro=models.CharField(max_length=50, choices=mes)
    fecha_corte=models.CharField(max_length=50)
    num_empresa = models.IntegerField()
    nombre_empresa = models.CharField(max_length=50)
    mes_resumen=models.CharField(max_length=50, choices=mes)
    imp_resumen=models.IntegerField()
    imp_bonificacion=models.IntegerField(default=0, blank=True,null=True)
    num_documento = models.IntegerField(default=0, blank=True, null=True)
    imp_resguardo = models.IntegerField(default=0, blank=True, null=True)
    imp_recargo = models.IntegerField(default=0,  blank=True ,null=True)
    imp_cobrar=models.IntegerField()
    medio_pago=models.CharField(max_length=50, choices=medio_pago)

    sap_banco = models.IntegerField(blank=True,null=True)
    sap_convenios = models.IntegerField(default=0, blank=True, null=True)
    imp_pago = models.IntegerField(blank=True,null=True)
    fecha_pago=models.DateField(blank=True,null=True)
    estado = models.BooleanField(default=True)
