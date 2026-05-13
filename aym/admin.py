from django.contrib import admin
from .models import Producto 

# Registramos el modelo Producto para que sea visible
admin.site.register(Producto)