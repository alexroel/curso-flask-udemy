from flask import (
    render_template, Blueprint,  g, redirect, request, url_for
    )

from .models import User, Todo
from . import db

from .auth import login_required

bp = Blueprint('todo', __name__, url_prefix='/todo')

#Obtner un ususario
def get_user(id):
    user = User.query.get_or_404(id)
    return user

@bp.route('/list')
@login_required
def index():
    todos = Todo.query.all()   
    return render_template('todo/index.html', todos=todos)

@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        
        post = Todo(g.user.id, title, desc)

        db.session.add(post)
        db.session.commit()
        return redirect(url_for('todo.index'))

    return render_template('todo/create.html')


def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo


@bp.route('/update/<int:id>', methods=('GET','POST'))
@login_required
def update(id):

    todo = get_todo(id)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        todo.state = True if request.form.get('state') == 'on' else False

        # db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))

    return render_template('todo/update.html', todo = todo)


#Eliminar un post
@bp.route('/blog/delete/<int:id>')
@login_required
def delete(id):
    todo = get_todo(id)
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('todo.index'))