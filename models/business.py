from app import db
from sqlalchemy import String
from sqlalchemy.dialects.mysql import VARCHAR, INTEGER, SMALLINT, BINARY
from sqlalchemy_utils import PhoneNumberType, EmailType
from business_tag import business_tag

class Business(db.model):
    id = db.Column(INTEGER, primary_key=True)
    owner_id = db.Column(INTEGER, nullable=False)
    name = db.Column(String(64), unique=True, nullable=False)
    description = db.Column(VARCHAR, nullable=False)
    phone_number = db.Column(PhoneNumberType, unique=True)
    email = db.Column(EmailType, unique=True)
    street_address = db.Column(String(128), unique=True, nullable=False)
    state = db.Column(INTEGER, db.ForeignKey('state.id'), nullable=False)
    zip_code = db.Column(SMALLINT, nullable=False)
    display_address = db.Column(BINARY, nullable=False)
    tags = db.relationship('Tag', secondary=business_tag, backref='businesses')

    def __repr__(self):
        return f'<Business "{self.name}">'