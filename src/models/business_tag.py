from utils.database import db
from sqlalchemy.dialects.sqlite import INTEGER

class BusinessTag(db.Model):
    business_id = db.Column(INTEGER, db.ForeignKey('business.id'), primary_key=True)
    tag_id = db.Column(INTEGER, db.ForeignKey('tag.id'), primary_key=True)