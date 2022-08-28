from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CancelacionCliente(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_carga = models.DateField(name="Fecha")
    nombre_cancelacion = models.CharField(max_length=50,name="Nombre")
    ci_cancelacion=models.IntegerField(name="CI")
    plataforma_cancelacion=models.CharField(max_length=50,name="Plataforma")
    mediopago_cancelacion=models.CharField(max_length=50,name="Medio_pago")
    pedido_cancelacion = models.IntegerField(name="Pedido")
    fecha_cancela = models.DateField(name="Fecha_cancela")
    fecha_recibido = models.DateField(name="Fecha_recibido")
    importe_cancelacion = models.IntegerField(name="Importe")
    motivo_cancelacion = models.CharField(max_length=50, name="Motivo")
    comentario_cancelacion=models.TextField(max_length=200,name="Comentario")

class CambiosML(models.Model):
    usuario=models.CharField(max_length=20)
    fecha_carga = models.DateField(name="Fecha")
    nombre_cambio = models.CharField(max_length=50, name="Nombre")
    ci_cambio = models.IntegerField(name="CI")
    pedido_cambio = models.IntegerField(name="Pedido")
    fecha_compra = models.DateField(name="Fecha_compra")
    importe_cambio = models.IntegerField(name="Importe")
    comentario_cambio=models.TextField(max_length=200,name="Comentario")
