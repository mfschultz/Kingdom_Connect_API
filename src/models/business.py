from database import db
from sqlalchemy import String
from sqlalchemy.dialects.sqlite import VARCHAR, INTEGER
from sqlalchemy_utils import PhoneNumberType, EmailType, UUIDType
from models.tag import Tag
from models.address import Address
from models.business_tag import BusinessTag

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
    addresses = db.relationship('Address', backref='business')
    tags = db.relationship('Tag', secondary='business_tag', backref='businesses')

    def __repr__(self):
        return f'<Business "{self.name}">'