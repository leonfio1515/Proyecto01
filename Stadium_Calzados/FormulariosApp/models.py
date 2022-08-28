from django.db import models
from django.contrib.auth.models import User
from ArticulosApp.models import *
from .choices import *

# Create your models here.

#Modelo Formularios
class Descuentos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creado = models.DateField("Fecha_creado", auto_now=True, auto_now_add=False) #Se crea automaticamente con cada registro
    valor_descuento = models.CharField(max_length=5)
    fecha_descuento= models.DateField()
    nombre_descuento=models.CharField(max_length=50)


class PedidoLuces(models.Model):
    usuario = models.CharField(max_length=20, blank=True, null=True)
    fecha_pedido_luces = models.DateField(auto_now=True, auto_now_add=False,
        blank=True, null=True, name="Fecha_pedido")
    cantidad_ar111 = models.IntegerField(
        blank=True, null=True, name="AR111")
    cantidad_dicroica_led = models.IntegerField(blank=True, null=True, name="Dicroica_led")
    cantidad_emb = models.IntegerField(
        blank=True, null=True, name="EMB")
    cantidad_lampara = models.IntegerField(
        blank=True, null=True, name="Lampara")
    cantidad_par30_fria = models.IntegerField(
        blank=True, null=True, name="Par30_fria")
    cantidad_par30_calida = models.IntegerField(
        blank=True, null=True, name="Par30_calida")
    cantidad_tacho = models.IntegerField(
        blank=True, null=True, name="Tacho")
    cantidad_tubo_led = models.IntegerField(
        blank=True, null=True, name="Tubo_led")
    cantidad_driver = models.IntegerField(
        blank=True, null=True, name="Driver")
    fecha_enviado = models.DateField(blank=True, null=True, name="Fecha_enviado")

class PedidoFarmacia(models.Model):
    usuario = models.CharField(max_length=20, blank=True, null=True)
    fecha_pedido_farmacia = models.DateField(auto_now=True, auto_now_add=False,blank=True, null=True, name="Fecha_pedido")
    cantidad_ibuprofeno = models.IntegerField(blank=True, null=True, name="Ibuprofeno")
    cantidad_leuco = models.IntegerField(blank=True, null=True, name="Leuco")
    cantidad_iodofon = models.IntegerField(blank=True, null=True, name="Iodofon")
    cantidad_gasa = models.IntegerField(blank=True, null=True, name="Gasa")
    cantidad_disan = models.IntegerField(blank=True, null=True, name="Disan")
    cantidad_curitas = models.IntegerField(blank=True, null=True, name="Curitas")
    cantidad_algodon = models.IntegerField(blank=True, null=True, name="Algodon")
    cantidad_alcohol_rectificado = models.IntegerField(blank=True, null=True, name="Alcohol_rectificado")
    cantidad_alcohol_gel = models.IntegerField(blank=True, null=True, name="Alcohol_gel")
    cantidad_agua_oxigenada = models.IntegerField(blank=True, null=True, name="Agua_oxigenada")
    fecha_enviado = models.DateField(blank=True, null=True, name="Fecha_enviado")

class PedidoDiseno(models.Model):
    usuario = models.CharField(max_length=20, blank=True, null=True)
    fecha_pedido_diseno = models.DateField(auto_now=True, auto_now_add=False,blank=True, null=True, name="Fecha_pedido")
    cantidad_tarj_presentacion = models.IntegerField(
        blank=True, null=True, name="Tarjeta_presentacion")
    cantidad_tarj_atencion = models.IntegerField(
        blank=True, null=True, name="Tarjeta_atencion")
    cantidad_talon_cambio = models.IntegerField(
        blank=True, null=True, name="Talon_cambio")
    fecha_enviado = models.DateField(blank=True, null=True, name="Fecha_enviado")

class PedidoBolsas(models.Model):
    usuario = models.CharField(max_length=20, blank=True, null=True)
    fecha_pedido_bolsas = models.DateField(auto_now=True, auto_now_add=False,
        blank=True, null=True, name="Fecha_pedido")
    cantidad_bolsa_chica = models.IntegerField(
        blank=True, null=True, name="Bolsa_chica")
    cantidad_bolsa_media = models.IntegerField(
        blank=True, null=True, name="Bolsa_media")
    cantidad_bolsa_grande = models.IntegerField(
        blank=True, null=True, name="Bolsa_grande")
    fecha_enviado = models.DateField(blank=True, null=True, name="Fecha_enviado")
    
