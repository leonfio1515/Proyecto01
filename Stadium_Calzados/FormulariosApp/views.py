from django.shortcuts import render, redirect
from datetime import timedelta, date

#Models y forms
from .models import *
from FormulariosApp.forms import *
from AdministracionApp.models import Mensajes

#CRUD
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.

def descuentos(request):

    user = request.user

    if request.method =="POST":
        form_descuentos=request.POST

        descuentos = Descuentos(
            usuario=user,
            nombre_descuento=form_descuentos["nombre_descuento"],
            fecha_descuento=form_descuentos["fecha_descuento"],
            valor_descuento=form_descuentos["valor_descuento"],
        )

        descuentos.save()
        return redirect("inicio")

    else:
        form_descuentos = ()

    return render(request,'form_descuentos.html')

def reparaciones(request):

    user = request.user

    if request.method =="POST":
        form_repara=request.POST

        repara = PedidoReparaciones(
            usuario=user,
            Servicio=form_repara["Servicio"],
            Asunto=form_repara["Asunto"],
            Comentario=form_repara["Comentario"],
        )

        repara.save()
        return redirect("inicio")

    else:
        form_repara = ()

    return render(request,'pedidoreparaciones_form.html')

#CRUD CreateView
class BolsasCreate(CreateView):
    model = PedidoBolsas
    form_class = BolsasForm
    template_name="pedidobolsas_form.html"

    def post(self, request,*args,**kwargs):
        user = request.user.username
        form=self.form_class(request.POST)
        if form.is_valid():
            nuevo=PedidoBolsas(
                usuario = user,
                Bolsa_chica=form.cleaned_data.get("Bolsa_chica"),
                Bolsa_media=form.cleaned_data.get("Bolsa_media"),
                Bolsa_grande=form.cleaned_data.get("Bolsa_grande"),
            )
            nuevo.save()
            return redirect("inicio")
   
class DisenoCreate(CreateView):
    model = PedidoDiseno
    form_class = DisenoForm
    template_name="pedidodiseno_form.html"

    def post(self, request, *args, **kwargs):
        user = request.user.username
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo = PedidoDiseno(
                usuario=user,
                Tarjeta_presentacion=form.cleaned_data.get(
                    "Tarjeta_presentacion"),
                Tarjeta_atencion=form.cleaned_data.get("Tarjeta_atencion"),
                Talon_cambio=form.cleaned_data.get("Talon_cambio"),
            )
            nuevo.save()
            return redirect("inicio")

class FarmaciaCreate(CreateView):
    model = PedidoFarmacia
    form_class = FarmaciaForm
    template_name="pedidofarmacia_form.html"

    def post(self, request, *args, **kwargs):
        user = request.user.username
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo = PedidoFarmacia(
                usuario=user,
                Ibuprofeno=form.cleaned_data.get(
                    "Ibuprofeno"),
                Leuco=form.cleaned_data.get("Leuco"),
                Iodofon=form.cleaned_data.get("Iodofon"),
                Gasa=form.cleaned_data.get("Gasa"),
                Disan=form.cleaned_data.get("Disan"),
                Curitas=form.cleaned_data.get("Curitas"),
                Algodon=form.cleaned_data.get("Algodon"),
                Alcohol_rectificado=form.cleaned_data.get(
                    "Alcohol_rectificado"),
                Alcohol_gel=form.cleaned_data.get("Alcohol_gel"),
                Agua_oxigenada=form.cleaned_data.get("Agua_oxigenada"),
            )
            nuevo.save()
            return redirect("inicio")

class LimpiezaCreate(CreateView):
    model = PedidoLimpieza
    form_class = LimpiezaForm
    template_name="pedidolimpieza_form.html"

    def post(self, request, *args, **kwargs):
        user = request.user.username
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo = PedidoLimpieza(
                usuario=user,
                Plumero=form.cleaned_data.get(
                    "Ibuprofeno"),
                Insecticida=form.cleaned_data.get("Insecticida"),
                Pulidor_cremoso=form.cleaned_data.get("Pulidor_cremoso"),
                Perfumol=form.cleaned_data.get("Perfumol"),
                PH=form.cleaned_data.get("PH"),
                Panos_piso=form.cleaned_data.get("Panos_piso"),
                Limpia_vidrio=form.cleaned_data.get("Limpia_vidrio"),
                Hipoclorito=form.cleaned_data.get(
                    "Hipoclorito"),
                Jabon_liq=form.cleaned_data.get("Jabon_liq"),
                Franela=form.cleaned_data.get("Franela"),
                Esponja=form.cleaned_data.get("Esponja"),
                Detergente=form.cleaned_data.get("Detergente"),
                Cera_roja=form.cleaned_data.get("Cera_roja"),
                Cera_incolora=form.cleaned_data.get("Cera_incolora"),
                Bolsas=form.cleaned_data.get("Bolsas"),
                Lustramueble=form.cleaned_data.get("Lustramueble"),
                Des_ambiente=form.cleaned_data.get("Des_ambiente"),
            )
            nuevo.save()
            return redirect("inicio")

