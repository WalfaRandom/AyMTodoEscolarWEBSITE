from django import forms

class ProductoForm(forms.Form):
    pk = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    nombre = forms.CharField(max_length=255, label='Nombre')
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, label='Descripción')
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio de venta')
    precio_coste = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio de coste')
    stock = forms.IntegerField(min_value=0, label='Stock')
    categoria = forms.CharField(max_length=255, label='Categoría')