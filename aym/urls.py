from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listar_productos, name='lista_prod'),
    path('productos/nuevo/', views.crear_producto, name='crear_prod'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_prod'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_prod'),
]   