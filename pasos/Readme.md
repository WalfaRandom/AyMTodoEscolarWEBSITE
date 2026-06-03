# Configuración de Django 🚀

# Tabla de contenidos

- [Configuración de Django 🚀](#configuración-de-django-)
- [Tabla de contenidos](#tabla-de-contenidos)
  - [0. Conceptos a conocer](#0-conceptos-a-conocer)
  - [1. Entorno de trabajo](#1-entorno-de-trabajo)
  - [2. Estructura del proyecto](#2-estructura-del-proyecto)
    - [2.1 Configuración inicial](#21-configuración-inicial)
  - [3. Los nuevos archivos](#3-los-nuevos-archivos)
  - [4. App dentro de un proyecto](#4-app-dentro-de-un-proyecto)
    - [4.1 Registrar la app](#41-registrar-la-app)
    - [4.2 Realizar migraciones](#42-realizar-migraciones)
  - [5. Creando los modelos](#5-creando-los-modelos)
    - [5.1 Aplicar planos](#51-aplicar-planos)
    - [5.2 Crear superusuario](#52-crear-superusuario)
    - [5.3 Registrar modelo en el panel](#53-registrar-modelo-en-el-panel)
  - [6. Creando la vista](#6-creando-la-vista)
    - [6.1 Mapa de rutas](#61-mapa-de-rutas)
  - [7. Creación de Categorías](#7-creación-de-categorías)
    - [7.1. Creación del Front-End](#71-creación-del-front-end)
    - [7.2 Filtrado de datos](#72-filtrado-de-datos)
    - [7.3 Validador de campos vacíos](#73-validador-de-campos-vacíos)
    - [7.4 Correcciones en model](#74-correcciones-en-model)
  - [8. Agregar productos desde mi JSON](#8-agregar-productos-desde-mi-json)
  - [9 CRUD](#9-crud)
    - [9.1 GET vs POST en formularios](#91-get-vs-post-en-formularios)
    - [9.2 Creación de productos](#92-creación-de-productos)
    - [9.3 Editar productos](#93-editar-productos)
    - [9.4 Eliminar productos](#94-eliminar-productos)
  - [10. Filtrado de productos](#10-filtrado-de-productos)


---

## 0. Conceptos a conocer
**MVT (Modelo - Vista - Template)**

- **Modelo (M):** La estructura de la Bodega. Cómo se guarda un lápiz o un cuaderno en la base de datos.  

- **Vista (V):** La lógica en Python que decide qué datos mostrar.  

- **Template (T):** El HTML que el cliente finalmente ve.

**MODELADO EN DJANGO**
En Django, cada modelo es una clase de Python que representa una tabla en la base de datos. Usaremos **models.CharField** para texto y **models.IntegerField** para números.

**ORM (Object Relational Mapping)**

Es una técnica y herramienta de software que nos permite convertir (en este caso) nuestro código python (models.py) en código SQL para que nuestra base de datos la pueda leer correctamente y así, nos envitamos de escribir SQL en nuestro documento. 

**Los cuatro tipos de campos básicos** 
Para aprovechar nuestro ORM que nos brinda Django, necesitamos conocer los 4 campos de datos más usados:
`CharField:` Para textos cortos (nombres, marcas). Siempre pide un max_length para saber cuánta memoria reservar en el disco duro.

`TextField:` Para textos largos (descripciones, notas). No tiene límite estricto de caracteres.

`IntegerField:` Para números enteros (precios, stock).

`BooleanField:` Para Verdadero/Falso.

> Al momento de crear nuestros nuevos campos y asignarlos a las variables, es imperativo saber que estas en las bases de datos no usan camelCase sino que deben usar snake_case para nombrarlas`

---


## 1. Entorno de trabajo
**siempre verificar estar en la carpeta del proyecto**
```bash
# 1. Crear entorno virtual
python -m venv env

# 2. Activar entorno
# Si es PowerShell:
\env\Scripts\Activate.ps1
# Si es CMD:
\env\Scripts\activate
#Si es git
source env/Scripts/activate
```
Una vez que nos aparece el (env) en la terminal instalamos:
```bash
pip install django
```
## 2. Estructura del proyecto
```bash
#Crear Proyecto:
python -m django startproject config .
#Migraciones:
python manage.py migrate
python manage.py runserver
```
**Explicación de startproject**
`python -m` &rarr; Si en env nosotros instalamos la versión 5.0 de django nos aseguramos de usar solo esa versión, esto sirve para evitar conflictos de clases o funciones obsoletas

`config .` &rarr; Es el nombre que tendrá nuestra carpeta, por buenas prácticas siempre se le llama config, ya que van muchas configuraciones dentro.
El punto final mvita que Django cree una carpeta dentro de otra con el mismo nombre.

### 2.1 Configuración inicial
Luego de ejecutar los comandos anteriores, debemos entrar a `settings.py` para cambiar el idioma y hora del sistema:
```bash
# settings.py

# 1. Idioma español
LANGUAGE_CODE = 'es-cl' 

# 2. Zona horaria de Chile 
TIME_ZONE = 'America/Santiago'

USE_I18N = True
USE_TZ = True
```

## 3. Los nuevos archivos
`manage.py`:  A partir de ahora, casi siempre usaremos `python manage.py [comando]`. Es la herramienta para prender el servidor, crear tablas en la base de datos y crear nuevas secciones del sistema.  

`settings.py`: Es el archivo de configuración global. Aquí registramos qué base de datos usaremos, el idioma del sitio y las carpetas de seguridad.   

`urls.py`: Es el encargado del enrutamiento, es el mapa que le dice al Protocolo HTTP a qué dirección debe ir cuando el usuario pide algo en el navegador.   

## 4. App dentro de un proyecto
En Django, un Proyecto es el sitio web completo (El Bazar), y una App es una funcionalidad específica (Inventario, Ventas, Usuarios).

Si mañana el Bazar quiere vender almuerzo, solo creamos la App comida sin romper lo que ya hicimos de escolares.

Creando la primera funcionalidad, asegura que **env** esté activo:
```bash
python manage.py startapp aym
```
**python manage.py:** Es el control del proyecto que creamos anteriormente.

**startapp:** Le ordena a Django que cree una nueva carpeta con archivos específicos para manejar una funcionalidad.

**aym:** Es el **nombre** de nuestra carpeta. Aquí definiremos qué datos tiene cada producto que creemos.

### 4.1 Registrar la app
Luego de ejecutar el comando anterior, debemos decirle a Django que trabajaremos con esta app creada. Vamos a modificar nuestro archivo `settings.py`
```bash
# config/settings.py

INSTALLED_APPS = [
    'aym',  # Agregamos nuestra nueva app
    'django.contrib.admin',
    'django.contrib.auth',
    # ... otras aplicaciones que ya vienen 
]
```
### 4.2 Realizar migraciones
Django viene con una base de datos interna para manejar usuarios y sesiones.

Una migración es la orden que le damos a Django para que tome sus planos de diseño y los transforme en tablas reales dentro del archivo de la base de datos (db.sqlite3).
Para ello vamos a realizar los siguientes comandos:
```bash
python manage.py migrate
```
Lee todas las aplicaciones registradas en settings.py y crea las tablas necesarias en la base de datos.

Desde ahora **cada vez** que hagamos un cambio en los modelos deberemos usar estos comandos
```bash
#1. Crea el plano del cambio
python manage.py makemigrationss

#2. Aplica los cambios en la BD
python manage.py migrate

```
Luego de esto podemos correr nuestro servidor con este comando
```bash
python manage.py runserver

```
Si entramos al link que nos muestra en la terminal (http://127.0.0.1:8000/) veremos un cohete de Django

## 5. Creando los modelos
Vamos a ingresar a nuestra carpeta aym y abrimos `models.py`. Acá vamos a crear la tabla producto
```bash
#aym/models.py
from django.db import models

class Producto(models.Model):
    # Texto para el nombre (máximo 100 caracteres)
    nombre = models.CharField(max_length=100)
    
    # Texto largo para detalles (opcional)
    descripcion = models.TextField(blank=True, null=True)
    
    # Número entero para el precio
    precio = models.IntegerField()
    
    stock = models.IntegerField()

    #Retornamos el nombre del producto
    def __str__(self):
        return self.nombre
```
### 5.1 Aplicar planos
Como modificamos models debemos avisarle a Django, para ello detén el servidor si esta corriendo (Ctrl + C) y en la terminal escribimos:
```bash

python manage.py makemigrations aym
# Nos mostrara un mensaje: Create model Producto
python manage.py migrate
# Acá se guarda la tabla en la BD
```
### 5.2 Crear superusuario
Vamos a crear nuestro usuario **admin**:
```bash
python manage.py createsuperuser
```
Ahora la terminal va a hacer preguntas:
- **Username:** admin 

- **Email address:** Déjalo en blanco y presiona Enter.

- **Password:** Cuando escribas la contraseña, no verás que se mueva el cursor ni aparecerán asteriscos. Escribe tu clave y presiona Enter.

- **Password (again):** Repite la misma clave y presiona Enter.

Si pones una clave muy corta Django te advierte que es insegura, puedes escribir **y** para confirmar que quieres usarla de todas formas.

### 5.3 Registrar modelo en el panel
Nos vamos a la ruta `aym/admin.py` y escribimos lo siguiente:
```bash
from django.contrib import admin
from .models import Producto # El punto (.) significa "busca en la misma carpeta"

# Registramos el modelo Producto para que sea visible
admin.site.register(Producto)
```
Ahora vamos a crear un nuevo producto desde el admin
- Primero ejecutamos el servidor con el `python manage.py runserver`
- Nos vamos a la siguiente url `http://127.0.0.1:8000/admin`
- Ingresamos con las credenciales que creamos.
- Entramos donde dice Productos
- Apretamos "add Producto"
- Rellenamos con los datos solicitados
- Guardamos
  
## 6. Creando la vista
En el archivo `aym/views.py` vamos a escribir una función que traiga todos los artículos escolares de la base de datos.
```python
from django.shortcuts import render
from .models import Producto # Importamos la tabla que creamos

def listar_productos(request):
    # 1. busca TODOS los productos 
    productos = Producto.objects.all()
    
    # 2. Preparamos el "paquete" para enviar al HTML
    # Esto es un Diccionario de Python 
    contexto = {
        'lista': productos
    }
    
    # 3. Entregamos
    return render(request, 'aym/index.html', contexto)
```
### 6.1 Mapa de rutas
Debemos configurar las direcciones para que Django sepa donde enviar nuestros producto, para ello debemos realizar dos pasos:
**Paso 1**
Primero nos vamos, en **aym**, a `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('/productos/', views.listar_productos, name='lista_prods'),
]
```


`path('productos/', ...)`: Aquí definimos la sub-ruta. Esto significa que cuando alguien escriba /productos/ en la barra de direcciones, Django sabrá que debe buscar en la aplicación de AyM.

`views.listar_productos`: Es la orden directa. Le decimos: "Si alguien llega a esta dirección, llama inmediatamente a listar_productos para que los muestre".

`name='lista_prods'`: Es un apodo técnico. En el futuro, si queremos crear un botón que lleve a los productos, usaremos este nombre en lugar de escribir toda la dirección a mano.

---

**Paso 2** 
Luego conectamos con el cerebro de Django, para ello nos vamos a `config/urls.py`
```python
from django.contrib import admin
from django.urls import path, include # Importamos include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aym/', include('aym.urls')), # Conectamos nuestro local
]
```

Esto es lo primero que revisa Django cuando alguien entra a tu sitio web.

`from django.urls import ..., include`: La palabra clave aquí es include. Es la herramienta que nos permite conectar otros mapas.

`path('aym/', include('aym.urls'))`:  Le estamos diciendo al sistema:

Cualquier dirección que empiece con aym/... pásasela al mapa interno de la aplicación aym para que ella decida qué hacer.
## 7. Creación de Categorías

Como ahora tenemos un aproximado de las cantidades y tipos de productos que trabajan, vamos a crear tres tipos de categorías generales. Para ello vamos a modificar nuestra carpeta `models.py`.
```python
from django.db import models

class Producto(models.Model):
    # Opciones de categorías para el Bazar
    OPCIONES_CATEGORIA = [
        ('ESCOLAR', 'Artículos Escolares'),
        ('REGALO', 'Regalos/Bazar'),
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
```
`choices`: Crea un menú desplegable en el Panel de Admin. El dueño solo selecciona la opción, evitando errores de tipeo (ej: escribir "Escolares" y otros "Escolar").

`get_categoria_display()`: Es un truco de Django para que en el panel no leamos ESCOLAR, sino el Artículos Escolares.

### 7.1. Creación del Front-End
Vamos a ir a nuestra carpeta `aym` y allí vamos a crear una subcarpeta llamada `templates`, luego, dentro de esta creamremos otra carpeta llamada igual que nuestra app `aym`, aí creamos el index.html. Les deberá quedar así:
`aym/templates/aym/index.html`. Allí vamos a escribir la estrucutra de nuestro HTML junto con el **for** para que recorra nuestra tabla **productos**:

```html
<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
        table,th,tr,td{
            border: 1px solid;
            border-collapse: collapse;            
            padding: 2px;
        }
        
    </style>
  </head>
  <body>
    <h1>Inventario de AYM</h1>
    <p>Lista de artículos escolares y colaciones en sistema:</p>      
      
      <table>
        <tr>
            <th>Nombre</th>
            <th>Precio</th>
            <th>Stock</th>
            <th>Descripción</th>
            <th>Categoría</th>
        </tr>
        {% for prod in lista %}
        <tr>
            <td>{{ prod.nombre }}</td>
            <td>${{ prod.precio }}   </td>
            <td>{{ prod.stock }}</td>
            <td>{{ prod.descripcion }}</td>
            <td>{{ prod.get_categoria_display }}</td>
        </tr>
         {% empty %}
        <h2>No hay productos Registrados en el inventario</h2>
        {% endfor %}
      </table>
                
  </body>
</html>
```
Le agregué el signo **$** antes de prod.precio para que se entienda mejor que hablamos de dinero.

**{{ prod.get_categoria_display }}:** En vez de mostrarle al cliente ALIMENTO en mayúsculas, mostrará "**Colaciones/Alimentos**".

**{% empty %}:** Es un salvavidas. Si se borran todos los productos, en vez de quedar la página en blanco, mostrará el mensaje automático de que no hay registros.

### 7.2 Filtrado de datos
Por el momento funciona todo bien, pero cuando agreguemos los 600 productos va a ser muy díficil buscar los productos entre tantos otros. Lo que vamos a hacer ahora es filtrar datos usando el **ORM** de Django.
Nosotros actualmente para mostrar los productos en nuestro `views.py` tenemos `Producto.objects.all()`, lo que hace es mostrar todo de la BD, para filtrar los datos vamos a usar la función `filter()`. Para ello vamos a modificar nuestro archivo, nos iremos a `aym/views.py`:
Si nosotros quisieramos ver solo la catergoría alimento deberíamos hacer esto:
```bash
# Le decimos al ORM que solo traiga los productos cuya categoría sea exactamente 'ALIMENTO'
productos = Producto.objects.filter(categoria='ALIMENTO')
```
Si nosotros quisíeramos seleccionar otra categoría diferente tenenos, por el momento, dos opciones:

- Cambiar directamente el tipo de categoría en el archivo views.py
- Cambiar la categoría desde la URL:
Para ello podemos enviar instrucciones "ocultas" en la URL usando el símbolo **?**. Por ejemplo:
`http://127.0.0.1:8000/aym/productos/?cat=ALIMENTO`
El Backend puede leer lo que viene después de `?cat=` y usar esa palabra para filtrar la base de datos automáticamente.

Para hacer nuestro proyecto dinámico vamos a usar este segundo concepto y lo aplicaremos a nuestro `views.py` y a nuestro `index.html`.
```python
def listar_productos(request):
    # 1. Leemos si el usuario mandó una categoría en la URL (ej: ?cat=REGALO)
    # Si no mandó nada, la variable quedará vacía (None)
    cat_seleccionada = request.GET.get('cat')
    
    # 2. Lógica de decisión
    if cat_seleccionada:
        # Si el usuario eligió una categoría, filtramos por ella
        productos = Producto.objects.filter(categoria=cat_seleccionada)
    else:
        # Si entró a la página normal (sin ?cat=), mostramos TODO el inventario
        productos = Producto.objects.all()

    # Diccionario de productos
    contexto={
        'lista': productos
    }

    return render(request, 'aym/index.html',contexto)
```
Una vez hecho esto podemos modificar los filtros desde la URL para que muestren los productos por categoría. Ejemplo:

http://127.0.0.1:8000/aym/productos/ &rarr; Debería mostrar la tabla completa con todos los productos.

http://127.0.0.1:8000/aym/productos/?cat=ALIMENTO &rarr; Debería mostrar solo los categorizados como alimentos (galletas).

http://127.0.0.1:8000/aym/productos/?cat=ESCOLAR &rarr; Debería mostrar solo los categorizados como escolar (cuaderno).
Luego de verificar que los productos funcionan correctamente, vamos a modificar nuestro HTML para que filtre mediante un click. Para ello vamos a agregar en nuestro **header** (si tenemos) un nav con las url predeterminadas según el tipo de filtro
```html
<nav style="margin-bottom: 20px;">
    <strong>Filtrar por categoría:</strong>
    <a href="/aym/productos/">Todos</a> | 
    <a href="/aym/productos/?cat=ESCOLAR">Útiles Escolares</a> | 
    <a href="/aym/productos/?cat=ALIMENTO">Colaciones</a> | 
    <a href="/aym/productos/?cat=REGALO">Regalos/Bazar</a>
</nav>
```
El primer enlace `(/aym/productos/)` no lleva ningún parámetro **?cat=**. Al hacer clic ahí, tu variable categoria_seleccionada en `views.py` será vacía, por lo que el **else** del código se activará y mostrará todo.

Los otros enlaces inyectan la palabra exacta que el **ORM** espera recibir en el filtro ('ESCOLAR', 'ALIMENTO', etc.).

### 7.3 Validador de campos vacíos
Para evitar que nuestra página, cuando no hayan productos, nos muestre fondo blanco, vamos a agregar tres validaciones dentro de mi tabla:
- **Primera validación**:
Es para cuando el valor del producto no existe o es 0
```html
 {% for prod in lista %}
      <tr>
        <td>{{ prod.nombre }}</td>
        <td>
          {% if prod.precio > 0 %} ${{ prod.precio }} {% else %} No hay precio
          disponible {% endif %}
        </td>
        <td>
```
- **Segunda validación:**
Vamos a validar que si nuestro stock es bajo x cantidad, en este caso es 5:
```html
<td>
          {% if prod.stock <= 5 %}
          <p style="color: red; font-weight: bold; padding: 0;margin: 0;">
            {{ prod.stock }} (¡Stock Bajo!)</p>
          {% else %} {{ prod.stock }} {% endif %}
        </td>
```
- **Tercera validación:**
Vamos a revisar cuando no hay ningpun producto en nuesta BD.
```html
   <td>{{ prod.descripcion }}</td>
        <td>{{ prod.get_categoria_display }}</td>
      </tr>
      {% empty %}
      <tr>
        <td colspan="5" style="text-align: center; color: red; padding: 10px">
          <strong>No hay productos registrados en el inventario.</strong>
        </td>
      </tr>
      {% endfor %}
```
**Recuerden que estos no son el HTML completo por lo que deben modificar solamente la parte acorde a la validación que se realiza**

### 7.4 Correcciones en model 
```python
   from django.db import models
from django.core.validators import MinValueValidator

# Definimos la estructura de un producto 

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
```
De acá modificamos:
- El **import** se agregó el **MinValueValidator**, el cual valida que los datos no puedan ser negativos, evitando asi un problema grande en caso de que alguien intente eliminar de más el stock de x producto.
- En **descripción, precio y precio_coste** se agregaron los parámetros por defecto de "" y 0, los cuales me permiten, en caso de que luego de improtar nuestros archivos a nuestra bd, si se quiera agregar otros que no poseen todos sus campos completos, estos se rellenen automáticamente sin provocar errores.

## 8. Agregar productos desde mi JSON
Una vez terminada nuestra bd de prueba lo que debemos hacer es:
**Primero:** Eliminar los datos anteriores para tener nuestra BD limpia, esto lo haremos con un comando simple pero poderoso: `python manage.py flush`

**Segundo:**  Vamos a crear en nuestra ruta de `aym` una carpeta llamada **fixtures**, allí, vamos a agregar nuestro archivo .JSON con los productos que subiremos, nos deberá quedar algo como esta ruta: `aym/fixtures/productos.json`.
Luego de agregar nuestro archivo .JSON en esa ruta, vamos a ejecutar el siguiente comando:
`python manage.py loaddata productos`
Acá reemplacen el último término por el nombre de su archivo JSON, no es necesario que agreguen la extensión de archivo.


**Tercero:** Crear nuestro nuevo superusuario, como lo anterior elimina todos los datos de nuestra BD, nos quedamos sin superusuario para acceder al admin, por lo que debemos crearlo: `python manage.py createsuperuser`

## 9 CRUD
Lo primero que haremos será crear un formulario, para ellos nos iremos a nuestra carpeta raiz, `aym` y crearemos el documento que se llamará `forms.py`.
**Para construir este formulario, necesitamos importar la biblioteca de formularios de Django (from django import forms) y también el modelo que creamos (from .models import Producto).**
Este archivo tendrá esto dentro:
```python
#/aym/forms.py
from django import forms
from .models import Producto

# Creamos un formulario que copia la estructura de nuestro modelo
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # Le decimos a Django qué campos queremos que el usuario pueda rellenar en la web
        fields = ['nombre', 'descripcion', 'precio', 'precio_coste', 'stock', 'categoria']
```
**class Meta**: Es una configuración interna. Le dice a Django que use el modelo Producto como molde para fabricar este formulario".

**fields**: Aquí listamos las columnas que se transformarán en casillas de texto en la pantalla. Django transformará automáticamente el campo categoria en un menú de selección con tus opciones en mayúsculas (ESCOLAR, BAZAR, ALIMENTO).

### 9.1 GET vs POST en formularios

Cuando un usuario interactúa con un formulario, la vista tiene que manejar **dos** situaciones completamente distintas utilizando la misma URL:

Petición **GET** (El usuario entra a la página): El cliente quiere ver el formulario para empezar a escribir. La vista debe crear un formulario totalmente vacío y dibujarlo en la pantalla.

Petición **POST** (El usuario presiona "Guardar"): El cliente envía los datos que digitó de vuelta al servidor. La vista debe atrapar esa información, revisar que cumpla las reglas preventivas y guardarla en la base de datos.

### 9.2 Creación de productos
Es importante mencionar que son muy similares las formas de hacer el CRUD, por lo que si entienden una van a comprender la demás de mejor manera

**Vamos a una función dedicada a la creación de productos en `aym/views.py`:**

Para poder usar el formulario y redirigir al usuario una vez que guarde, necesitamos importar ProductoForm desde tu archivo .forms, y también la función redirect desde django.shortcuts.
```python
from django.shortcuts import render, redirect # Agregamos redirect aquí
from .models import Producto
from .forms import ProductoForm # Importamos tu nuevo formulario
```
Al final de `aym/views.py`, vamos a agregar la siguiente función.
```python
def crear_producto(request):
    # 1. Si el usuario presionó el botón de guardar (envió datos)
    if request.method == 'POST':
        # Tomamos el formulario e inyectamos los datos que del POST
        formulario = ProductoForm(request.POST)
        
        # Validación automática de Django 
        if formulario.is_valid():
            # Si todo está perfecto, el ORM lo guarda directo en la base de datos
            formulario.save()
            # Redirigimos al usuario de vuelta al listado de productos para que vea el cambio
            return redirect('lista_prods')
            
    # 2. Si el usuario solo está entrando a la página a mirar (petición GET)
    else:
        # Creamos el formulario limpio y vacío
        formulario = ProductoForm()
        
    # Enviamos el formulario (ya sea vacío o con los errores de validación) al HTML
    contexto = {
        'form': formulario
    }
    return render(request, 'aym/crear.html', contexto)
```
**request.POST:** Son los datos que el usuario llenó en el navegador. Al pasársela a ProductoForm(request.POST), Django ingresa cada dato en su casilla correspondiente de manera automática.

**formulario.is_valid():** Esta es una de las funciones más potentes de Django. Analiza si el nombre no está vacío, si los precios son números válidos y ejecuta en segundo plano tu **MinValueValidator(0)** para el stock. Si algo falla (por ejemplo, ponen stock -5), esta función da False, el código salta el guardado y vuelve a renderizar la página mostrando los errores en pantalla de forma automática.

**formulario.save():** El ORM genera el comando INSERT INTO en SQL por debajo y guarda el nuevo artículo en un milisegundo.

Ahora vamos a conectar la ruta en la  URLs, para ello debemos asignarle una dirección clara, para ello nos iremos a `aym/urls.py` y dentro de nuestro `urlpatterns`, agregaremos los siguiente:
```python
path('productos/nuevo/', views.crear_producto, name='crear_prod'),
```

Luego de agregar la URL, como pueden ver en la ultima línea  de nuestro `views.py` dice que esto estará en el archivo `crear.html`, el cual aun no hemos creado y es lo siguiente que haremos. Vamos a crear este archivo en la misma carpeta que index.html `aym/templates/aym/crear.html`:

```html
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>AyM - Añadir Producto</title>
  </head>
  <body>
    <h1>Registrar Nuevo Artículo</h1>
    <p>Complete los datos para incorporar el producto al inventario oficial:</p>

    <form method="POST">
      {% csrf_token %}

      <table>
        {{ form.as_table }}
      </table>

      <br />
      <button type="submit">Guardar Producto en Bodega</button>
    </form>

    <br />
    <a href="{% url 'lista_prods' %}">Volver al Inventario Total</a>
  </body>
</html>
```
**method="POST":** Le dice al navegador que cuando el usuario presione el botón, empaquete los datos de forma segura dentro del cuerpo de la petición HTTP (request.POST) y no a través de la URL.

**{% csrf_token %}:** ¡Esto es obligación en Django! Es una directiva de seguridad que inyecta un código secreto invisible y único. Evita un tipo de ataque hacker llamado Cross-Site Request Forgery (Falsificación de Petición en Sitios Cruzados), donde un sitio malicioso intenta enviar datos a tu base de datos haciéndose pasar por el dueño. Si no ponemos esta línea, Django bloqueará el guardado por seguridad y lanzará un error 403 Forbidden.

**{{ form.as_table }}:** Aquí ocurre la magia frontend de Django. En lugar de escribir seis etiquetas `<label>` y seis ``<input>``, Django lee tu forms.py y dibuja automáticamente las filas de la tabla con los cuadros de texto correspondientes, incluyendo los mensajes en rojo si hay errores de validación.

### 9.3 Editar productos
Este en general es igual al anterior pero primero es imporante aclarar que cuando creamos un producto, el form aparece vacío, pero al editar un artículo este debe tener sus datos correspondientes.

- Necesita saber qué producto se quiere editar (pasando el ID por la URL)
- Necesita además ingresar a la BD, buscar el producto y cargar sus datos

Primero nos iremos a nuestro `views.py`, en donde vamos a crear otra función que permita editar el producto:

```python
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    #POST
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_prods')
    #GET
    else:
        formulario = ProductoForm(instance=producto)
        # Empaquetar y renderizar
    contexto = {
        'form': formulario,
        'producto': producto # nos sirve si queremos mostrar el nombre original en el HTML
    }
    return render(request, 'aym/editar.html', contexto)    
```
Luego, igual que cuando creamos un producto, vamos a crear su URL pero esta será **dinámica**. Esto porque Django necesita recibir el ID del producto que se va a editar (por ejemplo: `/productos/editar/1/`, `/productos/editar/2/`, etc.).

Entonces nuestro archivo `aym/urls.py`nos deberá quedar asi:
```python
path('productos/editar/<int:id>/', views.editar_producto, name='editar_prod'),
```
`<int:id>` **le dice a Django**: "Cualquier número entero que el usuario ponga en esta parte de la barra de direcciones, atrápalo y pásaselo automáticamente como el argumento llamado id a la función editar_producto en las vistas".

Posterior a eso, vamos a crear nuestra vista de editar, en la misma carpeta donde tenemos los html crearemos nuestro `editar.html`, el cuál va a ser idéntico a nuestro `crear.html`.

Después vamos a modificar nuestra tabla (donde se muestran todos los productos). Vamos a crear una columna nueva, pondremos **Acciones** de encabezado y como cuerpo va a ser un botón que me direccione a la URL de la edición:
**Como hemos modificado la cantidad de elementos que posee mi tabla deberemos cambiar, a 6, el colspan que ingresamos antes**
```html
 {% empty %}
      <tr>
        <td colspan="6" style="text-align: center; color: red; padding: 10px">
          <strong>No hay productos registrados en el inventario.</strong>
```

```html
    <td>{{ prod.descripcion }}</td>
    <td>{{ prod.get_categoria_display }}</td>
    <td>
        <button>
            <a href="{% url 'editar_prod' prod.id %}">Editar</a>
            <!-- Esta es la forma de pasarle el ID del producto seleccionado de forma dinámica a la URL -->
        </button>      
    </td>
``` 

### 9.4 Eliminar productos
Al igual que los anteriores, esta función también necesita recibir el id del producto.

- Si el método es POST (el usuario confirmó que quiere borrar), usamos el método .delete() del ORM y redirigimos.

- Si el método es GET, simplemente le mostramos una página de advertencia preguntándole: ¿Está seguro de eliminar este producto?

Vamos a crear nuesta función en `views.py`:
```python
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    
    if request.method == 'POST':
        # El ORM borra el registro de la base de datos de forma definitiva
        producto.delete()
        return redirect('lista_prods')
        
    return render(request, 'aym/eliminar.html', {'producto': producto})
```
Luego creamos la URL en nuestro `urls.py`:
```python
path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_prod'),
```
Y creamos nuestro archivo `eliminar.html`, cuya función será mostrar el mensaje de confirmación de la eliminación del producto:
```html
<html lang="es">
<head><title>Eliminar Producto</title></head>
<body>
    <h1>¿Está seguro de eliminar el producto: "{{ producto.nombre }}"?</h1>
    <p style="color: red;">Esta acción es irreversible y removerá el artículo de la bodega.</p>

    <form method="POST">
        {% csrf_token %}
        <button type="submit" style="background-color: red; color: white;">Sí, Confirmar Eliminación</button>
        <a href="{% url 'lista_prods' %}">Cancelar y Volver</a>
    </form>
</body>
</html>
```
## 10. Filtrado de productos

Lo siguiente a realizar es una búsqueda específica de un producto en concreto. Para ello usaremos `Lookups`, que son operadores de consultas avanzados, específicamente el **__icontains**

- **contains:** Significa "que contenga este texto".

- La **i** al principio significa **Case-Insensitive** (insensible a mayúsculas o minúsculas). Da igual si escribe "ACUARELA", "Acuarela" o "acuarela", el ORM lo encontrará de todas formas.

Para ello, vamos a modificar nuestra función `listar_productos`en `aym/views.py`.
```python
def listar_productos(request):
    # 1. Traemos la consulta base (todos los productos) sin ejecutarla aún en SQL
    productos = Producto.objects.all()
    
    # 2. CAPTURA DE PARÁMETROS DESDE LA URL (request.GET)
    busqueda = request.GET.get('q', '')         # Texto de la barra de búsqueda
    categoria = request.GET.get('cat', '')      # Filtro de categoría (el que ya creamos)
    ordenar_por = request.GET.get('order', '')  # Criterio de ordenamiento (precio, nombre)

    # 3. APLICACIÓN DE FILTROS (Se van acumulando de forma inteligente)
    
    # Si el usuario escribió algo en la barra de búsqueda
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)
        
    # Si el usuario seleccionó una categoría en la botonera
    if categoria:
        productos = productos.filter(categoria=categoria)
        
    # 4. APLICACIÓN DE ORDENAMIENTO (order_by)
    if ordenar_por == 'precio_asc':
        productos = productos.order_by('precio')       # Menor a Mayor
    elif ordenar_por == 'precio_desc':
        productos = productos.order_by('-precio')      # Mayor a Menor (el signo '-' invierte)
    elif ordenar_por == 'nombre_az':
        productos = productos.order_by('nombre')       # A - Z
    elif ordenar_por == 'nombre_za':
        productos = productos.order_by('-nombre')      # Z - A

    # 5. EMPAQUETADO PARA EL TEMPLATE
    contexto = {
        'lista': productos,
        'busqueda_actual': busqueda, # Mantenemos el texto en la casilla para comodidad del usuario
        'categoria_actual': categoria,
        'orden_actual': ordenar_por
    }
    return render(request, 'aym/index.html', contexto)
```