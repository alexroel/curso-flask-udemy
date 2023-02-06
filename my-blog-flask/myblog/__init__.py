from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Crear extencion de SQLAlchemy
db = SQLAlchemy()

# Crea y configura la aplicación
def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    #Configuracion de CKEditor
    from flask_ckeditor import CKEditor
    app.config['CKEDITOR_PKG_TYPE'] = 'full'
    ckeditor = CKEditor(app)

    

    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    # app.config.from_mapping(
    #         SECRET_KEY='dev',
    #         SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://postgres:123456@localhost:5432/myblog_db",
    #     )

    # app.config.from_mapping(
    #          SECRET_KEY='dev',
    #          SQLALCHEMY_DATABASE_URI="sqlite:///project.db",
    #      ) 

    #app.config.from_pyfile('config.py')
    app.config.from_object('config.DevConfig')
    


    # Configuración de base de datos
    db.init_app(app)   
    # db = SQLAlchemy(app)
    #Registrar vistas de posts 
    from .posts import views
    app.register_blueprint(views.bp)

    #Registrar vistas de auth
    from .auth import views
    app.register_blueprint(views.bp)

    #Registrar vistas de blogs
    from .blog import views
    app.register_blueprint(views.bp)

        #@app.route('/')
        #def hello():
        #    return 'Hola Mundo'

    #Generar cambios en base de datos 
    with app.app_context():
        db.create_all()
    
    return app
    