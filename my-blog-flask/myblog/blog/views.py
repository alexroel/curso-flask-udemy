from flask import (
    render_template, Blueprint, 
    flash, g, redirect, request, url_for
    )

from werkzeug.exceptions import abort
from .models import Post
from myblog.auth.models import User

from myblog.auth.views import login_required

from myblog import db

bp = Blueprint('blog', __name__, url_prefix='/blog')

#Obtner un ususario
def get_user(id):
    user = User.query.get_or_404(id)
    return user

@bp.route('/blogs')
@login_required
def blogs():
    posts = Post.query.all()
    posts = list(reversed(posts))
    db.session.commit()

    return render_template('blog/blogs.html', posts = posts, get_user=get_user)

@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        info = request.form.get('info')
        content = request.form.get('ckeditor')

        post = Post(g.user.id, title, info, content)

        # Validación de datos 
        error = None
        if not title:
            error = 'Se requiere un título'
        
        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.blogs'))

        flash(error)

    return render_template('blog/create.html')

# Obtener post por Id
def get_post(id, check_author=True):
    post = Post.query.get(id)

    if post is None:
        abort(404, f'Id {id} de la publicación no existe.')

    if check_author and post.author != g.user.id:
        abort(404)
    
    return post

# Editar post
@bp.route('/update/<int:id>', methods=('GET','POST'))
@login_required
def update(id):
    post = get_post(id) 

    if request.method == 'POST':
        post.title = request.form.get('title')
        post.info = request.form.get('info')
        post.content = request.form.get('ckeditor')

        error = None
        if not post.title:
            error = 'Se requiere un título'
        
        if error is not None:
            flash(error)
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.blogs'))
        
        flash(error)

    return render_template('blog/update.html', post=post)

#Eliminar un post
@bp.route('/blog/delete/<int:id>')
@login_required
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('blog.blogs'))