import json
from pathlib import Path

from django.conf import settings
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'aym/index.html')

def login(request):
    return render(request, 'aym/login.html')

def tables(request):
    product_file = Path(settings.BASE_DIR) / 'static' / 'productos.json'
    products = []

    if product_file.exists():
        try:
            with product_file.open('r', encoding='utf-8') as f:
                data = json.load(f)
            products = [
                {
                    'pk': item.get('pk'),
                    **item.get('fields', {}),
                }
                for item in data
            ]
        except (json.JSONDecodeError, OSError):
            products = []

    return render(request, 'aym/tables.html', {'products': products})
