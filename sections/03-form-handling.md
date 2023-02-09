# Manejo de Formulario

1. [Introducción a los formularios](#Introducción-a-los-formularios)
2. [Crear formularios](#Crear-formularios)
3. [Validación de datos de formularios](#Validación-de-datos-de-formularios)
4. [Formulario con WTForms](#Formulario-con-WTForms)
5. [Validación de datos con WTForm](#Validación-de-datos-con-WTForm)

---
## Introducción a los formularios

Los formularios son una parte importante de cualquier aplicación web, ya que permiten recibir y enviar información del usuario. En Flask, los formularios se pueden crear usando HTML y CSS, pero también existen bibliotecas que facilitan el proceso y añaden características adicionales como la validación de datos y la protección contra ataques.

Los formularios son importantes en Flask porque te permiten interactuar con el usuario de manera más efectiva. Por ejemplo, puedes crear formularios de inicio de sesión para que los usuarios puedan iniciar sesión en tu aplicación, formularios de registro para que los usuarios puedan crear una cuenta, formularios de búsqueda para que los usuarios puedan buscar información en tu aplicación, entre otros.

Además, los formularios son una parte crucial de cualquier aplicación web, ya que te permiten recoger y procesar información del usuario, lo que es esencial para la mayoría de las aplicaciones. Por ejemplo, puedes usar formularios para recoger información de una encuesta, para procesar una transacción en una tienda en línea, para publicar un nuevo mensaje en un foro, etc.

---
## Crear formularios
La creación de formularios simples con HTML y Flask se puede hacer mediante el siguiente proceso:

1. Crear un archivo HTML que contenga la estructura del formulario:
    
    ~~~html
    <h1>Registrar Usuario </h1>
    <form action="" method="post">
        <label for="username">Nombre se usuario: </label>
        <input type="text" name="username" id="username">
        <br>
        <label for="password">Contraseña: </label>
        <input type="password" name="password" id="password">
        <br>
        <input type="submit" value="Registrar">
    </form>
    ~~~
2. Definir una ruta en Flask que se encargará de manejar la solicitud del formulario:

    ~~~python
    from flask import Flask, render_template, request
    app = Flask(__name__)

    @app.route('/auth/register', methods = ['GET', 'POST'])
    def hello():
        print(request.form)
        username = None
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            print(username, password)
            return "Nombre de usuario: " + username + ", Contraseña: " + password

        return render_template('auth/register.html')
    ~~~

En este ejemplo, la ruta "/auth/register" maneja tanto solicitudes GET como POST. Si la solicitud es una solicitud POST, se extraen el nombre de usuario y la contraseña del formulario y se devuelven ambos valores. Si la solicitud es una solicitud GET, se devuelve la estructura HTML del formulario.

Es importante tener en cuenta que, aunque este es un ejemplo básico, en la vida real es necesario validar los datos del formulario antes de procesarlos y protegerse contra ataques como el Cross-Site Scripting (XSS) y el Cross-Site Request Forgery (CSRF). Esto se puede lograr con la ayuda de bibliotecas como WTForms.


---
## Validación de datos de formularios
La validación de datos de formularios es un paso importante en el procesamiento de formularios. Se utiliza para garantizar que los datos ingresados por el usuario sean válidos y seguros antes de procesarlos. En Flask, se puede realizar la validación de los datos de los formularios de varias maneras.

Aquí hay un ejemplo de código que explica cómo realizar la validación de datos de un formulario de registro de usuario en Flask sin WTForms:

~~~html
<h1>Registrar Usuario </h1>
<form action="" method="post">
    <label for="username">Nombre se usuario: </label>
    <input type="text" name="username" id="username">
    <br>
    <label for="password">Contraseña: </label>
    <input type="password" name="password" id="password">
    <br>
    <input type="submit" value="Registrar">
</form>

{% if error %}
  <p style="color: red;">{{ error }}</p>
{% endif %}
~~~

Definir una ruta en Flask que se encargará de manejar la solicitud del formulario:

~~~python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/auth/register', methods = ['GET', 'POST'])
def hello():
    print(request.form)
    username = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:
            return "Nombre de usuario: " + username + ", Contraseña: " + password
        else:
            error = "Nombre de usuario debe tener entre 4 y 25 caracteres y la contraseña debe tener entre 6 y 40 caracteres."
            return render_template("auth/register.html", error=error)

        

    return render_template('auth/register.html')
~~~

En este ejemplo, se valida que el nombre de usuario tenga entre 4 y 25 caracteres y la contraseña tenga entre 6 y 40 caracteres. Si los datos no son válidos, se muestra un mensaje de error.

---
## Formulario con WTForms
WTForms es una biblioteca que permite validar fácilmente los datos de los formularios y proporciona una capa adicional de seguridad contra ataques como el Cross-Site Scripting (XSS) y el Cross-Site Request Forgery (CSRF).

Aquí hay un ejemplo de código que explica cómo validar un formulario de registro de usuario en Flask con WTForms:

1. Instalar WTForms:
    ~~~
    pip install flask-wtf
    ~~~

2. Crear un archivo de formulario con WTForms
    ~~~python
    from flask_wtf import FlaskForm
    from wtforms import StringField, PasswordField, SubmitField
    from wtforms.validators import DataRequired, Length

    class RegisterForm(FlaskForm):
        username = StringField("Nombre de usuario")
        password = PasswordField("Contraseña")
        submit = SubmitField("Registrarse")
    ~~~
3. Definir una ruta en Flask que se encargará de manejar la solicitud del formulario:
    ~~~python
    @app.route("/auth/register", methods=["GET", "POST"])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            return "Nombre de usuario: " + username + ", Contraseña: " + password
        return render_template("auth/register.html", form=form)
    ~~~

4. Crear un archivo HTML que contenga la estructura del formulario:
    ~~~html
    <form action="" method="post">
        {{ form.hidden_tag() }}
        {{ form.username.label }} {{ form.username }}
        {{ form.password.label }} {{ form.password }}
        {{ form.submit }}
    </form>
    ~~~

---
## Validación de datos con WTForm
WTForms es una biblioteca de formularios de Python que facilita la validación de datos de formularios en aplicaciones Flask. Aquí hay un ejemplo de cómo se puede implementar la validación de datos en una aplicación Flask usando WTForms:

 ~~~python
    from flask_wtf import FlaskForm
    from wtforms import StringField, PasswordField, SubmitField
    from wtforms.validators import DataRequired, Length

    class RegisterForm(FlaskForm):
        username = StringField("Nombre de usuario", validators=[DataRequired(), Length(min=4, max=25)])
        password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6, max=40)])
        submit = SubmitField("Registrarse")
    ~~~




