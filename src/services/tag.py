from models.tag import Tag
from utils.database import db

def get_tag(tag_id):
    tag = Tag.query.get(tag_id)
    return tag

def get_all_tags():
    tags = Tag.query.all()
    return tags

def create_tag(tag):
    db.session.add(tag)
    db.session.commit()
    return tag

def delete_tag(tag):
    db.session.delete(tag)
    db.session.commit()