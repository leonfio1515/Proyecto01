from django.shortcuts import render,redirect
from datetime import datetime
from AdministracionApp.models import *
from .models import *
# Create your views here.

def VCargarCancelaciones(request):
    medio = MediosPago.objects.all()
    plataforma = Plataforma.objects.all()
    motivo = MotivoDev.objects.all()
    fecha = datetime.now()
    user = request.user.username
    error = {"Algo salio mal, contactese con el administrador": "error"}

    try:
        if request.method == "POST":
            form_cancelacion = request.POST

            cancelacion = CancelacionCliente(
                usuario=user,
                Fecha=fecha,
                Nombre=form_cancelacion["Nombre"],
                CI=form_cancelacion["CI"],
                Plataforma=form_cancelacion["Plataforma"],
                Medio_pago=form_cancelacion["Medio_pago"],
                Pedido=form_cancelacion["Pedido"],
                Fecha_cancela=form_cancelacion["Fecha_cancela"],
                Fecha_recibido=form_cancelacion["Fecha_recibido"],
                Importe=form_cancelacion["Importe"],
                Motivo=form_cancelacion["Motivo"],
                Comentario=form_cancelacion["Comentario"],
            )

            cancelacion.save()
            return redirect("inicio")
        else:
                form_cancelacion = ()
    except:
        return render(request, "form_cancelaciones.html", {"medio": medio, "plataforma": plataforma, "motivo": motivo, "error": error})

    return render(request,"form_cancelaciones.html",{"medio":medio,"plataforma":plataforma,"motivo":motivo})

def VCargarCambiosML(request):
    fecha = datetime.now()
    user = request.user.username
    error = {"Algo salio mal, contactese con el administrador": "error"}

    try:
        if request.method == "POST":
            form_cambio = request.POST

            cambio = CambiosML(
                usuario=user,
                Fecha=fecha,
                Nombre=form_cambio["Nombre"],
                CI=form_cambio["CI"],
                Pedido=form_cambio["Pedido"],
                Fecha_compra=form_cambio["Fecha_compra"],
                Importe=form_cambio["Importe"],
                Comentario=form_cambio["Comentario"],
            )

            cambio.save()
            return redirect("inicio")
        else:
            form_cambio = ()
    except:
        return render(request, "form_cambiosML.html", {"error": error})

    return render(request,"form_cambiosML.html")

def VPaquetesRecibidos(request):
    pass