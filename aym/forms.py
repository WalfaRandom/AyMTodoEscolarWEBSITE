from django import forms
from .models import producto

class productoForm(forms.ModelForm):
    class Meta:
        model = producto 
        fields = ['nombre', 'descripcion', 'precio', 'precio_coste', 'stock', 'categoria']