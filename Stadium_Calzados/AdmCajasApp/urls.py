from django.urls import path
from .views import *


urlpatterns = [
    path('registro_errores', RegistroErroresCreate.as_view(), name='registro_errores'),
    path('registro_quebrantos', RegistroQuebrantosCreate.as_view(),
         name='registro_quebrantos'),

    path('registro_retop', RegistroRetopCreate.as_view(),
         name='registro_retop'),
    path('registro_promotora', RegistroPromotoraCreate.as_view(),
         name='registro_promotora'),
    path('registro_creditosD', RegistroCreditosDCreate.as_view(),
         name='registro_creditosD'),

]
