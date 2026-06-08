from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listar_productos, name='lista_prods'),
    path('productos/nuevo/', views.crear_producto, name='crear_prod')
]