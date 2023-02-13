# Estructura de una aplicación - TodoList

1. [Presentación del proyecto](#¿Qué-es-Flask?)
2. [Estructura del proyecto](#Instalación-y-configuración)
3. [Hola Mundo con Flask](#Hola-Mundo-con-Flask)
4. [El depurado en Flask](#El-depurado-en-Flask)
5. [Rutas y vistas](#Rutas-y-vistas)
6. [Variables en rutas](#Variables-en-rutas)
7. [Escape de HTML](#Escape-de-HTML)


---
## Presentación del proyecto
---
## Estructura del proyecto
Para crear un proyecto en flask podemos seguir los siguientes pasos: 

1. Crear un directorio para tu proyecto y acceder a él:
	~~~
	mkdir todo-list
	cd todo-list
	~~~

2. Crear un entorno virtual:
	~~~
	python3 -m venv env-todo
	~~~
3. Activar el entorno virtual:

	~~~
	Linux/Mac: source env-todo/bin/activate
	Windows: env-todo\Scripts\activate
	~~~
4. Instalar Flask:
	~~~
	pip install Flask
	~~~

### Crea la estructura de tu proyecto 
Una estructura de una aplicación medianamente grande en Flask podría ser la siguiente:

~~~
todo-list/
├── todor/
│   ├── __init__.py
│   ├── todo.py
│   ├── auth.py
│   ├── models.py
│   └── templates/
├── requirements.txt
└── run.py
~~~

- `todor/`: es el directorio principal de la aplicación Flask.
- `todor/__init__.py`: contiene la inicialización de la aplicación Flask.
- `todor/models.py`: contiene los modelos de datos de la aplicación.
- `todor/templates/`: contiene los archivos HTML de la aplicación.
- `requirements.txt`: contiene las dependencias de la aplicación.
- `run.py`: contiene el código para ejecutar la aplicación Flask.

Esta estructura es un ejemplo básico, y puedes agregar o modificar directorios y archivos según las necesidades de tu proyecto.

---
## Configurar nuetra aplicación

Este código corresponde a una aplicación Flask. La aplicación se está creando utilizando una función `create_app`.

`todor/__init__.py`
~~~python
from flask import Flask

def create_app():
    app = Flask(__name__)

    #Configuración de poyecto 
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
    )

    @app.route('/hello')
    def hello():
        return 'Hola Mundo'
        
    return app
~~~

- La primera línea from `flask import Flask` importa la clase Flask del módulo flask. Esta clase es necesaria para crear una aplicación Flask.

- La función `create_app` es una función que devuelve una instancia de la clase Flask. Dentro de la función, se crea una nueva aplicación Flask con la siguiente línea: `app = Flask(__name__)`.

- En la sección de Configuración de proyecto se establecen los valores para dos variables de configuración: `DEBUG` y `SECRET_KEY`. La variable `DEBUG` se utiliza para habilitar o deshabilitar el modo de depuración de la aplicación, mientras que la variable `SECRET_KEY` se utiliza como clave secreta para proteger la aplicación contra ataques de seguridad.

- La decoración `@app.route('/hello')` indica que la función hello será ejecutada cuando el usuario acceda a la ruta `/hell`o en el navegador web.

- La función `hello` devuelve una cadena de texto "Hola Mundo", que será mostrada en el navegador web cuando se acceda a la ruta `/hello`.

- Finalmente, la función `create_app` devuelve la instancia de la aplicación Flask app.

En resumen, este código muestra cómo crear una aplicación Flask y cómo establecer configuraciones para la aplicación, así como cómo crear una ruta y una función para manejar la solicitud a esa ruta.

### Archivo principal del proyecto 
Este código es un ejemplo de un archivo principal para una aplicación Flask.

`run.py`
~~~python
from todor import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
~~~

- La primera línea `from todor import create_app` importa la función `create_app` desde el módulo `todor`. Esta función se utiliza para crear una instancia de la aplicación Flask.

- El código que se encuentra dentro del bloque `if __name__ == '__main__'`: se ejecutará solo si este archivo se ejecuta directamente. Esto significa que si este archivo se importa como un módulo en otro archivo, el código dentro del bloque if no se ejecutará.

- En el interior del bloque if, se crea una nueva instancia de la aplicación Flask llamando a la función `create_app`. El resultado de la función se almacena en la variable `app`.

- Finalmente, se llama a la función `app.run()` para ejecutar la aplicación. La función `run` inicia un servidor web local en el que se puede acceder a la aplicación desde un navegador web en la dirección http://localhost:5000/.

En resumen, este código muestra cómo importar una función que crea una aplicación Flask y cómo ejecutar la aplicación. También muestra cómo usar un bloque `if __name__ == '__main__'`: para asegurarse de que el código solo se ejecute cuando se ejecuta directamente este archivo y no cuando se importa como un módulo en otro archivo.


---
## Blueprint y Vistas
Blueprint es una característica de Flask que permite organizar y separar las vistas de una aplicación Flask en módulos independientes. Cada Blueprint es un objeto que define un conjunto de rutas y funciones vistas asociadas.

Un Blueprint puede registrarse en la aplicación Flask principal para hacer que sus rutas y vistas estén disponibles en la aplicación. Esto permite que los desarrolladores organizan su código en módulos separados que pueden ser reutilizados en diferentes aplicaciones Flask.

Además, los Blueprints también permiten una mayor flexibilidad y escalabilidad en la estructuración de una aplicación Flask, lo que facilita la mantenibilidad y la gestión de código a largo plazo.

### Crea vistas con Blueprint

El código que proporciono es un ejemplo de una implementación de un Blueprint en Flask.


`todo.py`
~~~python
from flask import Blueprint

bp = Blueprint('todo', __name__)

@bp.route('/')
def index():
    return 'Página principal'

@bp.route('/todo/create')
def create():
    return 'Página de crear todo'

@bp.route('/todo/update')
def update():
    return 'Página de editar todo'
~~~

- `from flask import Blueprint`: importa la clase Blueprint de Flask, que se utiliza para crear un blueprint o plantilla para una aplicación Flask.

- `bp = Blueprint('todo', __name__)` crea una nueva instancia de Blueprint y la asigna a la variable bp. El primer argumento `'todo'` es el nombre del blueprint y el segundo argumento `__name__` es el nombre del módulo actual.

- `@bp.route('/')` es un decorador que indica que la función index es un controlador de rutas que maneja la ruta raíz '/' del blueprint bp.

- `def index()`: define la función index que se invoca cuando se accede a la ruta raíz del blueprint.

return 'Página principal' devuelve una respuesta con el texto "Página principal" para la ruta raíz.

Para utilizar este blueprint en una aplicación Flask, debe registrarlo en la aplicación Flask. Por ejemplo:

`__ini__.py`
~~~python
# Registrar Bluprint
from . import todo
app.register_blueprint(todo.bp)
~~~


El tercer argumento `url_prefix='/auth'` es un prefijo que se aplica a todas las rutas registradas en este blueprint.

Por ejemplo, si una ruta es definida `como @bp.route('/login')` en el blueprint auth, su URL será `/auth/login`.

`auth.py`
~~~python
from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix = '/auth')

@bp.route('/register')
def register():
    return 'Página register'

@bp.route('/login')
def login():
    return 'Página login'

@bp.route('/logout')
def logout():
    return 'Página de logout'
~~~

`__ini__.py`
~~~python
# Registrar Bluprint
from . import auth
app.register_blueprint(auth.bp)
~~~

---









