from models.business import Business
from utils.database import db

def get_business(business_id):
    business = Business.query.get(business_id)
    return business

def get_all_businesses():
    businesses = Business.query.all()
    return businesses

def create_business(business):
    db.session.add(business)
    db.session.commit()
    return business

def delete_business(business):
    db.session.delete(business)
    db.session.commit()