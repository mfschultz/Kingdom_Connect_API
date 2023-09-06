from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.tag import Tag

class TagSchema(SQLAlchemySchema):
    class Meta:
        model = Tag
        load_instance = True

    id = auto_field(dump_only=True)
    name = auto_field(required=True)
    