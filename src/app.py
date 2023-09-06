from flask import Flask
from flask_restful import Api
from utils.database import db

from resources.business import BusinessResource
from resources.user import UserResource
from resources.tag import TagResource
from resources.business_tag import BusinessTagResource
from resources.address import AddressResource


api = Api()

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kingdomconnect.db'
    db.init_app(app)
    api.init_app(app)
    return app

def setup_database(app):
    with app.app_context():
        db.create_all()

api.add_resource(UserResource, '/user', '/user/<string:user_id>')
api.add_resource(BusinessResource, '/business', '/business/<string:business_id>')
api.add_resource(TagResource, '/tag', '/tag/<string:tag_id>')
api.add_resource(BusinessTagResource, '/business_tag', '/business_tag/business/<string:business_id>', '/business_tag/tag/<string:tag_id>', '/business_tag/business/<string:business_id>/tag/<string:tag_id>')
api.add_resource(AddressResource, '/address', '/address/<string:address_id>', '/address/business/<string:business_id>')

if __name__== '__main__':
    app = create_app()
    setup_database(app)
    app.run()