class PapeleriaCreate(CreateView):
    model = PedidoPapeleria
    form_class = PapeleriaForm
    template_name="pedidopapeleria_form.html"

    def post(self, request,*args,**kwargs):
        user = request.user.username
        form=self.form_class(request.POST)
        if form.is_valid():
            nuevo=PedidoPapeleria(
                usuario = user,
                Lapiceras=form.cleaned_data.get("Lapiceras"),
                Clips=form.cleaned_data.get("Clips"),
                Lapiz=form.cleaned_data.get("Lapiz"),
                Lapicera_mostrador=form.cleaned_data.get("Lapicera_mostrador"),
                Cinta_fina_1=form.cleaned_data.get("Cinta_fina_1"),
                Cinta_fina_2=form.cleaned_data.get("Cinta_fina_2"),
                Cinta_anchaT=form.cleaned_data.get("Cinta_anchaT"),
                Cinta_impresa=form.cleaned_data.get("Cinta_impresa"),
                Etiqueta_60X40=form.cleaned_data.get("Etiqueta_60X40"),
                Marcador_perm_fino=form.cleaned_data.get("Marcador_perm_fino"),
                Marcador_fluor=form.cleaned_data.get("Marcador_fluor"),
                Medias=form.cleaned_data.get("Medias"),
                Grapas=form.cleaned_data.get("Grapas"),
                PilasAA=form.cleaned_data.get("PilasAA"),
                PilasAAA=form.cleaned_data.get("PilasAAA"),
                Precinto_cajon=form.cleaned_data.get("Precinto_cajon"),
                Precinto_sobre=form.cleaned_data.get("Precinto_sobre"),
                ResmaA4=form.cleaned_data.get("ResmaA4"),
                Resma_otro=form.cleaned_data.get("Resma_otro"),
                Ribbon=form.cleaned_data.get("Ribbon"),
                Rollo_calc=form.cleaned_data.get("Rollo_calc"),
                Rollo_fact=form.cleaned_data.get("Rollo_fact"),
                Sobre_carta=form.cleaned_data.get("Sobre_carta"),
                Tinta_calc=form.cleaned_data.get("Tinta_calc"),
                Hilos=form.cleaned_data.get("Hilos"),
                Pistola=form.cleaned_data.get("Pistola"),
                Trincheta=form.cleaned_data.get("Trincheta"),
                Tijera=form.cleaned_data.get("Tijera"),
                Etiqueta_60X150=form.cleaned_data.get("Etiqueta_60X150"),
                Goma=form.cleaned_data.get("Goma"),
                Banda_elastica=form.cleaned_data.get("Banda_elastica"),
                Marcador_perm_grueso=form.cleaned_data.get("Marcador_perm_grueso"),
                Carpeta=form.cleaned_data.get("Carpeta"),
                Tinta_sello=form.cleaned_data.get("Tinta_sello"),
                Grapadora=form.cleaned_data.get("Grapadora"),
                Etiqueta_color=form.cleaned_data.get("Etiqueta_color"),
            )
            nuevo.save()
            return redirect("inicio")


def lucescreate(request):
    user = request.user
    luces_object = Luces.objects.all()

    if request.method == "POST":
        form_luces = request.POST

        luces = PedidoLuces(
            usuario=user,
            AR111=form_luces["AR111"],
            Dicroica_led=form_luces["Dicroica Led"],
            Driver=form_luces["Driver Tachos"],
            EMB=form_luces["Emb Rec Led 35W"],
            Lampara=form_luces["Lampara"],
            Par30_calida=form_luces["Par 30 Luz calida"],
            Par30_fria=form_luces["Par 30 Luz fria"],
            Tacho=form_luces["Tachos"],
            Tubo_led=form_luces["Tubo Led"],
        )

        luces.save()
        return redirect("inicio")

    else:
        form_luces = ()

    return render(request, 'pedidoluces_form.html',{"luces_object":luces_object})


