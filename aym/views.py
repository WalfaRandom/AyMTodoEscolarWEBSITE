import json
from pathlib import Path

from django.conf import settings
from django.shortcuts import render

from .forms import ProductoForm

PRODUCT_FILE = Path(settings.BASE_DIR) / 'static' / 'productos.json'


def _read_products():
    products = []
    if PRODUCT_FILE.exists():
        try:
            with PRODUCT_FILE.open('r', encoding='utf-8') as f:
                data = json.load(f)
            for item in data:
                if not isinstance(item, dict):
                    continue
                pk = item.get('pk')
                if pk is None:
                    continue
                fields = item.get('fields') or {}
                product = {'pk': pk}
                product.update(fields)
                products.append(product)
        except (json.JSONDecodeError, OSError):
            products = []
    return products


def _write_products(products):
    output = []
    for product in products:
        fields = {key: value for key, value in product.items() if key != 'pk'}
        output.append({'model': 'aym.producto', 'pk': product['pk'], 'fields': fields})
    PRODUCT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with PRODUCT_FILE.open('w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)


def _get_next_pk(products):
    return max((product['pk'] for product in products), default=0) + 1


def index(request):
    return render(request, 'aym/index.html')


def login(request):
    return render(request, 'aym/login.html')


def crud(request):
    products = _read_products()
    categories = sorted({
        str(product.get('categoria')).strip()
        for product in products
        if product.get('categoria')
    })

    message = ''
    message_type = 'success'
    form_operation = 'add'
    form = ProductoForm()

    if request.method == 'POST':
        operation = request.POST.get('operation', 'add')
        if operation in {'add', 'update'}:
            form = ProductoForm(request.POST)
            if form.is_valid():
                product_data = {
                    'nombre': form.cleaned_data['nombre'],
                    'descripcion': form.cleaned_data['descripcion'],
                    'precio': float(form.cleaned_data['precio']),
                    'precio_coste': float(form.cleaned_data['precio_coste']),
                    'stock': int(form.cleaned_data['stock']),
                    'categoria': form.cleaned_data['categoria'],
                }
                if operation == 'add':
                    product_data['pk'] = _get_next_pk(products)
                    products.append(product_data)
                    message = 'Producto agregado correctamente.'
                else:
                    pk = form.cleaned_data.get('pk')
                    try:
                        pk = int(pk)
                    except (TypeError, ValueError):
                        pk = None
                    updated = False
                    for product in products:
                        if product['pk'] == pk:
                            product.update(product_data)
                            updated = True
                            break
                    if updated:
                        message = 'Producto actualizado correctamente.'
                    else:
                        message = 'No se encontró el producto para actualizar.'
                        message_type = 'error'
                _write_products(products)
                form = ProductoForm()
                form_operation = 'add'
            else:
                message = 'Corrija los errores del formulario antes de continuar.'
                message_type = 'error'
                form_operation = operation
        elif operation == 'delete':
            try:
                pk = int(request.POST.get('pk'))
            except (TypeError, ValueError):
                pk = None
            if pk is not None:
                products = [product for product in products if product['pk'] != pk]
                _write_products(products)
                message = 'Producto eliminado correctamente.'
            else:
                message = 'ID de producto inválido para eliminar.'
                message_type = 'error'
        else:
            message = 'Operación inválida.'
            message_type = 'error'

    elif request.GET.get('edit'):
        try:
            edit_pk = int(request.GET.get('edit'))
        except (TypeError, ValueError):
            edit_pk = None
        if edit_pk is not None:
            product_to_edit = next((product for product in products if product['pk'] == edit_pk), None)
            if product_to_edit:
                initial = {
                    'pk': product_to_edit['pk'],
                    'nombre': product_to_edit.get('nombre', ''),
                    'descripcion': product_to_edit.get('descripcion', ''),
                    'precio': product_to_edit.get('precio', 0),
                    'precio_coste': product_to_edit.get('precio_coste', 0),
                    'stock': product_to_edit.get('stock', 0),
                    'categoria': product_to_edit.get('categoria', ''),
                }
                form = ProductoForm(initial=initial)
                form_operation = 'update'
            else:
                message = 'Producto no encontrado para editar.'
                message_type = 'error'

    context = {
        'products': sorted(products, key=lambda product: product['pk']),
        'categories': categories,
        'form': form,
        'form_operation': form_operation,
        'message': message,
        'message_type': message_type,
    }
    return render(request, 'aym/crud.html', context)


def tables(request):
    products = _read_products()
    selected_category = request.GET.get('categoria', '').strip()
    search_query = request.GET.get('search', '').strip()
    sort_option = request.GET.get('sort', '').strip()
    categories = sorted({
        str(product.get('categoria')).strip()
        for product in products
        if product.get('categoria')
    })

    if selected_category:
        products = [
            product
            for product in products
            if str(product.get('categoria', '')).strip().lower() == selected_category.lower()
        ]

    if search_query:
        products = [
            product
            for product in products
            if search_query.lower() in str(product.get('nombre', '')).lower()
        ]

    if sort_option:
        if sort_option == 'az':
            products.sort(key=lambda product: str(product.get('nombre', '')).lower())
        elif sort_option == 'za':
            products.sort(key=lambda product: str(product.get('nombre', '')).lower(), reverse=True)
        elif sort_option == 'price_asc':
            products.sort(key=lambda product: float(product.get('precio') or 0))
        elif sort_option == 'price_desc':
            products.sort(key=lambda product: float(product.get('precio') or 0), reverse=True)
        elif sort_option == 'stock':
            products.sort(key=lambda product: int(product.get('stock') or 0), reverse=True)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
        'sort_option': sort_option,
    }
    return render(request, 'aym/tables.html', context)