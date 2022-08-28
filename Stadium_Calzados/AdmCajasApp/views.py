from django.shortcuts import render, redirect
from .models import *
from datetime import date, datetime
from django.views.generic.edit import CreateView
from .forms import *

# Create your views here.
class RegistroQuebrantosCreate(CreateView):
    model=RegistroQuebranto
    form_class=QuebrantosForm
    template_name="form_quebrantos.html"

    def post(self,request,*args,**kwargs):
        user = request.user.username
        form = self.form_class(request.POST)

        if form.is_valid():
            nuevo = RegistroQuebranto(
                    usuario=user,
                    sucursal=form.cleaned_data.get("sucursal"),
                    fecha_faltante=form.cleaned_data.get("fecha_faltante"),
                    num_cajera=form.cleaned_data.get("num_cajera"),
                    nombre_cajera=form.cleaned_data.get("nombre_cajera"),
                    num_boleta=form.cleaned_data.get("num_boleta"),
                    importe_faltante=form.cleaned_data.get("importe_faltante"),
                    comentario=form.cleaned_data.get("comentario"),

            )

            nuevo.save()
            return redirect("registro_quebrantos")


class RegistroErroresCreate(CreateView):
    model=Errores
    form_class=ErroresForm
    template_name= "form_registro_errores.html"

    def post(self, request, *args, **kwargs):
        user=request.user.username
        form=self.form_class(request.POST)

        if form.is_valid():
            nuevo=Errores(
                usuario=user,
                sucursal=form.cleaned_data.get("sucursal"),
                fecha_error=form.cleaned_data.get("fecha_error"),
                num_cajera=form.cleaned_data.get("num_cajera"),
                num_boleta=form.cleaned_data.get("num_boleta"),
                grupo=form.cleaned_data.get("grupo"),
                comentario=form.cleaned_data.get("comentario"),
            )
            nuevo.save()
            return redirect("registro_errores")

class RegistroRetopCreate(CreateView):
    model=PresRetop
    form_class=RetopForm
    template_name="form_registro_retop.html"

    def post(self,request,*args,**kwargs):
        user=request.user.username
        form=self.form_class(request.POST)

        if form.is_valid():
            nuevo=PresRetop(
                usuario=user,
                num_comercio=form.cleaned_data.get("num_comercio"),
                fecha_orden=form.cleaned_data.get("fecha_orden"),
                importe=form.cleaned_data.get("importe"),
                plan=form.cleaned_data.get("plan"),
            )
            nuevo.save()
            return redirect("registro_retop")


class RegistroPromotoraCreate(CreateView):
    model=PresPromotora
    form_class=PromotoraForm
    template_name="form_registro_promotora.html"

    def post(self,request,*args,**kwargs):
        user=request.user.username
        form=self.form_class(request.POST)

        if form.is_valid():
            nuevo=PresPromotora(
                usuario=user,
                num_orden=form.cleaned_data.get("num_orden"),
                fecha_orden=form.cleaned_data.get("fecha_orden"),
                importe=form.cleaned_data.get("importe"),
                plan=form.cleaned_data.get("plan"),
                promo=form.cleaned_data.get("promo"),
            )
            nuevo.save()
            return redirect("registro_promotora")


class RegistroCreditosDCreate(CreateView):
    model = PresCreditosD
    form_class = CreditosDForm
    template_name = "form_registro_creditos.html"

    def post(self, request, *args, **kwargs):
        user = request.user.username
        form = self.form_class(request.POST)

        if form.is_valid():
            nuevo = PresCreditosD(
                usuario=user,
                num_orden=form.cleaned_data.get("num_orden"),
                fecha_orden=form.cleaned_data.get("fecha_orden"),
                importe=form.cleaned_data.get("importe"),
                plan=form.cleaned_data.get("plan"),
            )
            nuevo.save()
            return redirect("registro_creditosD")
