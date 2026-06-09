from django.shortcuts import render
from .models import Producto
from django.shortcuts import render, redirect # Agregamos redirect aquí
from .forms import ProductoForm # Importamos tu nuevo formulario
# Create your views here.

def listar_productos(request):
    # 1. Traemos la consulta base sin ejecutar
    #Lo que hace Django acá no es leer los 600 productos, sino que apunta solamente al contenedor de productos
    productos = Producto.objects.all()
    
    # 2. CAPTURA DE PARÁMETROS DESDE LA URL (request.GET)
    busqueda = request.GET.get('q', '')         # Texto de la barra de búsqueda
    categoria = request.GET.get('cat', '')      # Filtro de categoría (el que ya creamos)
    ordenar_por = request.GET.get('order', '')  # Criterio de ordenamiento (precio, nombre)

    """ 
    El asistente mira la URL del navegador (request) para ver si el usuario escribió algo en la barra de búsqueda ('q'), si presionó un botón de categoría ('cat'), o si hizo clic en ordenar ('order').
    Si no hay nada, estas variables quedan vacías (''). 
    """


    # 3. APLICACIÓN DE FILTROS (Se van acumulando de forma inteligente)
    
    # Si el usuario escribió algo en la barra de búsqueda
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)
        
    """ 
    Si el usuario escribió "Acuarela", el asistente busca en la caja de productos y saca solo los que contienen la palabra "acuarela" (sin importar mayúsculas o minúsculas por el __icontains), y descarta el resto. Ahora la caja quizás tiene solo 5 productos.
    """

    # Si el usuario seleccionó una categoría en la botonera
    if categoria:
        productos = productos.filter(categoria=categoria)
        
    """ 
    Si además el usuario tenía seleccionada la categoría "ESCOLAR", el asistente toma esos 5 productos que sobrevivieron al primer filtro y les aplica un segundo embudo. Si de las 5 acuarelas una era de "BAZAR", la quita. Los filtros se acumulan de forma inteligente.
    """

    # 4. APLICACIÓN DE ORDENAMIENTO (order_by)
    if ordenar_por == 'precio_asc':
        productos = productos.order_by('precio')       # Menor a Mayor
    elif ordenar_por == 'precio_desc':
        productos = productos.order_by('-precio')      # Mayor a Menor (el signo '-' invierte)

    elif ordenar_por == 'nombre_az':
        productos = productos.order_by('nombre')       # A - Z
    elif ordenar_por == 'nombre_za':
        productos = productos.order_by('-nombre')      # Z - A

    # 5. EMPAQUETADO PARA EL TEMPLATE
    contexto = {
        'lista': productos,
        'busqueda_actual': busqueda, # Mantenemos el texto en la casilla para comodidad del usuario
        'categoria_actual': categoria,
        'orden_actual': ordenar_por
    }
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