# Introducción a Flask

1. [¿Qué es Flask?](#¿Qué-es-Flask?)
2. [Instalación y configuración](#Instalación-y-configuración)
3. [Hola Mundo con Flask](#Hola-Mundo-con-Flask)
4. [El depurado en Flask](#El-depurado-en-Flask)
5. [Rutas y vistas](#Rutas-y-vistas)
6. [Variables en rutas](#Variables-en-rutas)
7. [Escape de HTML](#Escape-de-HTML)

---
## ¿Qué es Flask?

Flask es un microframework de Python para desarrollar aplicaciones web. Es fácil de usar y permite a los desarrolladores crear aplicaciones web rápidamente y con poco código. Flask proporciona un enrutador URL y herramientas básicas para manejar solicitudes HTTP y respuestas, pero deja al desarrollador la libertad de elegir las bibliotecas y extensiones que mejor se ajusten a sus necesidades.

Flask ofrece una gran cantidad de flexibilidad y personalización, lo que lo hace adecuado tanto para proyectos pequeños como para aplicaciones de gran escala. Además, gracias a su gran comunidad y documentación en línea, es fácil encontrar soluciones a problemas comunes y aprender nuevas características y mejores prácticas.

### Ventajas de Flask

Algunas de las ventajas de Flask son:

- Fácil de usar: Flask es un framework muy simple y fácil de aprender. No tiene una gran cantidad de conceptos complicados y se puede comenzar a desarrollar aplicaciones web en poco tiempo.

- Flexibilidad: Flask es un framework muy flexible que permite al desarrollador elegir las herramientas y tecnologías que desea usar en su proyecto. No impone restricciones en cuanto a la forma en que debes estructurar tu aplicación.

- Pequeño y ligero: Flask es un framework muy ligero que se ejecuta en poco tiempo y requiere poca memoria. Esto lo hace ideal para aplicaciones web pequeñas y medianas.

- Comunidad activa: Flask cuenta con una comunidad activa de desarrolladores y usuarios que contribuyen con paquetes y extensiones para añadir nuevas funcionalidades.

- Bajo nivel de abstractión: Flask se enfoca en mantener un nivel bajo de abstractión, lo que permite al desarrollador tener un mayor control sobre su aplicación.

- Fácil de integrar con otros servicios: Flask es compatible con una amplia variedad de servicios y tecnologías, lo que permite integrarse fácilmente con otros servicios y aplicaciones.

Estas son solo algunas de las ventajas de Flask, pero hay muchas más que lo hacen una excelente opción para desarrollar aplicaciones web.

### Diferencia entre Flask y otros frameworks de aplicaciones web
Flask es un framework de aplicaciones web muy popular que se diferencia de otros frameworks en algunos aspectos clave:

- Tamaño: Flask es un framework muy ligero y de bajo nivel de abstracción, mientras que otros frameworks como Django o Ruby on Rails son más grandes y con un nivel de abstracción más alto.

- Flexibilidad: Flask es un framework muy flexible que permite a los desarrolladores elegir las herramientas y tecnologías que desean usar en su proyecto, mientras que otros frameworks imponen restricciones en cuanto a la forma en que deben estructurarse las aplicaciones.

- Enfoque: Flask se enfoca en ser una herramienta simple y fácil de usar para desarrollar aplicaciones web pequeñas y medianas, mientras que otros frameworks como Django están diseñados para ser utilizados en proyectos más grandes y complejos.

- Comunidad: Flask cuenta con una comunidad activa de desarrolladores y usuarios que contribuyen con paquetes y extensiones para añadir nuevas funcionalidades, mientras que otros frameworks como Django tienen una comunidad más grande y con más recursos disponibles.

En resumen, Flask y otros frameworks de aplicaciones web tienen sus ventajas y desventajas y la elección depende de tus necesidades y objetivos de desarrollo. Si buscas una herramienta flexible, simple y fácil de aprender, Flask es una buena opción, mientras que si buscas un framework más completo y con una comunidad más grande, otros frameworks como Django pueden ser una mejor opción.

---
## Instalación y configuración
La instalación de Flask es sencilla y puede ser realizada en pocos pasos:

- Instalar Python: Flask es una aplicación escrita en Python, por lo que debes tener una versión compatible de Python instalada en tu sistema.

- Instalar Flask: Puedes instalar Flask usando pip, el gestor de paquetes de Python, ejecutando el siguiente comando en la línea de comandos o terminal:

### Instalación VENV y PIP en Linux 
Si no viene instalado puedes instalar con el siguiente comando.
~~~
sudo apt-get install python3-pip
sudo apt-get install python3-venv
~~~

### Crea un entorno virtual 

Para crear un entorno virtual de Python con `venv` y instalar Flask, siga estos pasos:

1. Asegúrese de tener Python 3 instalado en su sistema.

2. Cree un nuevo entorno virtual con `venv`:

    ~~~
    python3 -m venv nombre_del_entorno
    ~~~

3. Active el entorno virtual:

    ~~~
    Windows: nombre_del_entorno\Scripts\activate
    Linux/MacOS: source nombre_del_entorno/bin/activate
    ~~~

4. Instale Flask en el entorno virtual:
    ~~~
    pip install flask
    ~~~

---
## Hola Mundo con Flask

Aquí hay un ejemplo básico de código para crear un "Hola mundo" con Flask:

~~~python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola, mundo!"
~~~

Guarde este código en un archivo con un nombre, por ejemplo, `hello.py`. A continuación, ejecute el archivo en su terminal con el comando:

~~~
flask --app hello run
~~~

Después de ejecutar este comando, puede acceder a su "Hola, mundo!" en su navegador en la URL `http://127.0.0.1:5000/`.

### El código de "Hola, mundo!" con Flask consta de los siguientes componentes:

1. Importación de Flask:
    ~~~python
    from flask import Flask
    ~~~
    Se importa la clase Flask desde el módulo flask para poder utilizar sus funcionalidades.

2. Creación de la aplicación Flask:
    ~~~python
    app = Flask(__name__)
    ~~~
    Se crea una instancia de la clase Flask, que representa la aplicación web en sí. La variable `__name__` se pasa como argumento para que Flask pueda determinar el nombre del módulo actual.

3. Definición de la ruta:
    ~~~python
    @app.route("/")
    ~~~
    Se usa la función `route` para indicar la URL que se asociará con la función que sigue. En este caso, se asocia la raíz `/` con la función `hello`.

4. Función de controlador:
    ~~~python
    def hello():
        return "Hola, mundo!"
    ~~~
    Esta función es la que se invocará cuando se acceda a la URL asociada. Devuelve una cadena de texto que representa la respuesta que se enviará al navegador.

5. Ejevuta la aplicación 
    `flask run` es un comando de la línea de comandos de Flask que se utiliza para iniciar un servidor web en el localhost (127.0.0.1) en el puerto 5000.

    El argumento `--app` se utiliza para especificar el nombre de la aplicación Flask que se ejecutará. En este caso, el nombre de la aplicación es "hello".

    Por lo tanto, el comando completo `flask run --app hello` iniciará el servidor web para la aplicación Flask llamada "hello".

    Tenga en cuenta que antes de ejecutar este comando, debe asegurarse de que Flask está instalado en su sistema y que también ha creado una aplicación Flask llamada "hola". De lo contrario, obtendrá un error.

    Después de guardar este código en un archivo, puede ejecutarlo en su terminal con el comando python nombre_del_archivo.py. Luego, puede acceder a su "Hola, mundo!" en su navegador en la URL http://127.0.0.1:5000/.

---
## El depurado en Flask

El depurado en Flask es el proceso de identificar y corregir errores en una aplicación Flask. Flask proporciona algunas herramientas para facilitar el depurado, incluidas las siguientes:

- Modo de depuración: El argumento `--debug` se utiliza para habilitar el modo de depuración en la aplicación Flask. Cuando el modo de depuración está habilitado, Flask proporciona información detallada sobre los errores que se producen, como la pila de llamadas, el archivo y la línea de código donde se produjo el error, etc. Por lo tanto, el comando completo `flask run --app hello --debug` iniciará el servidor web para la aplicación Flask llamada "hello" con el modo de depuración habilitado.

- Registro: Flask tiene un sistema de registro que permite registrar mensajes informativos, advertencias y errores en la aplicación. El registro puede ayudar a identificar la causa de un error en tiempo real.

- Depuración interactiva: Flask permite la depuración interactiva mediante el uso de puntos de interrupción y herramientas de depuración como pdb o ipdb.

- Herramientas de terceros: También hay herramientas de terceros disponibles que pueden ayudar en el depurado de Flask, como Flask-DebugToolbar, que proporciona una barra de herramientas de depuración en el navegador.

En resumen, Flask proporciona una serie de herramientas y características para ayudar en el depurado de aplicaciones Flask. La combinación adecuada de estas herramientas depende del tamaño y la complejidad de la aplicación, así como de las preferencias personales de cada desarrollador.

---
## Rutas y vistas 
En Flask, una "ruta" es un URL asociado a una función de Python que se ejecuta cuando se accede a esa URL en el navegador. Esta función se conoce como "vista".

Las rutas se definen en el código de la aplicación usando la decoración de Flask `@app.route`. Por ejemplo, aquí hay una ruta que se activa cuando se accede a la URL raíz de la aplicación:

~~~python
@app.route('/')
def index():
    return '<h1>Página de inicio!</h1>'
~~~
Cuando se accede a la URL raíz en el navegador, la función `index()` se ejecuta y su resultado se devuelve al navegador como la respuesta HTTP.

Y aquí hay otra ruta que se activa cuando se accede a la URL `/hello` de la aplicación:

~~~python
@app.route('/hello')
def hello():
    return '<h1>Hola Mundo!</h1>'
~~~

### Varias rutas en una vista 
En Flask, puede asignar varias rutas a una misma vista (función) utilizando varios decoradores `@app.route` con diferentes URLs. Por ejemplo:

~~~python
@app.route('/')
@app.route('/index')
def index():
    return '<h1>Página de inicio!</h1>'
~~~

En este ejemplo, la función `index()` se activará tanto para la URL "/" como para la URL "/index". Cada vez que se acceda a una de estas URLs en el navegador, la función `index()` se ejecutará y su resultado se devolverá como la respuesta HTTP.


---
## Variables en rutas 
Las vistas pueden aceptar argumentos en la URL, por ejemplo en Flask, puede incluir variables en las rutas de la siguiente manera:

~~~python
@app.route('/hello/<name>')
def hello(name=None):
    return f'<h1>Hola, {name}!</h1>'
~~~

En este ejemplo, "name" es una variable de la ruta. Cualquier valor proporcionado en su lugar en la URL se asignará a la variable "name" y se pasará a la función hello() como argumento.

También puede especificar el tipo de datos que se espera para la variable en la ruta. 
- `string`: (predeterminado) acepta cualquier texto sin barra inclinada
- `int`: acepta enteros positivos
- `float`: acepta valores de coma flotante positivos
- `path`: Me gusta `string` pero también acepta barras
- `uuid`: acepta cadenas UUID

Por ejemplo, solo números enteros:
~~~python
@app.route('/hello/<int:age>')
def hello(age=None):
    return f'<h1>Hola, tu edad es {age}!</h1>'
~~~
En este ejemplo, la variable "age" es un número entero y se convertirá automáticamente en un int en Python antes de ser pasado a la función hello(). Si se proporciona un valor que no sea un número entero en la URL, Flask generará un error de URL no válido.

Con todo lo que ya sabemos, podemos crear variar rutas con respuestas distintas. 
~~~python
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def hello(name=None, age=None):
    
    if name == None and age == None:
        return '<h1>Hola Mundo!</h1>'
    elif age == None:
        return f'<h1>Hola, {name}!</h1>'
    else:
        return f'<h1>Hola, {name} el doble de tu edad es {age * 2}!</h1>'
~~~

---
## Escape de HTML
En Flask, se recomienda escapar todas las entradas de usuario antes de incluirlas en una página HTML para prevenir ataques de inyección de código. Puede usar la función `escape()` de la biblioteca `markupsafe` de Python para escapar cualquier texto antes de incluirlo en una página HTML. Por ejemplo:

~~~python
from markupsafe import escape

@app.route('/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
~~~

En este ejemplo, la función `escape()` escapa cualquier carácter especial en la variable `code` antes de incluirla en la respuesta HTML. Esto ayuda a prevenir ataques de inyección de código al asegurarse de que cualquier carácter malicioso se muestre como texto plano en lugar de ejecutarse como código en el navegador.



