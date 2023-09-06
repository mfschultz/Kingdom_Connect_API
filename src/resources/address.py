from database import db
from flask_restful import Resource, request
from schemas.address import AddressSchema
from services.address import get_address, get_addresses_by_business, get_all_addresses, create_address, delete_address

class AddressResource(Resource):

    def get(self, address_id=None, business_id=None):
        if address_id:
            json_result = AddressSchema().dump(
                get_address(address_id)
            )
        elif business_id:
            json_result = AddressSchema(many=True).dump(
                get_addresses_by_business(business_id)
            )
        else:
            json_result = AddressSchema(many=True).dump(
                get_all_addresses()
            )
        return json_result, 200
    
    def post(self):
        address = create_address(
            AddressSchema().load(request.get_json(), session=db.session)
        )
        return AddressSchema().dump(address), 201
    
    # def put(self, address_id):
    #     result = update_address( 
    #         AddressSchema(partial=True).load(request.get_json(), session=db.session), 
    #         address_id=address_id
    #     )
    #     return result, 201
    
    def delete(self, address_id):
        address = get_address(address_id)
        if address:
            delete_address(address)
        return {}, 204

