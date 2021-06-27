from django.shortcuts import render
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from core.models import Encuest
# Create your views here.

def home(request):
    return render(request, "core/home.html")

def login(request):
    return render(request, "core/login.html")

def graficas(request):
    return render(request, "core/graficas.html")

def test(request):
    return render(request, "core/test.html")

def tablas(request):
    return render(request, "core/tablas.html")    

def edicion(request):
    return render(request, "core/edicion.html") 

# def base(request):
#     return render(request, "core/base.html")

def encuesta_list(request):
    data = {
        'title': 'Listado',
        'encuestas': Encuest.objects.all()
    }
    return render(request, 'core/list.html', data)