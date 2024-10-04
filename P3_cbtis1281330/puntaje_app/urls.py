from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("contactos",views.contactos,name="contactos"),
    path("empleado",views.empleado,name="empleado"),
    path("cliente",views.cliente,name="cliente"),
    path("productos",views.productos,name="productos"),
    path("sucursales",views.sucursales,name="sucursales")
] 
    