class PedidoLimpieza(models.Model):
    usuario = models.CharField(max_length=20, blank=True, null=True)
    fecha_pedido_limpieza = models.DateField(auto_now=True, auto_now_add=False,blank=True, null=True, name="Fecha_pedido")
    cantidad_plumero = models.IntegerField(blank=True, null=True, name="Plumero")
    cantidad_insecticida = models.IntegerField(blank=True, null=True, name="Insecticida")
    cantidad_pulidor_cremoso = models.IntegerField(blank=True, null=True, name="Pulidor_cremoso")
    cantidad_perfumol = models.IntegerField(blank=True, null=True, name="Perfumol")
    cantidad_ph = models.IntegerField(blank=True, null=True, name="PH")
    cantidad_panos_piso = models.IntegerField(blank=True, null=True, name="Panos_piso")
    cantidad_limpia_vidrio = models.IntegerField(blank=True, null=True, name="Limpia_vidrio")
    cantidad_hipoclorito = models.IntegerField(blank=True, null=True, name="Hipoclorito")
    cantidad_jabon_liq = models.IntegerField(blank=True, null=True, name="Jabon_liq")
    cantidad_franela = models.IntegerField(blank=True, null=True, name="Franela")
    cantidad_esponja = models.IntegerField(blank=True, null=True, name="Esponja")
    cantidad_detergente = models.IntegerField(blank=True, null=True, name="Detergente")
    cantidad_cera_roja = models.IntegerField(blank=True, null=True, name="Cera_roja")
    cantidad_cera_inc = models.IntegerField(blank=True, null=True, name="Cera_incolora")
    cantidad_bolsas = models.IntegerField(blank=True, null=True, name="Bolsas")
    cantidad_lustramueble = models.IntegerField(blank=True, null=True, name="Lustramueble")
    cantidad_des_ambiente = models.IntegerField(blank=True, null=True, name="Des_ambiente")
    fecha_enviado = models.DateField(blank=True, null=True, name="Fecha_enviado")

class PedidoPapeleria(models.Model):
    usuario = models.CharField(max_length=20, blank=True, null=True)
    fecha_pedido_papeleria = models.DateField(auto_now=True, auto_now_add=False,blank=True, null=True, name="Fecha_pedido")
    cantidad_lapiceras=models.IntegerField(blank=True, null=True, name="Lapiceras")
    cantidad_clips=models.IntegerField(blank=True, null=True, name="Clips")
    cantidad_lapiz=models.IntegerField(blank=True, null=True, name="Lapiz")
    cantidad_lapicera_mostrador=models.IntegerField(blank=True, null=True, name="Lapicera_mostrador")
    cantidad_cinta_fina1=models.IntegerField(blank=True, null=True, name="Cinta_fina_1")
    cantidad_cinta_fina2=models.IntegerField(blank=True, null=True, name="Cinta_fina_2")
    cantidad_cinta_anchaT=models.IntegerField(blank=True, null=True, name="Cinta_anchaT")
    cantidad_cinta_impresa=models.IntegerField(blank=True, null=True, name="Cinta_impresa")
    cantidad_etiqueta_60x40=models.IntegerField(blank=True, null=True, name="Etiqueta_60X40")
    cantidad_marcador_perm_fino=models.IntegerField(blank=True, null=True, name="Marcador_perm_fino")
    cantidad_marcador_fluor=models.IntegerField(blank=True, null=True, name="Marcador_fluor")
    cantidad_medias=models.IntegerField(blank=True, null=True, name="Medias")
    cantidad_grapas=models.IntegerField(blank=True, null=True, name="Grapas")
    cantidad_pilasAA=models.IntegerField(blank=True, null=True, name="PilasAA")
    cantidad_pilasAAA=models.IntegerField(blank=True, null=True, name="PilasAAA")
    cantidad_precinto_cajon=models.IntegerField(blank=True, null=True, name="Precinto_cajon")
    cantidad_precinto_sobre=models.IntegerField(blank=True, null=True, name="Precinto_sobre")
    cantidad_resmaA4=models.IntegerField(blank=True, null=True, name="ResmaA4")
    cantidad_resma_otro=models.IntegerField(blank=True, null=True, name="Resma_otro")
    cantidad_ribbon=models.IntegerField(blank=True, null=True, name="Ribbon")
    cantidad_rollo_calc=models.IntegerField(blank=True, null=True, name="Rollo_calc")
    cantidad_rollo_fact=models.IntegerField(blank=True, null=True, name="Rollo_fact")
    cantidad_sobre_carta=models.IntegerField(blank=True, null=True, name="Sobre_carta")
    cantidad_tinta_calc=models.IntegerField(blank=True, null=True, name="Tinta_calc")
    cantidad_hilos=models.IntegerField(blank=True, null=True, name="Hilos")
    cantidad_pistola=models.IntegerField(blank=True, null=True, name="Pistola")
    cantidad_trincheta=models.IntegerField(blank=True, null=True, name="Trincheta")
    cantidad_tijera=models.IntegerField(blank=True, null=True, name="Tijera")
    cantidad_etiqueta_60x150=models.IntegerField(blank=True, null=True, name="Etiqueta_60X150")
    cantidad_goma=models.IntegerField(blank=True, null=True, name="Goma")
    cantidad_banda_elastica=models.IntegerField(blank=True, null=True, name="Banda_elastica")
    cantidad_marcador_perm_grueso=models.IntegerField(blank=True, null=True, name="Marcador_perm_grueso")
    cantidad_carpeta=models.IntegerField(blank=True, null=True, name="Carpeta")
    cantidad_tinta_sello=models.IntegerField(blank=True, null=True, name="Tinta_sello")
    cantidad_grapadora=models.IntegerField(blank=True, null=True, name="Grapadora")
    cantidad_etiqueta_color=models.IntegerField(blank=True, null=True, name="Etiqueta_color")
    fecha_enviado = models.DateField(blank=True, null=True, name="Fecha_enviado")
    

