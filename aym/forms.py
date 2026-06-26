from django import forms 
from .models import Producto

# Creación del form de la bd
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'precio_coste', 'stock', 'categoria']
        