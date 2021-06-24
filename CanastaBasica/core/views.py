from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def login(request):
    return render(request, "core/login.html")

def graficas(request):
    return render(request, "core/graficas.html")

def test(request):
    return render(request, "core/test.html")

# def base(request):
#     return render(request, "core/base.html")