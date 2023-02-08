# Plantillas con Jinja2 y HTML

1. [Introducción a plantillas](#Introducción-a-plantillas)
2. [Creación de plantillas](#Creación-de-plantillas)
3. [Uso de variables y bucles ](#Uso-de-variables-y-bucles )
4. [Uso de herencia de plantillas](#Uso-de-herencia-de-plantillas)
5. [Uso de filtros y funciones](#Uso-de-filtros-y-funciones)
6. [Cómo enviar datos a las plantillas s](#Cómo-enviar-datos-a-las-plantillas )
7. [Enlaces y rutas](#Enlaces-y-rutas)
8. [Integrando archivos estáticos ](#Integrando-archivos-estáticos )

---
## Introducción a plantillas

Jinja2 es un motor de plantillas para Python que permite crear plantillas dinámicas y generar contenido HTML, XML, etc. con datos en tiempo de ejecución. Flask es un framework web de Python que permite construir aplicaciones web de manera fácil y rápida.

En Flask, Jinja2 se utiliza como motor de plantillas por defecto y se puede utilizar para incluir contenido dinámico en las páginas HTML. Por ejemplo, puedes pasar variables desde Flask a Jinja2 para ser mostradas en la página HTML. También se pueden utilizar control structures en Jinja2 como bucles y condicionales para crear contenido dinámico en base a datos en tiempo de ejecución.

En resumen, Jinja2 es una herramienta poderosa para crear plantillas dinámicas y su uso en Flask lo hace aún más fácil y flexible para desarrollar aplicaciones web.

---
## Creación de plantillas

Aquí hay un ejemplo básico de cómo crear una plantilla con Jinja2 y HTML:

`templates/index.html`
~~~html
<!DOCTYPE html>
<html>
  <head>
    <title>Mi sitio web</title>
  </head>
  <body>
    <h1>Bienvenido a mi sitio web</h1>
    {% if name %}
      <p>Hola, {{ name }}!</p>
    {% else %}
      <p>Hola, desconocido!</p>
    {% endif %}
  </body>
</html>
~~~

En este ejemplo, hemos creado una plantilla básica HTML con un título y un mensaje de bienvenida. Usamos Jinja2 para incluir una variable "name" en el mensaje de bienvenida. Si la variable "name" está presente, se mostrará un mensaje personalizado con el nombre. De lo contrario, se mostrará un mensaje genérico.

Las variables en Jinja2 se incluyen entre llaves dobles y doble porcentaje, como {{ name }}. Las estructuras de control se escriben con {% ... %}. En este caso, usamos una estructura "if ... else" para decidir qué mensaje mostrar en base a la presencia o ausencia de la variable "name".

Para renderizar la plantilla en Flask, se necesitaría el siguiente código:

~~~python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Alex'
    return render_template('index.html', name=name)
~~~

En este ejemplo, hemos creado una aplicación Flask que renderiza la plantilla "index.html" en la ruta raíz. Le pasamos la variable "name" con el valor "Alex" a la función `render_template()` para que esté disponible en la plantilla. Al ejecutar la aplicación y acceder a la ruta raíz en un navegador, se mostrará el mensaje personalizado con el nombre "Alex".

---
## Uso de variables y bucles 

Aquí hay un ejemplo de cómo usar variables y bucles en plantillas Jinja2:

`templates/index.html`
~~~html
<!DOCTYPE html>
<html>
  <head>
    <title>Mi sitio web</title>
  </head>
  <body>
    <h1>Bienvenido a mi sitio web</h1>
    {% if name %}
      <p>Hola, {{ name }}!</p>
    {% else %}
      <p>Hola, desconocido!</p>
    {% endif %}

    <h2>Lista de amigos</h2>
    <ul>
    {% for friends in friend %}
        <li>{{ friend }}</li>
    {% endfor %}
    </ul>
  </body>
</html>
~~~

En este ejemplo, hemos creado una plantilla HTML que muestra una lista de nombres. Usamos un bucle "for ... in" en Jinja2 para iterar sobre la lista de nombres y mostrar cada nombre en un elemento de lista "li". La variable "nombres" es una lista de nombres de amigos que se pasa desde Flask a la plantilla.

El siguiente es el código de Flask que renderiza la plantilla:

~~~python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Alex'
    friends = ['Alexander', 'Roel', 'Juan', 'Pedro']
    return render_template('index.html',name = name ,friends =friends)
~~~

---
## Uso de herencia de plantillas
Aquí hay un ejemplo de cómo usar la herencia de plantillas y bloques en Jinja2:

`templates/base.html`
~~~html
<!-- base.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>Mi sitio web - {% block title %}{% endblock %}</title>
  </head>
  <body>
    {% block content %}
    <!-- Bloque de contenido -->
    {% endblock %}
  </body>
</html>
~~~

`templates/index.html`
~~~html
{% extends 'base.html' %}

{% block title %}Página de inicio{% endblock %}

{% block content %}
    <h1>Bienvenido a mi sitio web</h1>
    {% if name %}
      <p>Hola, {{ name }}!</p>
    {% else %}
      <p>Hola, desconocido!</p>
    {% endif %}

    <h2>Lista de amigos</h2>
    <ul>
    {% for friends in friend %}
        <li>{{ friend }}</li>
    {% endfor %}
    </ul>
{% endblock %}
~~~

En este ejemplo, tenemos una plantilla base "base.html" que define una estructura básica de HTML para el sitio web. La plantilla hija "index.html" extiende la plantilla base y reemplaza los bloques "title" y "content" con su contenido específico.

El uso de bloques permite que la plantilla base defina una estructura básica que se pueda reutilizar en diferentes páginas del sitio web, mientras que las plantillas hijas pueden personalizar el contenido de cada página.

---
## Uso de filtros y funciones

Aquí hay un ejemplo de código que muestra cómo usar filtros y funciones personalizadas en Jinja2:

~~~html
<p>La fecha de hoy es: {{ today|date("d/m/Y") }}</p>
<p>El nombre en mayúsculas es: {{ name|upper }}</p>
<p>La frase repetida: {{ repeat("Hello", 3) }}</p>
~~~

En este ejemplo, estamos utilizando dos filtros ("date" y "upper") y una función personalizada ("repeat"). Estos elementos se usan dentro de los corchetes dobles y se aplican a las variables "today", "name" y "repeat", respectivamente.

El filtro "date" formatea una fecha en un formato específico, mientras que el filtro "upper" convierte una cadena en mayúsculas.

La función personalizada "repeat" toma una cadena y un número y devuelve una nueva cadena compuesta por la cadena repetida el número de veces especificado.

Para hacer que estos filtros y funciones estén disponibles en la plantilla, necesitaríamos proporcionarlos en nuestro archivo Flask:

~~~python
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.now()
    name = "Alex"
    friends = ['Alexander', 'Roel', 'Juan', 'Pedro']
    return render_template('plantilla.html', name=name, friends = friends, today=today)

@app.template_filter()
def repeat(s, n):
    return s * n
~~~

En este ejemplo, hemos creado una función personalizada "repeat" y la hemos registrado como un filtro de plantilla utilizando la función "template_filter()". Luego, en la función "index", estamos proporcionando una fecha y un nombre a la plantilla.

Al ejecutar la aplicación y acceder a la página en un navegador, se mostrará la fecha actual, el nombre en mayúsculas y la frase repetida tres veces.

---
## Cómo enviar datos a las plantillas 
Puedes enviar datos desde Flask a las plantillas Jinja2 mediante la función render_template de Flask. Aquí hay un ejemplo de código que muestra cómo hacerlo:
~~~ python 
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>/<email>')
def hola(name = None, age = None, email = None):
    my_data = {
        'name':name,
        'age': age,
        'email':email
    }
    return render_template('hola.html', data = my_data)
~~~

En este ejemplo, estamos creando un diccionario my_data que contiene información sobre un usuario. Luego, en la función index, estamos usando la función render_template para enviar este diccionario a la plantilla.

La plantilla puede acceder a los datos enviados de la siguiente manera:

`templates/hola.html`
~~~html
{% extends 'base.html' %}

{% block title %}Página de Hola{% endblock %}

{% block content %}
    {% if data.name is none and data.age is none%}
    <p>Hola Mundo!</p>
    {% elif data.age is none %}
    <p>Hola, {{ data.name }}!</p>
    {% elif data.email is none %}
    <p>Hola, {{ data.name }} el doble de tu edad es {{ data.age * 2 }}!</p>
    {% else %}
      <h2>Mis Datos </h2>
      <p>Nombre: {{ data.name }}</p>
      <p>Nombre: {{ data.age }}</p>
      <p>Nombre: {{ data.email }}</p>
    {% endif %}
{% endblock %}
~~~

En la plantilla, estamos accediendo a los datos enviados a través de la variable data. Esto nos permite acceder a los valores individuales como data.name, data.age y data.email.

Al ejecutar la aplicación y acceder a la página en un navegador, se mostrará la información del usuario en la plantilla.

---
## Enlaces y rutas 
En Jinja2, los enlaces son esenciales para crear una aplicación web dinámica. Para crear un enlace en Jinja2, puedes usar la siguiente sintaxis:

~~~html
<a href="{{ url_for('nombre_de_la_función_en_Flask') }}">Texto del enlace</a>
~~~

Aquí, "nombre_de_la_función_en_Flask" se refiere a la función en Flask que devuelve la página a la que quieres enlazar. La función `url_for()` se encarga de generar la URL correcta para esa función.


Creando rutas
~~~python
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    #Creando rutas 
    print(url_for('index'))
    print(url_for('hola'))
    print(url_for('code', code = 'print(code)'))
    return render_template('index.html')
~~~


Ejemplo en la aplicación 

``templates/base.html`
~~~html
<nav>
    <u>
        <li><a href="{{ url_for('index') }}">Inicio</a></li>
        <li><a href="{{ url_for('hello') }}">Hola</a></li>
        <li><a href="{{ url_for('code', code = 'print(code)' ) }}">Code</a></li>
    </u>
</nav>
~~~

--- 
## Integrando archivos estáticos  
Aquí hay un ejemplo de cómo integrar CSS y JavaScript en las plantillas Jinja2:

~~~html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<script src="{{ url_for('static', filename='js/main.js') }}"></script>
~~~

En este ejemplo, la plantilla base "base.html" incluye un enlace a un archivo CSS y un script de JavaScript al final del cuerpo de la página. Usamos la función "url_for()" de Flask para generar una URL para acceder a los archivos estáticos.

Para usar este ejemplo, necesitaríamos tener una carpeta "static" en la raíz de nuestro proyecto que contenga una carpeta "css" con un archivo "style.css" y una carpeta "js" con un archivo "maib.js".

El siguiente es un ejemplo básico de un archivo CSS:

`static/css/style.css`
~~~css
/* css/style.css */
body {
  font-family: sans-serif;
}

h1 {
  color: blue;
}
~~~

Y el siguiente es un ejemplo básico de un archivo JavaScript:

`static/css/main.js`
~~~js
// js/script.js
console.log('Hello, world!');
~~~

Al ejecutar la aplicación Flask y acceder a la página en un navegador, se mostrará la página de inicio con el estilo y la funcionalidad definidos en los archivos CSS y JavaScript.
