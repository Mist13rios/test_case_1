from functools import wraps
from flask import redirect, url_for, session


def auth_check(fn):
    @wraps(fn)
    def decoration(*args, **kwargs):
        if ('login' and 'password') in session:
            return fn(*args, **kwargs)
        else:
            return redirect(url_for('login_post'))
    return decoration
