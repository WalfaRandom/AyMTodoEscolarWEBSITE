from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    OPCIONES_CATEGORIA = [
        ('ESCOLAR', 'Artículos Escolares'),
        ('REGALO', 'Regalos/Bazar'),
        ('ALIMENTO', 'Colaciones/Alimentos'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(0,message="el precio no puede ser negativo")])
    stock = models.IntegerField(validators=[MinValueValidator(0,message="el stock no puede ser negativo")])
    precio_coste = models.IntegerField(default=0, blank=True,validators=[MinValueValidator(0,message="el precio no puede ser negativo")])
    categoria = models.CharField(
        max_length=20,
        choices=OPCIONES_CATEGORIA,
        default='ESCOLAR'
    )
    
    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"