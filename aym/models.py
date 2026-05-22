from django.db import models

# Definimos la estructura de un producto 

class Producto(models.Model):
    # Opciones de categorías para el Bazar
    OPCIONES_CATEGORIA = [
        ('ESCOLAR', 'Artículos Escolares'),
        ('BAZAR', 'Regalos/Bazar'),
        ('ALIMENTO', 'Colaciones/Alimentos'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    
    # Nuevo campo con opciones predefinidas
    categoria = models.CharField(
        max_length=20,
        choices=OPCIONES_CATEGORIA,
        default='ESCOLAR'
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"