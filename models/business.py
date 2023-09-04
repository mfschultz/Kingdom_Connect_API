from database import db
from sqlalchemy import String
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER
from sqlalchemy_utils import PhoneNumberType, EmailType, UUIDType

class Business(db.Model):
    id = db.Column(INTEGER, primary_key=True)
    owner_id = db.Column(UUIDType(), db.ForeignKey("user.id"), nullable=False)
    name = db.Column(String(64), unique=True, nullable=False)
    description = db.Column(VARCHAR, nullable=False)
    phone_number = db.Column(PhoneNumberType, unique=True)
    email = db.Column(EmailType, unique=True)
    website = db.Column(String(128), unique=True)
    
    #Relationships
    owner = db.relationship('User')

    def __repr__(self):
        return f'<Business "{self.name}">'