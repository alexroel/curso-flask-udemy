from flask import (render_template, Blueprint)

from myblog.blog.models import Post

from myblog import db

from myblog.blog.views import get_user

bp = Blueprint('posts', __name__)

@bp.route('/')
def index():
    posts = Post.query.all()
    posts = list(reversed(posts))
    db.session.commit()
    return render_template('index.html', posts = posts, get_user=get_user)

@bp.route('/blog/<int:id>', methods=('GET','POST'))
def blog(id):
    post = Post.query.get(id)
    return render_template('blog.html', post = post, get_user=get_user)
