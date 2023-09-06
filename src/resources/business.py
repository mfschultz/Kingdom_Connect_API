from database import db
from flask_restful import Resource, request
from schemas.business import BusinessSchema
from services.business import get_business, get_all_businesses, save_business, delete_business


class BusinessResource(Resource):
    
    def get(self, business_id=None): 
        if business_id:
            json_result = BusinessSchema().dump(
                get_business(business_id)
            )
        else:
            json_result = BusinessSchema(many=True).dump(
                get_all_businesses()
            )
        return json_result, 200
    
    def post(self):
        saved = save_business(
            business=BusinessSchema().load(request.get_json(), session=db.session)
        )
        return BusinessSchema().dump(saved), 201
    
    def put(self, business_id):
        result = save_business( 
            BusinessSchema(partial=True).load(request.get_json(), session=db.session), 
            business_id=business_id
        )
        return result, 201
    
    def delete(self, business_id):
        business = get_business(business_id)
        if business:
            delete_business(business)
        return {}, 204