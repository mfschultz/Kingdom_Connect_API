from app import db
from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy_utils import EmailType

class User(db.model, UserMixin):
    id = db.Column(INTEGER, primary_key=True)
    username = db.Column(String(64), unique=True, nullable=False)
    email = db.Column(EmailType, unique=True, nullable=False)

    def __repr__(self):
        return f'<User "{self.username}">'    