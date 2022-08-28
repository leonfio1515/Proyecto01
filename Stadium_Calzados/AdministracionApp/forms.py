from django import forms
from .models import *


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensajes
        fields = [
            "nombre",
            "asunto",
            "mensaje",
        ]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control text-center"}
            ),
            "asunto": forms.TextInput(
                attrs={"class": "form-control text-center"}
            ),
            "mensaje": forms.TextInput(
                attrs={"class": "form-control text-center"}
            ),
        }
