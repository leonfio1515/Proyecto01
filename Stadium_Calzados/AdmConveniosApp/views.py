from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q
from .models import *
from datetime import datetime
# Create your views here.


#------------Modulo Correo Uruguayo-----------------------------------------------
class CobranzasConveniosList(ListView):

    model = CobranzasConvenios
    template_name = "Convenios/list_cobranzas_convenios.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        filtro = CobranzasConvenios.objects.filter(estado=True).order_by('medio_pago')
        queryset = request.GET.get("buscar")
        if queryset:
            filtro = CobranzasConvenios.objects.filter(
                Q(medio_pago__icontains=queryset),
                Q(estado=True)
            )

        return render(request, self.template_name, {"filtro": filtro})


def edicion_cobranzas_convenios(request, id):
    user = request.user.username
    form = CobranzasConvenios.objects.get(id=id)

    return render(request, "update_cobranzas_convenios.html", {"form": form})


def editar_cobranzas_convenios(request):
    user = request.user.username
    id = int(request.POST['id'])
    mes_cobro = request.POST['mes_cobro']
    fecha_corte = request.POST['fecha_corte']
    num_empresa = request.POST['num_empresa']
    nombre_empresa = request.POST['nombre_empresa']
    mes_resumen = request.POST['mes_resumen']
    imp_resumen = request.POST['imp_resumen']
    imp_bonificacion = request.POST['imp_bonificacion']
    num_documento = request.POST['num_documento']
    imp_resguardo = request.POST['imp_resguardo']
    imp_recargo = request.POST['imp_recargo']
    imp_cobrar = request.POST['imp_cobrar']
    medio_pago = request.POST['medio_pago']

    sap_banco = request.POST['sap_banco']
    sap_convenios = request.POST['sap_convenios']
    imp_pago = request.POST['imp_pago']
    fecha_pago = request.POST['fecha_pago']


    editar = CobranzasConvenios.objects.get(id=id)
    editar.usuario = user
    editar.estado = False
    editar.mes_cobro = mes_cobro
    editar.fecha_corte = fecha_corte
    editar.num_empresa = num_empresa
    editar.nombre_empresa = nombre_empresa
    editar.mes_resumen = mes_resumen
    editar.imp_resumen = imp_resumen
    editar.imp_bonificacion = imp_bonificacion
    editar.num_documento = num_documento
    editar.imp_resguardo = imp_resguardo
    editar.imp_recargo = imp_recargo
    editar.imp_cobrar = imp_cobrar
    editar.medio_pago = medio_pago

    editar.sap_banco = sap_banco
    editar.sap_convenios = sap_convenios
    editar.imp_pago = imp_pago
    editar.fecha_pago = fecha_pago
    editar.save()
    return redirect("inicio")
