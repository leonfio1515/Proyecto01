from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
#Terminado
    path('cotiza_orden', cotiza_orden, name="cotiza_orden"),
    path('orden_sin_cotizar', orden_sin_cotizar, name="orden_sin_cotizar"),
    path('calcula_disponible', calcula_disponible, name="calcula_disponible"),

    path('calcula_descuento', calcula_descuento, name="calcula_descuento"),
    path('resultado_descuento', calcula_descuento, name="resultado_descuento"),

#Doc impresion
    path('cheque_uniforme', cheque_uniforme, name="cheque_uniforme"),
    path('retira_cliente', retira_cliente, name="retira_cliente"),
    path('solicitud_credito', solicitud_credito, name="solicitud_credito"),
    path('reserva_mercaderia', reserva_mercaderia, name="reserva_mercaderia"),
    path('venta_paga', venta_paga, name="venta_paga"),
    path('mercaderia_senada', mercaderia_senada, name="mercaderia_senada"),
    path('retira_vendedor', retira_vendedor, name="retira_vendedor"),
    path('reclamo_manual', reclamo_manual, name="reclamo_manual"),
    path('diferencia_caja', diferencia_caja, name="diferencia_caja"),
    path('reclamos_print', reclamos_print, name="reclamos_print"),


    path('lista_manuales', manuales, name="lista_manuales"),
    path(r'manual_detalle/^(?P<pk>\d+)$', ManualesDetail.as_view(), name ="manual_detalle"),
    path('pedidos_lista', login_required(pedidos_lista), name="pedidos_lista"),

    path('vale_creditel_cdelacasa', login_required(
        ValeCreditelCdelaCasaList.as_view()), name="vale_creditel_cdelacasa"),
    path(r'vale_creditel_update/<int:id>',
         edicion_vale_creditel, name='vale_creditel_update'),
    path(r'vale_creditel_guarda',
         editar_vale_creditel, name='vale_creditel_guarda'),

    path('vale_correo', login_required(
        ValeCorreoList.as_view()), name="vale_correo"),
    path(r'vale_correo_update/<int:id>',
         edicion_vale_correo, name='vale_correo_update'),
    path(r'vale_correo_guarda',
         editar_vale_correo, name='vale_correo_guarda'),

]