class PedidoReparaciones(models.Model):
    usuario = models.CharField(max_length=20, blank=True, null=True)
    fecha_pedido_reparaciones = models.DateField(auto_now=True, auto_now_add=False,blank=True, null=True, name="Fecha_pedido")
    nombre_servicio = models.TextField(max_length=200,choices=servicios, blank=True, null=True, name="Servicio")
    asunto_reparacion = models.CharField(max_length=100, blank=True, null=True, name="Asunto")
    comentario_reparacion = models.CharField(max_length=300, blank=True, null=True, name="Comentario")
    estado_reparacion = models.CharField(max_length=20, choices=estado, blank=True, null=True, name="Estado")
    fecha_resuelto = models.DateField(blank=True, null=True, name="Fecha_resuelto")
    comentarios_resuelto = models.TextField(max_length=200, blank=True, null=True, name="Comentario_resuelto")

class PedidoCambio(models.Model):
    usuario = models.CharField(max_length=20, blank=True, null=True)
    fecha_pedido = models.DateField(auto_now=True, auto_now_add=False)
    monedas_1=models.IntegerField()
    monedas_2=models.IntegerField()
    monedas_5=models.IntegerField()
    monedas_10=models.IntegerField()
    billetes_20=models.IntegerField()
    billetes_50=models.IntegerField()
    billetes_100=models.IntegerField()
    billetes_200=models.IntegerField()
    fecha_enviado = models.DateField(blank=True, null=True)

class PedidoUniforme(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_pedido = models.DateField(auto_now=True, auto_now_add=False)
    num_fun = models.IntegerField()
    ci_fun = models.IntegerField()
    talle_camisa = models.CharField(max_length=20)
    talle_pantalon = models.CharField(max_length=20)
    talle_abrigo = models.CharField(max_length=20)
    area_trabajo = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)
    fecha_enviado = models.DateField(blank=True, null=True)

class ValeConrad(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_carga = models.DateField(auto_now=True, auto_now_add=False)
    fecha_vta = models.DateField()
    num_vale = models.IntegerField()
    nombre_fun = models.CharField(max_length=100)
    num_vta = models.IntegerField()
    num_dev = models.IntegerField()

class ValeApmu(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_carga = models.DateField(auto_now=True, auto_now_add=False)
    num_vale = models.IntegerField()
    nombre_fun = models.CharField(max_length=100)
    apellido_fun = models.CharField(max_length=100)
    num_fun = models.IntegerField()
    fecha_vta = models.DateField()
    num_dev = models.IntegerField()
    comentarios = models.CharField(max_length=500)

class ChequeUniforme(models.Model):
    usuario = models.CharField(max_length=20)
    fecha_registro = models.DateField(auto_now=True, auto_now_add=False)
    ci_fun = models.IntegerField()
    num_fun = models.IntegerField()
    nombre_fun = models.CharField(max_length=60)
    cargo_fun = models.CharField(max_length=60)
    articulo = models.CharField(max_length=17)
    comentarios = models.CharField(max_length=150)

    estado_autorizacion = models.CharField(max_length=10, choices=autorizacion, blank=True, null=True, default="Pendiente")
    fecha_resolucion = models.DateField(blank=True, null=True)
    comentario_adm = models.CharField(max_length=500, blank=True, null=True)
    num_vta = models.IntegerField(blank=True, null=True)
