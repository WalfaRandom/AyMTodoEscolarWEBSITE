from django.shortcuts import render, redirect
from .models import Invenatario_Tienda
from.models import producto
from .forms import productoForm




def index(request):
    Tienda_Inventario = Invenatario_Tienda.objects.all()
    return render(request, 'aym/index.html', {'Tienda_Inventario': Tienda_Inventario})

def detalle(request, id):
    Tienda_Inventarios = Invenatario_Tienda.objects.get(id=id)
    return render(request, 'aym/detalle.html', {'Tienda_Inventarios': Tienda_Inventarios})

    
    

def crear_producto(request):
    if request.method == 'POST':
        formulario = productoForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_prods')
    
    else:
        formulario = productoForm()
    contexto = {
        'form': formulario
        
    }
    return render(request, 'aym/crear.html', contexto)


def editar_producto(request, id):
    producto_obj = producto.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = productoForm(request.POST, instance=producto_obj)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_prods')
        
    else:
        formulario = productoForm(instance=producto_obj)
    
    contexto = {
        'form': formulario,
        'producto': producto_obj 
    }
    return render(request, 'aym/editar.html', contexto)



def eliminar_producto(request, id):
    producto_obj = producto.objects.get(id=id)
    
    if request.method == 'POST':
        producto_obj.delete()
        return redirect('lista_prods')
    
    return render(request, 'aym/eliminar.html', {'producto_obj': producto_obj})


def listar_productos(request):
    productos = producto.objects.all()
    
    busqueda = request.GET.get('q', '')
    categoria = request.GET.get('cat', '')
    ordenar_por = request.GET.get('order', '')  
    
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)
        
    if categoria:
        productos = productos.filter(categoria=categoria)
        
    if ordenar_por == 'precio_asc':
        productos = productos.order_by('precio')
    elif ordenar_por == 'precio_desc':
        productos = productos.order_by('-precio')
    elif ordenar_por == 'nombre_az':
        productos = productos.order_by('nombre')
    elif ordenar_por == 'nombre_za':
        productos = productos.order_by('-nombre')
        
        
        
        
    contexto = {
        'lista': productos,
        'busqueda_actual': busqueda,
        'categoria_actual': categoria,
        'orden_actual': ordenar_por
    }   
    return render(request, 'aym/index.html', contexto)




