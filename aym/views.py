from django.shortcuts import render
from .models import Producto
from django.shortcuts import render, redirect # Agregamos redirect aquí
from .forms import ProductoForm # Importamos tu nuevo formulario
# Create your views here.

def listar_productos(request):
    cat_seleccionada = request.GET.get('cat')
    
    if cat_seleccionada:
        productos = Producto.objects.filter(categoria= cat_seleccionada)
    
    else:
        productos = Producto.objects.all()

    #Creación de un diccionario con los productos 
    contexto={
        'lista': productos
    }

    return render(request, 'aym/index.html',contexto)

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


def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    #POST
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_prods')
    #GET
    else:
        formulario = ProductoForm(instance=producto)
        # Empaquetar y renderizar
    contexto = {
        'form': formulario,
        'producto': producto # nos sirve si queremos mostrar el nombre original en el HTML
    }
    return render(request, 'aym/editar.html', contexto)    

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    
    if request.method == 'POST':
        # El ORM borra el registro de la base de datos de forma definitiva
        producto.delete()
        return redirect('lista_prods')
        
    return render(request, 'aym/eliminar.html', {'producto': producto})