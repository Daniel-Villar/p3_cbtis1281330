from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request,"index.html")

def contactos(request):
    return render(request,"contactos.html")

def empleado(request):
    return render(request,"empleado.html")

def cliente(request):
    return render(request,"cliente.html")

def productos(request):
    return render(request,"productos.html")

def sucursales(request):
    return render(request,"sucursales.html")
