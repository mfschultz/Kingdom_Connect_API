from utils.database import db
from flask_restful import Resource, request
from schemas.user import UserSchema
from services.user import get_user, get_all_users, create_user, delete_user


class UserResource(Resource):

    def get(self, user_id=None): 
        if user_id:
            json_result = UserResource().dump(
                get_user(user_id)
            )
        else:
            json_result = UserResource(many=True).dump(
                get_all_users()
            )
        return json_result, 200

    def post(self):
        new_user = create_user(
            user=UserSchema().load(request.get_json(), session=db.session)
        )
        return UserSchema().dump(new_user), 201

    def delete(self, user_id):
        user = get_user(user_id)
        if user:
            delete_user(user)
        return {}, 204