def pedido_cambio(request):
    user=request.user

    if request.method =="POST":
        form_cambio=request.POST

        cambio=PedidoCambio(
            usuario=user,
            monedas_1=form_cambio["1$"],
            monedas_2=form_cambio["2$"],
            monedas_5=form_cambio["5$"],
            monedas_10=form_cambio["10$"],
            billetes_20=form_cambio["20$"],
            billetes_50=form_cambio["50$"],
            billetes_100=form_cambio["100$"],
            billetes_200=form_cambio["200$"],
        )
        cambio.save()
        return redirect("inicio")

    else:
        form_cambio=()
    return render(request,"form_pedido_cambio.html")

def pedido_uniforme(request):
    user = request.user

    if request.method == "POST":
        form_uniforme = request.POST

        nuevo = PedidoUniforme(
            usuario=user,
            num_fun=form_uniforme["num_fun"],
            ci_fun=form_uniforme["ci_fun"],
            talle_camisa=form_uniforme["talle_camisa"],
            talle_pantalon=form_uniforme["talle_pantalon"],
            talle_abrigo=form_uniforme["talle_abrigo"],
            area_trabajo=form_uniforme["area_trabajo"],
            sexo=form_uniforme["sexo"],
        )
        nuevo.save()
        return redirect("pedido_uniforme")

    else:
        form_uniforme = ()
    return render(request, "form_uniforme_personal.html")


def vale_conrad(request):
    user = request.user

    if request.method == "POST":
        form_conrad = request.POST

        nuevo = ValeConrad(
            usuario=user,
            fecha_vta=form_conrad["fecha_vta"],
            num_vale=form_conrad["num_vale"],
            nombre_fun=form_conrad["nombre_fun"],
            num_vta=form_conrad["num_vta"],
            num_dev=form_conrad["num_dev"],
        )
        nuevo.save()
        return redirect("vale_conrad")

    else:
        form_conrad = ()
    return render(request, "form_vale_conrad.html")


def vale_apmu(request):
    user = request.user

    if request.method == "POST":
        form_apmu = request.POST

        nuevo = ValeApmu(
            usuario=user,
            num_vale=form_apmu["num_vale"],
            nombre_fun=form_apmu["nombre_fun"],
            apellido_fun=form_apmu["apellido_fun"],
            num_fun=form_apmu["num_fun"],
            fecha_vta=form_apmu["fecha_vta"],
            num_dev=form_apmu["num_dev"],
            comentarios=form_apmu["comentarios"],
        )
        nuevo.save()
        return redirect("vale_apmu")

    else:
        form_apmu = ()
    return render(request, "form_vale_apmu.html")


def cheque_uniforme(request):
    user = request.user

    if request.method == "POST":
        form_cheque = request.POST

        nuevo = ChequeUniforme(
            usuario=user,
            ci_fun=form_cheque["ci_fun"],
            num_fun=form_cheque["num_fun"],
            nombre_fun=form_cheque["nombre_fun"],
            cargo_fun=form_cheque["cargo_fun"],
            articulo=form_cheque["articulo"],
            comentarios=form_cheque["comentarios"],
        )
        nuevo.save()
        return redirect("cheque_uniforme")

    else:
        form_cheque = ()
    return render(request, "form_cheque_uniforme.html")



