from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('cobranzas_convenios', login_required(
        CobranzasConveniosList.as_view()), name="cobranzas_convenios"),
    path(r'cobranzas_convenios_update/<int:id>',
         edicion_cobranzas_convenios, name='cobranzas_convenios_update'),
    path(r'cobranzas_convenios_guarda',
         editar_cobranzas_convenios, name='cobranzas_convenios_guarda'),
]