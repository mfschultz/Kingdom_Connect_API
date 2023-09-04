from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.user import User

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field(dump_only=True)
    username = auto_field(required=True)
    email = auto_field(required=True)
    