#CRUD ListView
class BolsasList(ListView):

    model = PedidoBolsas
    template_name = "CajasApp/list_bolsas.html"

    def get(self,request,*args,**kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = PedidoBolsas.objects.filter(
            usuario=user, Fecha_pedido__gte=fechadesde).order_by('-Fecha_pedido')

        return render(request, self.template_name, {"filtro":filtro})

class DisenoList(ListView):

    model = PedidoDiseno
    template_name = "CajasApp/list_diseno.html"

    def get(self, request, *args, **kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = PedidoDiseno.objects.filter(
            usuario=user, Fecha_pedido__gte=fechadesde).order_by('-Fecha_pedido')

        return render(request, self.template_name, {"filtro": filtro})

class FarmaciaList(ListView):

    model = PedidoFarmacia
    template_name = "CajasApp/list_farmacia.html"

    def get(self, request, *args, **kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = PedidoFarmacia.objects.filter(
            usuario=user, Fecha_pedido__gte=fechadesde).order_by('-Fecha_pedido')

        return render(request, self.template_name, {"filtro": filtro})

class LimpiezaList(ListView):

    model = PedidoLimpieza
    template_name = "CajasApp/list_limpieza.html"

    def get(self, request, *args, **kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = PedidoLimpieza.objects.filter(
            usuario=user, Fecha_pedido__gte=fechadesde).order_by('-Fecha_pedido')

        return render(request, self.template_name, {"filtro": filtro})

class LucesList(ListView):

    model = PedidoLuces
    template_name = "CajasApp/list_luces.html"

    def get(self, request, *args, **kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = PedidoLuces.objects.filter(
            usuario=user, Fecha_pedido__gte=fechadesde).order_by('-Fecha_pedido')

        return render(request, self.template_name, {"filtro": filtro})

class PapeleriaList(ListView):

    model = PedidoPapeleria
    template_name = "CajasApp/list_papeleria.html"

    def get(self, request, *args, **kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = PedidoPapeleria.objects.filter(
            usuario=user, Fecha_pedido__gte=fechadesde).order_by('-Fecha_pedido')

        return render(request, self.template_name, {"filtro": filtro})

class ReparacionesList(ListView):

    model = PedidoReparaciones
    template_name = "CajasApp/list_reparaciones.html"

    def get(self, request, *args, **kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = PedidoReparaciones.objects.filter(
            usuario=user, Fecha_pedido__gte=fechadesde).order_by('-Fecha_pedido')

        return render(request, self.template_name, {"filtro": filtro})

class MensajesList(ListView):

    model = Mensajes
    template_name = "CajasApp/list_mensajes.html"

    def get(self, request, *args, **kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = Mensajes.objects.filter(
            usuario=user, fecha_creado__gte=fechadesde).order_by('-fecha_creado')

        return render(request, self.template_name, {"filtro": filtro})


class CambioList(ListView):

    model = PedidoCambio
    template_name = "CajasApp/list_cambio.html"

    def get(self, request, *args, **kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = PedidoCambio.objects.filter(
            usuario=user, fecha_pedido__gte=fechadesde).order_by('-fecha_pedido')

        return render(request, self.template_name, {"filtro": filtro})

class DescuentosList(ListView):

    model = Descuentos
    template_name = "CajasApp/list_descuentos.html"

    def get(self, request, *args, **kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = Descuentos.objects.filter(
            usuario=user, fecha_creado__gte=fechadesde).order_by('-fecha_creado')

        return render(request, self.template_name, {"filtro": filtro})


class ChequeUniformeList(ListView):

    model = ChequeUniforme
    template_name = "CajasApp/list_cheque_uniforme.html"

    def get(self, request, *args, **kwargs):
        dia_dif = timedelta(days=-180)
        fechahasta = date.today()
        fechadesde = fechahasta + dia_dif
        user = request.user
        filtro = ChequeUniforme.objects.filter(
            usuario=user, fecha_registro__gte=fechadesde).order_by('-fecha_registro')

        return render(request, self.template_name, {"filtro": filtro})



#CRUD DetailView
class BolsasDetail(DetailView):

    model = PedidoBolsas
    template_name = "CajasApp/detail_bolsas.html"

class DisenoDetail(DetailView):

    model = PedidoDiseno
    template_name = "CajasApp/detail_diseno.html"

class FarmaciaDetail(DetailView):

    model = PedidoFarmacia
    template_name = "CajasApp/detail_farmacia.html"

class LimpiezaDetail(DetailView):

    model = PedidoLimpieza
    template_name = "CajasApp/detail_limpieza.html"

class LucesDetail(DetailView):

    model = PedidoLuces
    template_name = "CajasApp/detail_luces.html"

class PapeleriaDetail(DetailView):

    model = PedidoPapeleria
    template_name = "CajasApp/detail_papeleria.html"

class ReparacionesDetail(DetailView):

    model = PedidoReparaciones
    template_name = "CajasApp/detail_reparaciones.html"

class MensajesDetail(DetailView):

    model = Mensajes
    template_name = "CajasApp/detail_mensajes.html"

class CambioDetail(DetailView):

    model = PedidoCambio
    template_name = "CajasApp/detail_cambio.html"

class ChequeUniformeDetail(DetailView):

    model = ChequeUniforme
    template_name = "CajasApp/detail_cheque_uniforme.html"
