from django.db import models

# Definimos la estructura de un producto 
class Producto(models.Model):
    
    nombre = models.CharField(max_length=100)
    
    # Detalle del producto (puede quedar vacío)
    descripcion = models.TextField(blank=True, null=True)
        
    precio = models.IntegerField()
        
    stock = models.IntegerField()

    # retorna el nombre del producto
    def __str__(self):
        return self.nombre
