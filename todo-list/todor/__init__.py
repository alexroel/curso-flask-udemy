from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Crear una extención 
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    #Configuración de poyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"
    )
    db.init_app(app)

    # Registrar Bluprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)


    # Vista de página de inicio
    @app.route('/')
    def index():
        return render_template('index.html')

    # Migra los modelos a  base de datos
    with app.app_context():
        db.create_all()
        
    return app