from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
    

class Invenatario_Tienda(models.Model):
    Nombre = models.CharField(max_length=20)
    TIPO_PRODUCTO =[
        ('Papeleria', 'Papeleria'),
        ('Alimento', 'Alimento'),
        ('Material_Escolar', 'Material_Escolar'),    
    ]
    
    Categoria = models.CharField(max_length=50, null= True, blank= True, choices=TIPO_PRODUCTO)
    Precio = models.DecimalField(max_digits= 7 , null= True, blank= True, decimal_places= 3)
    Stock = models.IntegerField()
    Nota = models.TextField(null= True, blank= True)
    
    
    
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    Stock = [
        ('ESCOLAR', 'Articulos escolares'),
        ('BAZAR', 'Regalos/Bazar'),
        ('ALIMENTO', 'Colaciones/Alimentos'),
    ]
    categoria = models.CharField(max_length=20, choices= Stock, default='ESCOLAR')
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    precio_coste = models.IntegerField(default= 0, blank=True)
    descripcion = models.TextField(blank=True, default="")
    precio = models.IntegerField(blank=True, default= 0)    
    
    
    
    
    
    
                                                                                              
    
    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"
    
    
    
    
