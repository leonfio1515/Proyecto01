from django.db import models
from FormulariosApp.choices import servicios
from .choices import *
# Create your models here.

#Modelo Articulos
class Luces(models.Model):
    imagen_luces = models.ImageField(upload_to="media/", blank=True, null=True)
    nombre_luces = models.CharField(max_length=20,blank=True, null=True)
    codigoSAP_luces = models.CharField(max_length=12, blank=True, null=True)
    medida_luces=models.CharField(max_length=20, blank=True, null=True)

class Bolsas(models.Model):
    nombre_bolsas =models.CharField(max_length=20)
    codigoSAP_bolsas=models.CharField(max_length=12, blank=True, null=True)
    medida_bolsas = models.CharField(max_length=20, blank=True, null=True)

class Papeleria(models.Model):
    nombre_papeleria = models.CharField(max_length=30)
    codigoSAP_papeleria = models.CharField(max_length=12,blank=True, null=True)
    medida_papeleria = models.CharField(max_length=20, blank=True, null=True)

class Farmacia(models.Model):
    nombre_farmacia = models.CharField(max_length=30)
    codigoSAP_farmacia = models.CharField(max_length=12, blank=True, null=True)
    medida_farmacia = models.CharField(max_length=20, blank=True, null=True)

class Limpieza(models.Model):
    nombre_limpieza = models.CharField(max_length=30)
    codigoSAP_limpieza = models.CharField(max_length=12, blank=True, null=True)
    medida_limpieza = models.CharField(max_length=20, blank=True, null=True)

class Diseno(models.Model):
    nombre_diseno = models.CharField(max_length=30)
    codigoSAP_diseno = models.CharField(max_length=12, blank=True, null=True)
    medida_diseno = models.CharField(max_length=20, blank=True, null=True)

class Reparaciones(models.Model):
    nombre_servicio=models.CharField(max_length=50, choices=servicios)
    nombre_empresa = models.CharField(max_length=50, blank=True, null=True, name="Empresa")
    tel_contacto = models.BigIntegerField(
        blank=True, null=True, name="Telefono")
    email_contacto = models.EmailField(blank=True, null=True, name="Email")

class Noticias(models.Model):
    nombre_noticia=models.CharField(max_length=50,name="Nombre")
    descripcion_noticia = models.CharField(max_length=200, name="Descripcion")
    noticia_noticia = models.TextField(max_length=5000, name="Noticia")
    imagen_noticia = models.ImageField(
        upload_to="media/", blank=True, null=True, name="Imagen")
    tema_noticia=models.CharField(max_length=50, choices=tema_noticia,name="Tema")
    fecha_noticia=models.DateField(blank=True, null=True)