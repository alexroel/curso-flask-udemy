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


# if __name__ == '__main__':
#     app.run(debug=True, port=3000, host='localhost')