from utils.database import db
from flask_restful import Resource, request
from schemas.tag import TagSchema
from services.tag import get_tag, get_all_tags, create_tag, delete_tag


class TagResource(Resource):
    
    def get(self, tag_id=None): 
        if tag_id:
            json_result = TagSchema().dump(
                get_tag(tag_id)
            )
        else:
            json_result = TagSchema(many=True).dump(
                get_all_tags()
            )
        return json_result, 200
    
    def post(self):
        saved = create_tag(
            tag=TagSchema().load(request.get_json(), session=db.session)
        )
        return TagSchema().dump(saved), 201
    
    def delete(self, tag_id):
        tag = get_tag(tag_id)
        if tag:
            delete_tag(tag)
        return {}, 204