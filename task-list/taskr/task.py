from flask import (
    Blueprint, render_template, request, 
    url_for, flash, redirect, session
)

from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .models import User, Task

# Crear plano de la vista 
bp = Blueprint('task', __name__, url_prefix='/task')


#Obtner un ususario
def get_user(id):
    user = User.query.get_or_404(id)
    return user
    
@bp.route('/')
def index():
    posts = Task.query.all()
    posts = list(reversed(posts))
    db.session.commit()
    return render_template('index.html', posts = posts, get_user=get_user)

