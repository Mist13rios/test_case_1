from local_values.reader import env_value
from flask import Flask, flash, render_template, redirect, url_for, request, session
from models import User
from forms import UserForm
from settings import Session
from api.User import api_bp
from auth import auth_check


app = Flask(__name__)
app.debug = env_value('DEBUG', default='False')
app.secret_key = env_value('SECRET_KEY')

app.register_blueprint(api_bp)
db_session = Session()


@app.route('/')
@auth_check
def profile_info(user=None):
    user = db_session.query(User).filter_by(email=session['login'], password=session['password']).first()
    return render_template('profile.html', user=user, page_name='Profile')


@app.route('/login', methods=['GET', 'POST'])
def login_post():
    form = UserForm()
    if request.method == 'GET':
        return render_template('login.html', form=form, page_name='Login')

    login = form.login.data
    password = form.password.data
    user = db_session.query(User).filter_by(email=login, password=password).first()

    if not user:
        flash('No existing user')
        return redirect(url_for('login_post'))
    elif not form.validate():
        flash('Wrong login or password')
        return redirect(url_for('login_post'))

    session['login'] = login
    session['password'] = password

    return redirect(url_for('profile_info'))


@app.route('/logout')
@auth_check
def logout():
    session.clear()
    return redirect(url_for('login_post'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
