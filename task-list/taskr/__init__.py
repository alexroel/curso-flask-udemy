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

    # Crea los modelos 
    from . import models
    
    # Registrar plano de auth
    from . import auth
    app.register_blueprint(auth.bp)

    with app.app_context():
        db.create_all()

    return app