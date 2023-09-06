from utils.database import db
from sqlalchemy import String, Boolean
from sqlalchemy.dialects.sqlite import INTEGER

class Address(db.Model):
    id = db.Column(INTEGER, primary_key=True)
    business_id = db.Column(INTEGER, db.ForeignKey("business.id"), nullable=False)
    street_address = db.Column(String(64), unique=True, nullable=False)
    city = db.Column(String(64), nullable=False)
    state_code = db.Column(String(2), nullable=False)
    zip_code = db.Column(String(5), nullable=False)
    is_public = db.Column(Boolean, nullable=False)