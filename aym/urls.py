from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listar_productos, name='lista_prods')
]