from django import forms
from .models import *

class ErroresForm(forms.ModelForm):
    class Meta:
        model=Errores
        fields=[
           "sucursal",
           "fecha_error",
           "num_cajera",
           "num_boleta",
           "grupo",
           "comentario",
        ]
        widgets={
        "sucursal": forms.NumberInput(
            attrs={"class": "form-control text-center"}
            ),
        "fecha_error": forms.DateInput(
            attrs={"class":"form-control text-center"}
            ),
        "num_cajera": forms.NumberInput(
            attrs={"class":"form-control text-center"}
            ),
        "num_boleta": forms.NumberInput(
            attrs={"class":"form-control text-center"}
            ),
        "grupo": forms.TextInput(
            attrs={"class":"form-control text-center"}
            ),
            "comentario": forms.TextInput(
            attrs={"class":"form-control text-center"}
            ),

        }


class QuebrantosForm(forms.ModelForm):
    class Meta:
        model = RegistroQuebranto
        fields = [
            "sucursal",
            "fecha_faltante",
            "num_cajera",
            "nombre_cajera",
            "num_boleta",
            "importe_faltante",
            "comentario",
        ]
 

class RetopForm(forms.ModelForm):
    class Meta:
        model = PresRetop
        fields = [
            "num_comercio",
            "fecha_orden",
            "importe",
            "plan",
        ]


class PromotoraForm(forms.ModelForm):
    class Meta:
        model = PresPromotora
        fields = [
            "num_orden",
            "fecha_orden",
            "importe",
            "plan",
            "promo",
        ]


class CreditosDForm(forms.ModelForm):
    class Meta:
        model = PresCreditosD
        fields = [
            "num_orden",
            "fecha_orden",
            "importe",
            "plan",
        ]
