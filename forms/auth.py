from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])