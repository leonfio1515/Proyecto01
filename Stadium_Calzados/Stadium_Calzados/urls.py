from django.contrib import admin
from django.urls import path, include

from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_request, name='login'),
    path('inicio', login_required(inicio), name='inicio'),
    path('logout', logout_request, name='logout'),
    path('Stadium/cajas/', include('CajasApp.urls')),
    path('Stadium/formularios/', include('FormulariosApp.urls')),
    path('Stadium/web/', include('WebApp.urls')),
    path('Stadium/admCajas/', include('AdmCajasApp.urls')),
    path('Stadium/adm/', include('AdministracionApp.urls')),
    path('Stadium/covenios/', include('AdmConveniosApp.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)