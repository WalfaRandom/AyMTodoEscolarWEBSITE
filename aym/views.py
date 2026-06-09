from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    productos = Producto.objects.all()
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
def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
    if formulario.is_valid():
        formulario.save()
        return redirect('lista_prods')
    else:
        formulario = ProductoForm()
    contexto = {
        'form': formulario
    }
    return render(request, 'aym/crear.html', contexto)
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_prods')
    else:
        formulario = ProductoForm(instance=producto)
    contexto = {
        'form': formulario,
        'producto': producto
    }
    return render(request, 'aym/editar.html', contexto)
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_prods')
    return render(request, 'aym/eliminar.html', {'producto': producto})
        
    
# Create your views here.

