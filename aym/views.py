from django.shortcuts import render, redirect
from .models import Producto # Importamos la tabla que creamos
from .forms import ProductoForm

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


def crear_producto(request):
    # 1. Si el usuario presionó el botón de guardar (envió datos)
    if request.method == 'POST':
        # Tomamos el formulario e inyectamos los datos que del POST
        formulario = ProductoForm(request.POST)
        
        # Validación automática de Django 
        if formulario.is_valid():
            # Si todo está perfecto, el ORM lo guarda directo en la base de datos
            formulario.save()
            # Redirigimos al usuario de vuelta al listado de productos para que vea el cambio
            return redirect('lista_prods')
            
    # 2. Si el usuario solo está entrando a la página a mirar (petición GET)
    else:
        # Creamos el formulario limpio y vacío
        formulario = ProductoForm()
        
    # Enviamos el formulario (ya sea vacío o con los errores de validación) al HTML
    contexto = {
        'form': formulario
    }
    return render(request, 'aym/crear.html', contexto)