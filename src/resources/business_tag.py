from database import db
from flask_restful import Resource, request
from schemas.business_tag import BusinessTagSchema
from services.business_tag import get_business_tag, get_all_business_tags, get_all_by_business, get_all_by_tag, create_business_tag, delete_business_tag


class BusinessTagResource(Resource):
    
    def get(self, business_id=None, tag_id=None): 
        if business_id and tag_id:
            json_result = BusinessTagSchema().dump(
                get_business_tag(business_id, tag_id)
            )
        elif business_id:
            json_result = BusinessTagSchema(many=True).dump(
                get_all_by_business(business_id)
            )
        elif tag_id:
            json_result = BusinessTagSchema(many=True).dump(
                get_all_by_tag(tag_id)
            )
        else:
            json_result = BusinessTagSchema(many=True).dump(
                get_all_business_tags()
            )
        return json_result, 200
    
    def post(self):
        saved = create_business_tag(
            business_tag=BusinessTagSchema().load(request.get_json(), session=db.session)
        )
        return BusinessTagSchema().dump(saved), 201
    
    def delete(self, business_id, tag_id):
        business_tag = get_business_tag(business_id=business_id, tag_id=tag_id)
        if business_tag:
            delete_business_tag(business_tag)
        return {}, 204