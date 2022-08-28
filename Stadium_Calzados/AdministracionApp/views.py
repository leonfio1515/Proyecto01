from django.shortcuts import render, redirect
from FormulariosApp.models import *
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
# Create your views here.


class Mensaje(CreateView):
    model = Mensajes
    form_class = MensajeForm
    template_name = "sugerencias.html"

    def post(self, request, *args, **kwargs):
        user = request.user.username
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo = Mensajes(
                usuario=user,
                nombre=form.cleaned_data.get("nombre"),
                asunto=form.cleaned_data.get("asunto"),
                mensaje=form.cleaned_data.get("mensaje"),
            )
            nuevo.save()
            return redirect("inicio")

def noticias(request):
    noticias = Noticias.objects.all().order_by('-fecha_noticia')

    return render(request, "noticias.html",{"noticias":noticias})


class NoticiasDetail(DetailView):

    model = Noticias
    template_name = "AdministracionApp/noticias_detail.html"
