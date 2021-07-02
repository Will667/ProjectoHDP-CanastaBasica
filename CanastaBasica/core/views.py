from django.forms.forms import Form
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from .models import Departaments, Encuest
from .forms import EncuestForm
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

def test_list(request):
    data = {
        'title': 'Listado',
        'encuestas': Encuest.objects.all()
    }
    return render(request, 'core/testlist.html', data)

def test_view(request):
    if request.method == 'POST':
        form = EncuestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('lista')
    else:
        form = EncuestForm()
    
    return render(request, 'core/list.html', {'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return render(request, 'lista')
        else:
            valor = "*Ingrese usuario valido o contraseña correcta"
            contex = {'valor': valor}
            return render (request, 'core/login.html', context)
    contex = {}
    return render(request, 'core/login.html')