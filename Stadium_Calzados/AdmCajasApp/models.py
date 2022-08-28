from django.db import models

# Create your models here.
class RegistroQuebranto(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_registro=models.DateField(auto_now=True, auto_now_add=False,blank=True, null=True)
    sucursal = models.IntegerField(blank=True, null=True)
    fecha_faltante=models.DateField(blank=True, null=True)
    num_cajera=models.CharField(max_length=20,blank=True, null=True)
    nombre_cajera=models.CharField(max_length=20,blank=True, null=True)
    num_boleta = models.IntegerField(blank=True, null=True)
    importe_faltante = models.IntegerField(blank=True, null=True)
    comentario = models.CharField(max_length=200, blank=True, null=True)

class Manuales(models.Model):
    nombre_manual = models.CharField(max_length=50, blank=True, default="")
    manual = models.FileField(upload_to="media/")

class Errores(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_registro=models.DateField(auto_now=True, auto_now_add=False,blank=True, null=True, name="Fecha_registro")
    sucursal=models.IntegerField()
    fecha_error=models.DateField()
    num_cajera=models.IntegerField()
    num_boleta=models.IntegerField()
    grupo=models.CharField(max_length=50, null=True)
    comentario=models.CharField(max_length=500, null=True)

class PresRetop(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_registro = models.DateField(auto_now=True, auto_now_add=False)
    num_comercio=models.IntegerField()
    fecha_orden=models.DateField()
    importe=models.IntegerField()
    plan=models.CharField(max_length=5)

class PresPromotora(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_registro=models.DateField(auto_now=True, auto_now_add=False)
    num_orden = models.IntegerField()
    fecha_orden = models.DateField()
    importe = models.IntegerField()
    plan = models.CharField(max_length=5)
    promo=models.BooleanField(default=False)

class PresCreditosD(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_registro = models.DateField(auto_now=True, auto_now_add=False)
    num_orden = models.IntegerField()
    fecha_orden = models.DateField()
    importe = models.IntegerField()
    plan = models.CharField(max_length=5)
