from django.shortcuts import render,redirect
from datetime import datetime, date

#CRUD
from django.views.generic.detail import DetailView
from django.views.generic import ListView, UpdateView
from django.db.models import Q
#Modelos
from AdmCajasApp.models import Manuales
from CajasApp.models import *
from FormulariosApp.models import *
from AdministracionApp.models import Sucursales
from django.contrib.auth.mixins import LoginRequiredMixin



def cotiza_orden(request):
    fechaahora = datetime.now()
    reserva = datetime.strftime(fechaahora,'%m%d%H%M%S')
    error = {"Debe completar todos los campos": "error"}
    try:
        if request.method== "POST":
            datos_cotiza = request.POST

            importe_compra = datos_cotiza["importe_compra"]
            descuento_compra = datos_cotiza["descuento_compra"]
            cuotas_compra = datos_cotiza["cuotas_compra"]
            vendedor_compra = datos_cotiza["vendedor_compra"]
            articulos_compra = datos_cotiza["articulos_compra"]
            comentarios_compra = datos_cotiza["comentarios_compra"]

            imp_desc = (int(importe_compra)*int(descuento_compra))/100
            imp_cdesc = int(importe_compra)-int(imp_desc)
            imp_recargo = int(imp_cdesc)*(int(cuotas_compra)*2/100)
            tot_compra = int(imp_cdesc)+int(imp_recargo)
            imp_cuota = int(tot_compra)/int(cuotas_compra)
            fecha2 = datetime.now()
            fecha = datetime.strftime(fecha2, '%d/%m/%Y')



            return render(request, "cotiza_orden_res.html", {
            "importe_compra":importe_compra,
            "descuento_compra":descuento_compra,
            "cuotas_compra":cuotas_compra,
            "vendedor_compra":vendedor_compra,
            "articulos_compra":articulos_compra,
            "comentarios_compra":comentarios_compra,
            "imp_desc":imp_desc,
            "imp_cdesc":imp_cdesc,
            "imp_recargo":imp_recargo,
            "tot_compra":tot_compra,
            "imp_cuota":imp_cuota,
            "fecha":fecha,
            "reserva":reserva,
        })
    except:
        return render(request, "cotiza_orden.html",{"error":error})

    return render(request, "cotiza_orden.html",)

def orden_sin_cotizar(request):
    error = {"Debe completar todos los campos": "error"}
    try:
        if request.method == "POST":
            datos_cotiza = request.POST

            importe_compra = datos_cotiza["importe_compra"]
            importe_orden = datos_cotiza["importe_orden"]
            descuento_compra = datos_cotiza["descuento_compra"]
            cuotas_compra = datos_cotiza["cuotas_compra"]

            imp_desc = round((int(importe_compra)*int(descuento_compra))/100,0)
            imp_recargo = round(int(importe_orden)*int(cuotas_compra*2)/(int(cuotas_compra*2)+100),0)
            total_compra = round(int(importe_compra)-int(importe_orden)-int(imp_desc)+int(imp_recargo),0)
            
            if total_compra > 0:
                tot_compra = (f"Dif a pagar (SEÑA) $"+str(total_compra))
            else:
                tot_compra = (f"Importe a Favor $"+str(total_compra))

            return render(request, "orden_sin_cotizar_res.html", {
                "importe_compra": importe_compra,
                "importe_orden": importe_orden,
                "descuento_compra": descuento_compra,
                "cuotas_compra": cuotas_compra,
                "imp_recargo": imp_recargo,
                "imp_desc": imp_desc,
                "tot_compra": tot_compra,
            })
    except:
        return render(request, "orden_sin_cotizar.html", {"error": error})

    return render(request, "orden_sin_cotizar.html",)

