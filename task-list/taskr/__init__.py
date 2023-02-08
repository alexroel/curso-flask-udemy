import os
from flask import Flask

def create_app():

    # Crea y configura la aplicación
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABSE = os.path.join(app.instance_path, 'task_list.db')
    )

    # Asegura de que exista al carpeta instance
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Una vista simple de prueva
    @app.route('/hola')
    def hola():
        return "Hola Mundo"

    # Configuración de db
    from . import db
    db.init_app(app)

    return app