from models.business_tag import BusinessTag
from utils.database import db

def get_business_tag(business_id, tag_id):
    business_tag = db.session.query(BusinessTag).filter_by(business_id=business_id, tag_id=tag_id).first()
    return business_tag

def get_all_by_business(business_id):
    business_tags = db.session.query(BusinessTag).filter_by(business_id=business_id).all()
    return business_tags

def get_all_by_tag(tag_id):
    business_tags = db.session.query(BusinessTag).filter_by(tag_id=tag_id).all()
    return business_tags

def get_all_business_tags():
    business_tags = BusinessTag.query.all()
    return business_tags

def create_business_tag(business_tag):
    db.session.add(business_tag)
    db.session.commit()
    return business_tag

def delete_business_tag(business_tag):
    db.session.delete(business_tag)
    db.session.commit()