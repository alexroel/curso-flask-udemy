from flask import (
    Blueprint, render_template, request, 
    url_for, flash, redirect, session
)

from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .models import User

# Crear plano de la vista 
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Mis Vistas 
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username, generate_password_hash(password))

        #Validar datos 
        error = None
        if not username:
            error = 'Se requiere nombre de usuario'
        elif not password:
            error = 'Se requiere contraseña'

        # Comparando nombre de usuario con los existentes
        user_name = User.query.filter_by(username = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'El usuario {username} ya esta registrado'
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET','POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validando datos 
        error = None
        user = User.query.filter_by(username = username).first()

        if user == None:
            error = 'Nombre de usuario incorrecto'
        elif not check_password_hash(user.password, password):
            error = 'Contraseña incorrecta'

        # Iniciando sesion
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('auth.task'))
        
        flash(error)
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    return 'Sesión serrada'



