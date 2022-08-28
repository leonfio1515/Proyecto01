from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('descuentos', login_required(descuentos), name="descuentos"),
    path('reparaciones_create', login_required(reparaciones),
         name="reparaciones_create"),
   
    #Create
    path('bolsas_create', login_required(BolsasCreate.as_view()), name='bolsas_create'),
    path('diseno_create', login_required(DisenoCreate.as_view()), name='diseno_create'),
    path('faramcia_create', login_required(FarmaciaCreate.as_view()),name='farmacia_create'),
    path('limpieza_create', login_required(LimpiezaCreate.as_view()),name='limpieza_create'),
    path('papeleria_create', login_required(PapeleriaCreate.as_view()),name='papeleria_create'),
    path('luces_create', login_required(lucescreate), name='luces_create'),
    path('pedido_cambio', login_required(pedido_cambio), name='pedido_cambio'),
    path('pedido_uniforme', login_required(pedido_uniforme), name='pedido_uniforme'),
    path('vale_conrad', login_required(vale_conrad), name='vale_conrad'),
    path('vale_apmu', login_required(vale_apmu), name='vale_apmu'),
    path('cheque_uniforme', login_required(cheque_uniforme), name='cheque_uniforme'),


#CRUD PEDIDOS

#List
    path('bolsas_list', login_required(BolsasList.as_view()), name="bolsas_list"),
    path('diseno_list', login_required(DisenoList.as_view()), name="diseno_list"),
    path('farmacia_list', login_required(FarmaciaList.as_view()), name="farmacia_list"),
    path('limpieza_list', login_required(LimpiezaList.as_view()), name="limpieza_list"),
    path('luces_list', login_required(LucesList.as_view()), name="luces_list"),
    path('papeleria_list', login_required(PapeleriaList.as_view()), name="papeleria_list"),
    path('reparaciones_list', login_required(ReparacionesList.as_view()), name="reparaciones_list"),
    path('mensajes_list', login_required(MensajesList.as_view()), name="mensajes_list"),
    path('cambio_list', login_required(CambioList.as_view()), name="cambio_list"),
    path('descuentos_list', login_required(DescuentosList.as_view()), name="descuentos_list"),
    path('cheque_uniforme_list', login_required(ChequeUniformeList.as_view()), name="cheque_uniforme_list"),


#Detail
    path(r'bolsas_detail^(?P<pk>\d+)$', login_required(BolsasDetail.as_view()), name="bolsas_detail"),
    path(r'diseno_detail^(?P<pk>\d+)$', login_required(DisenoDetail.as_view()), name="diseno_detail"),
    path(r'farmacia_detail^(?P<pk>\d+)$', login_required(FarmaciaDetail.as_view()), name="farmacia_detail"),
    path(r'limpieza_detail^(?P<pk>\d+)$', login_required(LimpiezaDetail.as_view()), name="limpieza_detail"),
    path(r'luces_detail^(?P<pk>\d+)$', login_required(LucesDetail.as_view()), name="luces_detail"),
    path(r'papeleria_detail^(?P<pk>\d+)$',
         login_required(PapeleriaDetail.as_view()), name="papeleria_detail"),
    path(r'reparaciones_detail^(?P<pk>\d+)$', login_required(ReparacionesDetail.as_view()), name="reparaciones_detail"),
    path(r'mensajes_detail^(?P<pk>\d+)$', login_required(MensajesDetail.as_view()), name="mensajes_detail"),
    path(r'cambio_detail^(?P<pk>\d+)$', login_required(CambioDetail.as_view()), name="cambio_detail"),
    path(r'cheque_uniforme_detail^(?P<pk>\d+)$', login_required(ChequeUniformeDetail.as_view()), name="cheque_uniforme_detail"),


]