def calcula_disponible(request):
    error = {"Debe completar todos los campos": "error"}
    try:
        if request.method == "POST":
            datos_cotiza = request.POST

            importe_orden = datos_cotiza["importe_orden"]
            cuotas_compra = datos_cotiza["cuotas_compra"]

            disponible = round((int(importe_orden)*100)/int(100+int(cuotas_compra*2)),2)
            imp_recargo = round(int(importe_orden)-int(disponible),2)
            

            return render(request, "calcula_disponible_res.html", {
                "importe_orden": importe_orden,
                "cuotas_compra": cuotas_compra,
                "imp_recargo": imp_recargo,
                "disponible": disponible,
            })
    except:
        return render(request, "calcula_disponible.html", {"error": error})

    return render(request, "calcula_disponible.html",)

def calcula_descuento(request):
    error = {"Debe completar todos los campos": "error"}
    try:
        if request.method == "POST":

            datos_desc = request.POST

            importe_compra = datos_desc["importe_compra"]
            monto_paga = datos_desc["monto_paga"]
            descuento_paga = datos_desc["descuento_paga"]
            descuento_dif = datos_desc["descuento_dif"]

            imp_desc = round(int(monto_paga) *
                            (int(descuento_paga)/(100-int(descuento_paga))), 2)
            imp_desc_dif = round(
                (int(importe_compra)-int(monto_paga)-int(imp_desc))*(int(descuento_dif)/100), 2)
            imp_dif = round(int(importe_compra)-int(monto_paga)-int(imp_desc), 2)
            tot_desc = round(int(imp_desc_dif)+int(imp_desc), 2)
            tot_venta = round(int(importe_compra)-int(tot_desc), 2)

            return render(request, 'desc_descuento_calculado.html', {
                "importe_compra": importe_compra,
                "monto_paga": monto_paga,
                "descuento_paga": descuento_paga,
                "descuento_dif": descuento_dif,
                "imp_desc": imp_desc,
                "imp_desc_dif": imp_desc_dif,
                "imp_dif": imp_dif,
                "tot_desc": tot_desc,
                "tot_venta": tot_venta,
            })
    except:
        return render(request, "desc_calcula_descuento.html",{"error":error})

    return render(request, "desc_calcula_descuento.html")

def retira_cliente(request):
    fechaahora = date.today()
    suc = Sucursales.objects.all()
    return render(request, "print_retira_cliente.html", {"fechaahora": fechaahora,"suc":suc})

def solicitud_credito(request):
    fechaahora = date.today()
    return render(request,"print_solicitud_credito.html",{"fechaahora":fechaahora})

def reserva_mercaderia(request):
    fechaahora = date.today()
    return render(request,"print_reserva_mercaderia.html",{"fechaahora":fechaahora})

def venta_paga(request):
    fechaahora = date.today()
    return render(request,"print_venta_paga.html",{"fechaahora":fechaahora})

def mercaderia_senada(request):
    fechaahora = date.today()
    return render(request,"print_mercaderia_senada.html",{"fechaahora":fechaahora})

def retira_vendedor(request):
    fechaahora = date.today()
    return render(request,"print_retira_vendedor.html",{"fechaahora":fechaahora})

def reclamo_manual(request):
    fechaahora = date.today()
    return render(request,"print_reclamo_manual.html",{"fechaahora":fechaahora})

def diferencia_caja(request):
    fechaahora = date.today()
    return render(request,"print_diferencia_caja.html",{"fechaahora":fechaahora})

def reclamos_print(request):
    fechaahora = date.today()
    return render(request,"print_reclamos.html",{"fechaahora":fechaahora})


def manuales(request):
    manuales = Manuales.objects.all()
    return render(request, "manual_list.html", {"manuales": manuales})

class ManualesDetail(LoginRequiredMixin, DetailView):
    model = Manuales
    template_name = 'CajasApp/manual.html'

def pedidos_lista(request):
    return render(request, "pedidos_list.html")

def cheque_uniforme(request):
    fechaahora = date.today()
    return render(request,"print_cheque_uniforme.html",{"fechaahora":fechaahora})    


