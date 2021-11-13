from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import Producto

# Create your views here.

""" VISTA AGREGAR PRODUCTO """

def agregar_producto(request, producto_id):

    carro = Carro(request) #instanciando carro

    producto = Producto.objects.get(id=producto_id) #obteniendo producto

    carro.agregar(producto) #agregando producto al carro

    return redirect("tienda")


""" VISTA ELIMINAR PRODUCTO """

def eliminar_producto(request, producto_id):
    
    carro = Carro(request) #instanciando carro

    producto = Producto.objects.get(id=producto_id) #obteniendo producto

    carro.eliminar(producto) #eliminando producto del carro

    return redirect("tienda")


""" VISTA RESTAR PRODUCTO """


def restar_producto(request, producto_id):

    carro = Carro(request)  # instanciando carro

    producto = Producto.objects.get(id=producto_id)  # obteniendo producto

    carro.restar_producto(producto)  # restando producto del carro

    return redirect("tienda")


""" LIMPIAR CARRO """

def limpiar_carro(request):
    
    carro = Carro(request)  # instanciando carro

    carro.limpiar_carro()

    return redirect("tienda")


""" def carro(request):
    
    return render(request, "carro/carro,html") """