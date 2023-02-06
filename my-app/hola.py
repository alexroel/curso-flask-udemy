from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    #Creando rutas 
    print(url_for('index'))
    print(url_for('hola'))
    print(url_for('code', code = 'print(code)'))
    return render_template('index.html')


@app.route('/hola', methods = ['GET', 'POST'])
def hola():
    print(request.form)
    nombre = None
    edad = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        print(nombre, type(edad))

        if edad == '':
            edad = None
        else:
            edad = int(edad)
    return render_template('hola.html', nombre= nombre, edad = edad)


#from markupsafe import escape

@app.route('/<path:code>')
def code(code):
    return render_template('code.html', code = code)


# if __name__ == '__main__':
#     app.run(debug=True, port=3000, host='localhost')