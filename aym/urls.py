from django.urls import path
from aym import views
from django.contrib.auth import views as auth_views # <-- IMPORTACIÓN NECESARIA

urlpatterns = [    
    path('dashboard', views.listar_productos, name='lista_prods'),
    path('nuevo/', views.crear_producto, name='crear_prod'),
    path('editar/<int:id>/', views.editar_producto, name='editar_prod'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_prod'),
    
    
    path('', auth_views.LoginView.as_view(template_name='aym/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='lista_prods'), name='logout'),
]