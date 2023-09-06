from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.business_tag import BusinessTag

class BusinessTagSchema(SQLAlchemySchema):
    class Meta:
        model = BusinessTag
        load_instance = True

    business_id = auto_field(required=True)
    tag_id = auto_field(required=True)
    