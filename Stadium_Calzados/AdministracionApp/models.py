from django.db import models
from .choices import *

# Create your models here.

class MediosPago(models.Model):
    nombre_pago = models.CharField(max_length=50, choices=medioPago)

class Plataforma(models.Model):
    plataforma = models.CharField(max_length=50, choices=plataforma)

class MotivoDev(models.Model):
    motivoDevolucion = models.CharField(max_length=50, choices=motivoDev)


class Mensajes(models.Model):
    usuario = models.CharField(max_length=20, blank=True, null=True)
    fecha_creado = models.DateField("Fecha_creado", auto_now=True, auto_now_add=False)
    nombre = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=2000)
    respuesta=models.TextField(max_length=2000, blank=True,null=True)

class Sucursales(models.Model):
    numero_suc = models.CharField(max_length=3, blank=True, null=True)
    direccion_suc=models.CharField(max_length=90)
    departamento_suc = models.CharField(max_length=90, blank=True, null=True)

class Promociones(models.Model):
    medio_promo=models.CharField(max_length=50)
    valor_promo = models.CharField(max_length=50)
    descripcion_promo = models.CharField(max_length=200)
    imagen_promo = models.ImageField(
        upload_to="media/", blank=True, null=True)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    alcance_promo = models.CharField(max_length=200)
    estado_promo = models.BooleanField(default=False)