#------------Modulo Creditel - Credito de la casa---------------------------------------

class ValeCreditelCdelaCasaList(ListView):

    model = ValeCreditelCdelaCasa
    template_name = "CajasApp/list_vale_creditel.html"

    def get(self, request, *args, **kwargs):        
        user = request.user
        filtro = ValeCreditelCdelaCasa.objects.filter(estado=True).order_by('ci_cliente')
        queryset=request.GET.get("buscar")
        if queryset:
            filtro = ValeCreditelCdelaCasa.objects.filter(
                Q(ci_cliente=queryset),
                Q(estado=True)
            )            

        return render(request, self.template_name, {"filtro": filtro})



def edicion_vale_creditel(request, id):
    user=request.user.username
    form=ValeCreditelCdelaCasa.objects.get(id=id)
 
    return render(request,"update_vale_creditel.html",{"form":form})

def editar_vale_creditel(request):
    user = request.user.username
    id = int(request.POST['id'])
    ci_cliente=request.POST['ci_cliente']
    nombre_cliente=request.POST['nombre_cliente']
    empresa_cliente=request.POST['empresa_cliente']
    importe_cliente=request.POST['importe_cliente']
    fpago_cliente=request.POST['fpago_cliente']

    num_cajera = request.POST['num_cajera']
    num_vta = request.POST['num_vta']
    num_dev = request.POST['num_dev']
    imp_facturado = request.POST['imp_facturado']
    num_seña = request.POST['num_seña']
    comentarios = request.POST['comentarios']

    editar = ValeCreditelCdelaCasa.objects.get(id=id)
    editar.usuario=user
    editar.estado=False
    editar.ci_cliente=ci_cliente
    editar.nombre_cliente=nombre_cliente
    editar.empresa_cliente=empresa_cliente
    editar.importe_cliente=importe_cliente
    editar.fpago_cliente=fpago_cliente
    editar.num_cajera=num_cajera
    editar.num_vta=num_vta
    editar.num_dev = num_dev
    editar.imp_facturado = imp_facturado
    editar.num_seña = num_seña
    editar.comentarios = comentarios
    editar.save()
    return redirect("inicio")



#------------Modulo Correo Uruguayo-----------------------------------------------
class ValeCorreoList(ListView):

    model = ValeCorreo
    template_name = "CajasApp/list_vale_correo.html"

    def get(self, request, *args, **kwargs):        
        user = request.user
        filtro = ValeCorreo.objects.filter(estado=True).order_by('ci_cliente')
        queryset=request.GET.get("buscar")
        if queryset:
            filtro = ValeCorreo.objects.filter(
                Q(ci_cliente=queryset),
                Q(estado=True)
            )            

        return render(request, self.template_name, {"filtro": filtro})


def edicion_vale_correo(request, id):
    user = request.user.username
    form = ValeCorreo.objects.get(id=id)

    return render(request, "update_vale_correo.html", {"form": form})


def editar_vale_correo(request):
    user = request.user.username
    id = int(request.POST['id'])
    ci_cliente = request.POST['ci_cliente']
    nombre_cliente = request.POST['nombre_cliente']
    genero_cliente = request.POST['genero_cliente']
    importe_cliente = request.POST['importe_cliente']

    num_cajera = request.POST['num_cajera']
    num_vta = request.POST['num_vta']
    num_dev = request.POST['num_dev']
    comentarios = request.POST['comentarios']

    editar = ValeCorreo.objects.get(id=id)
    editar.usuario = user
    editar.estado = False
    editar.genero_cliente = genero_cliente
    editar.ci_cliente = ci_cliente
    editar.nombre_cliente = nombre_cliente
    editar.importe_cliente = importe_cliente
    editar.num_cajera = num_cajera
    editar.num_vta = num_vta
    editar.num_dev = num_dev
    editar.comentarios = comentarios
    editar.save()
    return redirect("inicio")
