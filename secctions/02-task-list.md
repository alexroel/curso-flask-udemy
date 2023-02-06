# Proyecto: Lista de Tareas 


---
## Presentación del Proyecto 
Presenta el prpyecto como va quedar al final 


---
## Crea el proyecto 

1. Crea el prpyecto `task-list`
2. Crea el entorno virtual para el proyecto y activa
3. Instala flask para tu proyecto
4. Crea un paquete principal con nombre de `taskr`
5. Dentro crea el archivo `__init__.py`
6. En el archivo `__init__.py` realiza el hola mundo con flask. 
7. Ejecuta la aplicación con siguiente comando `flask --app taskr run`


~~~python
from flask import Flask

app = Flask(__name__)

# Una simple vista de prueva
@app.route('/hola')
def hola():
        return 'Hello, World!'

return app
~~~
---
## Configuración del Proyecto

Configuración de nuestro proyecto 

1. Crea una función con nombre `create_app`, para crear instancias de nuestro apliacación como para testing. 
2. `app.config.mapping` contiene la configuración de nuestra aplicación como de base de datos, clave secreta, y mas. 
3. Configura clave secreta `SECRET_KEY` y base de datos `DATABASE`

~~~python
from flask import Flask

def create_app():
    # Crea y configura la aplicación
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = 'ruta_db'
    )

    # Una simple vista de prueva
    @app.route('/hola')
    def hola():
        return 'Hello, World!'

    return app
~~~

---
## Crear conexión a Base de datos 

1. Instalar el paquete `Flask-SQLAlchemy`
2. Realizar la configuración para la conexión a base de datos 

~~~python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crear la extención
db = SQLAlchemy()

def create_app():
    # create and configure the app
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        #configurar la base de datos SQLite, relativa a la carpeta de la instance  
        SQLALCHEMY_DATABASE_URI = "sqlite:///tasklist.db",
    )
    db.init_app(app)# inicializar la aplicación con la extensión
    

    # Una simple vista de prueva
    @app.route('/hola')
    def hola():
        return 'Hello, World!'

    
    with app.app_context():
        db.create_all()
    return app
~~~

---
## Crar modelos para base de datos 

Crear modelos de usuario  y tareas 

~~~python
from taskr import db
from datetime import datetime

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.Text)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    desc = db.Column(db.Text)
    completed = db.Column(db.Boolean)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
~~~
Después de definir todos los modelos y tablas, llame SQLAlchemy.create_all()para crear el esquema de tabla en la base de datos. 



~~~python
    app = Flask(__name__)
    ...

    # Crea los modelos 
    from . import models 

    with app.app_context():
        db.create_all()

    return app
~~~

--- 
### Blueprint y Views

1. Crea un archivo para las vistas de `auth`, como 'auth.py'
2. Importa todo los moduloes que se van usar mas adelante 
3. Crea un plano para esta vista con Blueprint
4. Crea las vista con Blueprint 

~~~python
from flask import (
    Blueprint, render_template, request, 
    url_for, g, flash,session
)

from werkzeug.security import check_password_hash, generate_password_hash

from .models import User

# Crear plano de la vista 
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Mis Vistas 
@bp.route('/register')
def register():
    return 'Registrar usuario'

@bp.route('/login')
def login():
    return 'Incio de sesión'

@bp.route('/logout')
def logout():
    return 'Sesión serrada'
~~~

Registrar plano en la aplicación 

~~~python 
# Registrar plano de auth
from . import auth
app.register_blueprint(auth.bp)
~~~
---
## Plantilla de Auth

1. Crea un archivo html `base.html` dentro de carpeta `templates`
2. Codifica el siguiente código 
3. Crea una vista para probar

`base.html`
~~~html
<!DOCTYPE html>

<title>Task list - {% block title %}{% endblock %}</title>

<nav>
    <h1>Task List</h1>

    <ul>
        <!-- Sesión iniciada  -->
        {% if Flase %}
        <li><samp>alexroel</samp></li>
        <li><a href="">Cerrar sesión</a></li>
        {% else %}
        <li><a href="">Registrate</a></li>
        <li><a href="">Iniciar sesión</a></li>
        {% endif %}
    </ul>
</nav>

<section class="content">
    <header>
        {% block header %}{% endblock %}
    </header>
    {% block content %} {% endblock %}
</section>
~~~

´register.html´
~~~html
{% extends 'base.html' %}

{% block title %}Registrar usuario{% endblock %}

{% block header %}
<h1>Registrar Usuario </h1>
{% endblock %}

{% block content %}
    <form action="" method="post">
        <label for="username">Nombre de usurio</label> <br>
        <input type="text" name="username" id="username"><br>

        <label for="password">Contraseña</label><br>
        <input type="password", name="password" id="password"><br>

        <br>
        <input type="submit" value="Registrar">

    </form>
{% endblock %}
~~~

´login.html´
~~~html
{% extends 'base.html' %}

{% block title %}Iniciar sesión{% endblock %}

{% block header %}
<h1>Iniciar Sesión </h1>
{% endblock %}

{% block content %}
    <form action="" method="post">
        <label for="username">Nombre de usurio</label> <br>
        <input type="text" name="username" id="username"><br>

        <label for="password">Contraseña</label><br>
        <input type="password", name="password" id="password"><br>

        <br>
        <input type="submit" value="Iniciar sesión">

    </form>
{% endblock %}
~~~

---
## Registrar usuario