# Introducción a Flask 


---
## Instalar Flask 
Pasos y guia de instalar Flask: https://flask.palletsprojects.com/en/2.2.x/installation/

---
## Hola Mundo en Flask

Hola Mundo en Flask 
~~~python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return '<h1>Hola Mundo!</h1>'
~~~

Ejecutar una plicacion en flask 

~~~
flask --app hello run
~~~

Cambiar el Host y puerto

~~~
flask --app hola run -p 3000 -h localhost
~~~

Cambiar a modo desarrollo

~~~
flask --app hola --debug run -p 3000 -h localhost
~~~


---
## Configuraciones básicas 

~~~ python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return '<h1>Hola Mundo!</h1>'

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='localhost')
~~~

Para ejecutar esta aplicación ya no los haces con los comandos de  Flask, si no lo haces directamente con Python. 

~~~
python hola.py
~~~

---
## Enrutamieto

~~~python 
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Página de inicio!</h1>'

@app.route('/hola')
@app.route('/hello')
def hola():
    return '<h1>Hola Mundo!</h1>'
~~~

- Las funciones tienen que ser distintas 
- Las rutas tienen que ser unicas para evitar conflictos 
- Pero se puede crear varias  rutas para una vista

---
## Variables en las Rutas 
Como capturar datos mediante URL 

~~~python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Página de inicio!</h1>'

@app.route('/hola')
@app.route('/hola/<nombre>')
@app.route('/hola/<nombre>/<int:edad>')
def hola(nombre=None, edad=None):
    
    if nombre == None and edad == None:
        return '<h1>Hola Mundo!</h1>'
    elif edad == None:
        return f'<h1>Hola, {nombre}!</h1>'
    else:
        return f'<h1>Hola, {nombre} el doble de tu edad es {edad * 2}!</h1>'
~~~

---
## Escape de HTML

- Flask devuelbe plantilla HTML por defecto 
- Si enviamos un PATH de HTML lo tomara como código 
- En salida deben escaparse para protegerse de los ataques de inyección

~~~python
from markupsafe import escape

@app.route('/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
~~~

---
## Rendirizando Plantillas de HTML 

` <script>alert("bad")</script> `

Archivo de Python

~~~python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hola')
@app.route('/hola/<nombre>')
@app.route('/hola/<nombre>/<int:edad>')
def hola(nombre = None, edad = None):
    return render_template('hola.html', nombre = nombre, edad = edad)


from markupsafe import escape

@app.route('/<path:code>')
def code(code):
    return render_template('code.html', code = code)
~~~

Plantilas de HTML, todo se carga desde la carpeta templates

`index.html`
~~~html
<!DOCTYPE html>
<h1>Página de inicio</h1>
~~~

`hola.html`
~~~html
<!DOCTYPE html>
{% if nombre is none and edad is none%}
    <h1>Hola Mundo!</h1>
{% elif edad is none %}
    <h1>Hola, {{ nombre }}!</h1>
{% else %}
    <h1>Hola, {{ nombre }} el doble de tu edad es {{ edad * 2 }}!</h1>
{% endif %}
~~~

`code.html`
~~~html
<!DOCTYPE html>
<h1>El código</h1>
<p>
    <code>{{ code }}</code>
</p>
~~~

---
## Archivos Estaticos 
Todo se carga desde la carpeta static 
~~~html
<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
~~~






