import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('precio_unitario', models.DecimalField(decimal_places=0, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('descripcion', models.TextField(blank=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('activo', models.BooleanField(default=True)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='productos', to='inventario.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='MovimientoStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('entrada', 'Entrada'), ('salida', 'Salida')], max_length=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('motivo', models.CharField(blank=True, max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='inventario.producto')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Movimiento de stock',
                'verbose_name_plural': 'Movimientos de stock',
                'ordering': ['-fecha'],
            },
        ),
    ]