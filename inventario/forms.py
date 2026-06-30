from django import forms
from .models import Producto, Categoria, MovimientoStock


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio_unitario', 'stock', 'descripcion', 'imagen', 'activo']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 2}),
        }


class MovimientoStockForm(forms.ModelForm):
    class Meta:
        model = MovimientoStock
        fields = ['tipo', 'cantidad', 'motivo']


class BusquedaForm(forms.Form):
    q = forms.CharField(label='Buscar', required=False)
    categoria = forms.ModelChoiceField(
        label='Categoría', queryset=Categoria.objects.all(), required=False
    )