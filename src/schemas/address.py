from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from models.address import Address


class AddressSchema(SQLAlchemySchema):
    class Meta:
        model = Address
        load_instance = True

    id = auto_field(dump_only=True)
    business_id = auto_field(required=True)
    street_address = auto_field(required=True)
    city = auto_field(required=True)
    state_code = auto_field(required=True)
    zip_code = auto_field(required=True)
    is_public = auto_field(required=True)