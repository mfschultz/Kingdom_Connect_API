from utils.database import db
from sqlalchemy import String
from sqlalchemy_utils import EmailType, UUIDType
import uuid

class User(db.Model):
    id = db.Column(UUIDType(), primary_key=True, default=uuid.uuid4())
    username = db.Column(String(64), unique=True, nullable=False)
    email = db.Column(EmailType, unique=True, nullable=False)

    def __repr__(self):
        return f'<User "{self.username}">'    