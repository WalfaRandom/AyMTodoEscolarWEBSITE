from django.shortcuts import render
from .models import Producto # Importamos la tabla que creamos

def listar_productos(request):


    cat_seleccionada = request.GET.get('cat')

    # 1. busca TODOS los productos 

    if(cat_seleccionada):
        productos = Producto.objects.filter(categoria=cat_seleccionada)
    
    else:
        productos = Producto.objects.all()

    # 2. Preparamos el "paquete" para enviar al HTML
    # Esto es un Diccionario de Python 
    contexto = {
        'lista': productos
    }
    
    # 3. Entregamos
    return render(request, 'aym/index.html', contexto)