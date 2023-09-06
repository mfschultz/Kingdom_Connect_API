from models.user import User
from utils.database import db

def get_user(user_id):
    user = User.query.get(user_id)
    return user

def get_all_users():
    users = User.query.all()
    return users

def create_user(user):
    db.session.add(user)
    db.session.commit()
    return user

def delete_user(user):
    db.session.delete(user)
    db.session.commit()