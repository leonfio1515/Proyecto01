from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('mensaje', login_required(Mensaje.as_view()), name='mensaje'),
    path('noticias', noticias, name='noticias'),
    path(r'noticias_detail^(?P<pk>\d+)$',
         NoticiasDetail.as_view(), name="noticias_detail"),

]
