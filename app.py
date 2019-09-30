from flask import Flask
from local_values.reader import env_value
from flask import flash, render_template, redirect, url_for, request, session
from models import User
from forms import UserForm
from settings import Session

app = Flask(__name__)
app.debug = env_value('DEBUG', default='False')
app.secret_key = env_value('SECRET_KEY')


@app.route('/')
def profile_info(user=None):
    if ('login' and 'password') in session:
        return render_template('profile.html')
    else:
        return redirect(url_for('login_post'))


@app.route('/login', methods=['GET', 'POST'])
def login_post():
    if ('login' and 'password') in session:
        return redirect(url_for('profile_info'))
    form = UserForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)

    login = form.login.data
    password = form.password.data
    db_session = Session()
    user = db_session.query(User).filter_by(email=login).first()

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
def logout():
    session.clear()
    return 'Logout'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
