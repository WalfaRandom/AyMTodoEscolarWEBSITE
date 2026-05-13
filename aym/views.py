from django.shortcuts import render
from .models import Producto

def listar_productos(request):
    productos = Producto.objects.all()

    #Creación de un diccionario con los productos 
    contexto={
        'lista': productos
    }

    return render(request, 'aym/index.html',contexto)