from myblog import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100))
    info = db.Column(db.Text)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, author, title, info, content) -> None:
        self.author = author
        self.title = title
        self.info = info
        self.content = content

    def __repr__(self) -> str:
        return f'Post: {self.title}'