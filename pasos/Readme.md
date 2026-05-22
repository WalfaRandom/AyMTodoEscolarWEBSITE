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
  - [8. Creación del Front-End](#8-creación-del-front-end)


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

## 8. Creación del Front-End