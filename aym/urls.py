from django.urls import path
from aym import views

urlpatterns = [    
    path('', views.listar_productos, name='lista_prods'),
    path('nuevo/', views.crear_producto, name='crear_prod'),
    path('editar/<int:id>/', views.editar_producto, name='editar_prod'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_prod'),
    path('dashboard', views.dash, name='dashboard'),

]