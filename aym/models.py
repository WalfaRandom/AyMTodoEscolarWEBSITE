from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    # Opciones de categorías para el Bazar
    OPCIONES_CATEGORIA = [
        ('ESCOLAR', 'Artículos Escolares'),
        ('BAZAR', 'Regalos/Bazar'),
        ('ALIMENTO', 'Colaciones/Alimentos'),
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, default="")
    precio = models.IntegerField(default =0, blank=True)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    # Probando nuevos campos
    precio_coste = models.IntegerField(default=0, blank=True)
    
    # Nuevo campo con opciones predefinidas
    categoria = models.CharField(
        max_length=20,
        choices=OPCIONES_CATEGORIA,
        default='ESCOLAR'
    )

    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"
