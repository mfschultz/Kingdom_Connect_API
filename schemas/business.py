from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from models.business import Business
from schemas.user import UserSchema
from schemas.tag import TagSchema

class BusinessSchema(SQLAlchemySchema):
    class Meta:
        model = Business
        load_instance = True

    id = auto_field(dump_only=True)
    owner_id = auto_field(load_only=True)
    name = auto_field(required=True)
    description = auto_field(required=True)
    phone_number = auto_field()
    email = auto_field()
    website = auto_field()
    
    owner = fields.Nested(UserSchema)
    tags = fields.List(fields.Nested(TagSchema))