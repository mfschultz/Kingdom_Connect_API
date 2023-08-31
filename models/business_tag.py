from app import db
from sqlalchemy.dialects.mysql import INTEGER

class BusinessTag(db.Model):
    business_id = db.Column(INTEGER, db.ForeignKey('business.id'))
    tag_id = db.Column(INTEGER, db.ForeignKey('tag.id'))