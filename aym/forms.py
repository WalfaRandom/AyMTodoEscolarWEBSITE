#/aym/forms.py
from django import forms
from .models import Producto

# Creamos un formulario que copia la estructura de nuestro modelo
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # Le decimos a Django qué campos queremos que el usuario pueda rellenar en la web
        fields = ['nombre', 'descripcion', 'precio', 'precio_coste', 'stock', 'categoria']
