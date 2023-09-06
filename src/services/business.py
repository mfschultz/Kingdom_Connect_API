from models.business import Business
from database import db

def get_business(business_id):
    business = Business.query.get(business_id)
    return business

def get_all_businesses():
    businesses = Business.query.all()
    return businesses

def save_business(business, business_id=None):
    if business_id:
        # TODO: Create Update Business Functionality
        return None
    else:
        db.session.add(business)
    db.session.commit()
    return business

def delete_business(business):
    db.session.delete(business)
    db.session.commit()