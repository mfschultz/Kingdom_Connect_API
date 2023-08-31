from app import db
from sqlalchemy import String
from sqlalchemy.dialects.mysql import TINYINT

class Tag(db.model):
    id = db.Column(TINYINT, primary_key=True)
    name = db.Column(String(16), unique=True, nullable=False)

    def __repr__(self):
        return f'<Tag "{self.name}">'