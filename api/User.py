from settings import Session
from flask import Blueprint, session, redirect, url_for
from flask_restful import Resource, Api
from auth import auth_check
from models import User

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
db_session = Session()


class UserApi(Resource):

    def get(self, user_id):
        if ('login' and 'password') not in session:
            # TODO добавить код ошибки, 403, так как https не настроен
            return {"Message": "Permission denied"}
        user = db_session.query(User).filter_by(email=session['login'], password=session['password']).first()
        return {"Message": "Hello mr.{} {}, our user # {}".format(user.first_name, user.last_name, user_id)}

    @auth_check
    def post(self, user_id):
        # TODO добавить валидацию формы и сообщения ошибок
        return {"waiting for new": "user_id"}

    @auth_check
    def put(self, user_id):
        return {"let's change something": "user_id"}

    @auth_check
    def delete(self, user_id):
        return {"deleted user": "user_id"}


api.add_resource(UserApi, "/api/user/<string:user_id>")

