from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from ArticulosApp.models import Noticias
from datetime import date, timedelta
from AdministracionApp.models import Promociones

def login_request(request):
    user=request.user

    if user.is_authenticated:
        return redirect("inicio")

    else:
        if request.method=="POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect("inicio")
            
                else:
                    return render(request, "login.html", {"form":form,"mensaje":"Error"})
        
            else:
                return render(request, "login.html", {"form":form, "mensaje": "Error"})

        form = AuthenticationForm()
        return render(request, "login.html", {"form":form})


def inicio(request):
    dia_dif = timedelta(days=-30)
    fechahasta = date.today()
    fechadesde = fechahasta+ dia_dif

    noticias = Noticias.objects.filter(fecha_noticia__gte=fechadesde).order_by('-fecha_noticia')
    promo = Promociones.objects.filter(estado_promo=True).order_by('-fecha_fin')

    return render(request, "inicio.html",{"noticias":noticias,"promo":promo})


def logout_request(request):
    logout(request)
    return redirect("login")

