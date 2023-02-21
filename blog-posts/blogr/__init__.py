from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crear extensón
db = SQLAlchemy()

def create_app():

    # Configuración de la plicación 
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    # Configuración CKEditor
    #Configuracion de CKEditor
    from flask_ckeditor import CKEditor 
    ckeditor = CKEditor(app)

    import locale
    # Establecer el idioma y la configuración regional en español
    locale.setlocale(locale.LC_ALL, 'es_ES')

    # Registro de Bluprint 
    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)

    from blogr import post
    app.register_blueprint(post.bp)


    with app.app_context():
        db.create_all()

    return app