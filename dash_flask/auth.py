from flask import Blueprint
from flask_login import login_required, login_manager, login_user, logout_user
from . import User

auth = Blueprint('auth', __name__, url_prefix='/')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    user = User.User()
    login_user(user)
    return "login page"


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return "logout page"