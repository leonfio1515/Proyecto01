from django import forms
from .models import *


class DescuentosForm(forms.Form):
    valor_descuento=forms.IntegerField(label="% Descuento")
    fecha_descuento=forms.DateField(label="Fecha del descuento")
    nombre_descuento=forms.CharField(label="Nombre del descuento")

class BolsasForm(forms.ModelForm):
    class Meta:
        model = PedidoBolsas
        fields=[
            "Bolsa_chica",
            "Bolsa_media",
            "Bolsa_grande",
        ]
        widgets={
            "Bolsa_chica": forms.NumberInput(
                attrs={"class": "form-control text-center"}
                ),
            "Bolsa_media": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Bolsa_grande": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),

            }

class LucesForm(forms.ModelForm):
    class Meta:
        model = PedidoLuces
        fields=[
            "AR111",
            "EMB",
            "Lampara",
            "Par30_fria",
            "Par30_calida",
            "Tacho",
            "Tubo_led",
            "Driver",
            "Dicroica_led",
        ]
        widgets={
            "AR111": forms.NumberInput(
                attrs={"class": "form-control text-center"}
                ),
            "EMB": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Lampara": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Par30_fria": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Par30_calida": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Tacho": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Tubo_led": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Driver": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Dicroica_led": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),

            }

class FarmaciaForm(forms.ModelForm):
    class Meta:
        model = PedidoFarmacia
        fields=[
            "Ibuprofeno",
            "Leuco",
            "Iodofon",
            "Gasa",
            "Disan",
            "Curitas",
            "Algodon",
            "Alcohol_rectificado",
            "Alcohol_gel",
            "Agua_oxigenada",
        ]
        widgets={
            "Ibuprofeno": forms.NumberInput(
                attrs={"class": "form-control text-center"}
                ),
            "Leuco": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Iodofon": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Gasa": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Disan": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Curitas": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Algodon": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Alcohol_rectificado": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Alcohol_gel": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Agua_oxigenada": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),

            }

class DisenoForm(forms.ModelForm):
    class Meta:
        model = PedidoDiseno
        fields=[
            "Tarjeta_presentacion",
            "Tarjeta_atencion",
            "Talon_cambio",
        ]
        widgets={
            "Tarjeta_presentacion": forms.NumberInput(
                attrs={"class": "form-control text-center"}
                ),
            "Tarjeta_atencion": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Talon_cambio": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),

            }

class LimpiezaForm(forms.ModelForm):
    class Meta:
        model = PedidoLimpieza
        fields=[
            "Plumero",
            "Insecticida",
            "Pulidor_cremoso",
            "Perfumol",
            "PH",
            "Panos_piso",
            "Limpia_vidrio",
            "Hipoclorito",
            "Jabon_liq",
            "Franela",
            "Esponja",
            "Detergente",
            "Cera_roja",
            "Cera_incolora",
            "Bolsas",
            "Lustramueble",
            "Des_ambiente",
        ]
        widgets={
            "Plumero": forms.NumberInput(
                attrs={"class": "form-control text-center"}
                ),
            "Insecticida": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Pulidor_cremoso": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Perfumol": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "PH": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Panos_piso": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Limpia_vidrio": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Hipoclorito": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Jabon_liq": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Franela": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Esponja": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Detergente": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Cera_roja": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Cera_incolora": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Bolsas": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Lustramueble": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),
            "Des_ambiente": forms.NumberInput(
                attrs={"class":"form-control text-center"}
                ),

            }


class ReparacionesForm(forms.ModelForm):
    class Meta:
        model = PedidoReparaciones
        fields=[
            "Servicio",
            "Asunto",
            "Comentario",
        ]
        widgets={
            "Servicio": forms.ChoiceField(choices=servicios,
                ),
            "Asunto": forms.TextInput(
                attrs={"class":"form-control text-center col-md-9"}
                ),
            "Comentario": forms.Textarea(
                attrs={"class":"form-control text-center col-md-9"}
                ),

            }

class PapeleriaForm(forms.ModelForm):
    class Meta:
        model = PedidoPapeleria
        fields=[
            "Lapiceras",
            "Clips",
            "Lapiz",
            "Lapicera_mostrador",
            "Cinta_fina_1",
            "Cinta_fina_2",
            "Cinta_anchaT",
            "Cinta_impresa",
            "Etiqueta_60X40",
            "Marcador_perm_fino",
            "Marcador_fluor",
            "Medias",
            "Grapas",
            "PilasAA",
            "PilasAAA",
            "Precinto_cajon",
            "Precinto_sobre",
            "ResmaA4",
            "Resma_otro",
            "Ribbon",
            "Rollo_calc",
            "Rollo_fact",
            "Sobre_carta",
            "Tinta_calc",
            "Hilos",
            "Pistola",
            "Trincheta",
            "Tijera",
            "Etiqueta_60X150",
            "Goma",
            "Banda_elastica",
            "Marcador_perm_grueso",
            "Carpeta",
            "Tinta_sello",
            "Grapadora",
            "Etiqueta_color",
        ]
        widgets={
            "Lapiceras": forms.TextInput(
                attrs={"class": "form-control text-center"}
                ),
            "Clips": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Lapiz": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Lapicera_mostrador": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Cinta_fina_1": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Cinta_fina_2": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Cinta_anchaT": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Cinta_impresa": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Etiqueta_60X40": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Marcador_perm_fino": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Marcador_fluor": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Medias": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Grapas": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "PilasAA": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "PilasAAA": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Precinto_cajon": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Precinto_sobre": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "ResmaA4": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Resma_otro": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Ribbon": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Rollo_calc": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Rollo_fact": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Sobre_carta": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Tinta_calc": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Hilos": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Pistola": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Trincheta": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Tijera": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Etiqueta_60X150": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Goma": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Banda_elastica": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Marcador_perm_grueso": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Carpeta": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Tinta_sello": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Grapadora": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            "Etiqueta_color": forms.TextInput(
                attrs={"class":"form-control text-center"}
                ),
            }

