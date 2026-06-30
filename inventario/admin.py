from django.contrib import admin
from .models import Categoria, Producto, MovimientoStock


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio_unitario', 'stock', 'activo')
    list_filter = ('categoria', 'activo')
    search_fields = ('nombre',)


@admin.register(MovimientoStock)
class MovimientoStockAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo', 'cantidad', 'fecha', 'usuario')
    list_filter = ('tipo',)
    date_hierarchy = 'fecha'