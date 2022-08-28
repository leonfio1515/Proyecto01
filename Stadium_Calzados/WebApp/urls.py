from django.urls import path
from .views import *


urlpatterns = [
    path('cancelaciones_carga', VCargarCancelaciones, name='cancelaciones_carga'),
    path('cambiosML', VCargarCambiosML, name='cambiosML'),

]
