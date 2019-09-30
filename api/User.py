from settings import Session
from flask import Blueprint, session, redirect, url_for
from flask_restful import Resource, Api
from auth import auth_check
from models import User
from forms import NewUserForm

api_bp = Blueprint('api', __name__)
api = Api(api_bp)
db_session = Session()


class UserApi(Resource):

    def get(self, user_id):
        if ('login' and 'password') not in session:
            return {"fail": "Permission denied"}, 403  # Добавлен 403 код, так как https не настроен для 401
        user = db_session.query(User).filter_by(email=session['login'], password=session['password']).first()
        return {"success": "Hello mr.{} {}, our user # {}".format(user.first_name, user.last_name, user_id)}

    @auth_check
    def post(self, email, password, first_name, last_name):
        new_user_form = NewUserForm(email, password, first_name, last_name)
        if new_user_form.validate_on_submit():
            new_user = User(email, password, first_name, last_name)
            db_session.add(new_user)
            db_session.commit()
            return {'success': 'added user with id - {}'.format(new_user.id)}
        else:
            return {"fail": "wrong format"}

    @auth_check
    def put(self, user_id, field, value):

        user = db_session.query(User).get(user_id)
        setattr(user, field, value)
        return {'success': 'user field {} changed to {}'.format(field, getattr(user, field))}

    @auth_check
    def delete(self, user_id):
        db_session.query(User).filter(User.id == user_id).delete()
        return {"success": "User deleted"}


api.add_resource(UserApi, "/api/user/<string:user_id>")

