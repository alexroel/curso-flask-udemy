import pytest
from flask import g, session
from myblog import db
from myblog.auth.models import User
from myblog.blog.models import Post


# TEST AUTH REGISTER
def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    #response.headers["Location"] == "/auth/login"
    response.request.path == "/auth/login"
    with app.app_context():
        users = User.query.all()
        print(users)
        db.session.add(User('alex', 'alex'))
        db.session.commit()
   
@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    message in response.data


# TEST AUTH LOGIN
def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    response.request.path == "/blog/blogs"
    #assert response.headers["Location"] == "/blog/blogs"
    with client:
        client.get('/blog/blogs')
        assert session['user_id'] == 1

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    message in response.data


# TEST AUTH LOGOUT
def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session