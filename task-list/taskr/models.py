from taskr import db
from datetime import datetime

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.Text)

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
  
    def __repr__(self) -> str:
        return f'User: {self.username}'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    desc = db.Column(db.Text)
    completed = db.Column(db.Boolean)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __init__(self, created_by, desc, completed) -> None:
        self.created_by = created_by
        self.desc = desc
        self.completed = completed

    def __repr__(self) -> str:
        return f'Post: {self.desc}'
