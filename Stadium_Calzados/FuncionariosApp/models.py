from django.db import models
from.choices import *

# Create your models here.
class Funcionarios(models.Model):
    cedula_funcionario=models.IntegerField()
    nombre_funcionario=models.CharField(max_length=30)
    apellido_funcionario=models.CharField(max_length=30)
    numero_funcionario=models.IntegerField()
    cargo_funcionario = models.CharField(max_length=30, choices=cargo)
    sexo_funcionario = models.CharField(max_length=30, choices=sexo)
    fecha_ingreso=models.DateField()
    estado_funcionario=models.CharField(max_length=30, choices=estado)

class Sucursales(models.Model):
    nombre_sucursales=models.CharField(max_length=3)