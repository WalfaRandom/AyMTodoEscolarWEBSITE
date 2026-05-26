from django.contrib import admin
from .models import Producto # El punto (.) significa "busca en la misma carpeta"

# Registramos el modelo Producto para que sea visible
admin.site.register(Producto)