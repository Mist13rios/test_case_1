# from sqlalchemy import Session
from flask_restful import Resource, Api

from app import app
api = Api(app)


class UserApi(Resource):

    def get(self, user_id):
        return {"hello': 'user_id"}

    def post(self, user_id):
        return {"waiting for new: 'user_id"}

    def put(self, user_id):
        return {"let's change something': 'user_id"}

    def delete(self, user_id):
        return {"deleted user': 'user_id"}

api.add_resource(UserApi, "/user/<string:user_id>")
