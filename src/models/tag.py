from utils.database import db
from sqlalchemy import String
from sqlalchemy.dialects.sqlite import INTEGER

class Tag(db.Model):
    id = db.Column(INTEGER, primary_key=True)
    name = db.Column(String(16), unique=True, nullable=False)

    def __repr__(self):
        return f'<Tag "{self.name}">'