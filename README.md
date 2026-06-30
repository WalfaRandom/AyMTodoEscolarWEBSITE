```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Luego entra a `http://127.0.0.1:8000/login/` con el usuario creado.
Si le marcas "staff" al usuario (desde `/admin/` o al crearlo como
superusuario), también podrás administrar Categorías.

## Estructura

```
papeleria/
  papeleria/        # settings, urls del proyecto
  inventario/
    models.py        # Categoria, Producto, MovimientoStock
    forms.py          # ModelForms simples
    views.py          # Vistas genéricas + 1 vista de movimiento de stock
    urls.py
    admin.py           # Registro de modelos en el panel admin
    templates/inventario/
```