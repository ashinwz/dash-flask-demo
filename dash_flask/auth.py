from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import url_for, request
from werkzeug.urls import url_parse
from flask_login import current_user
from flask_login import login_required, login_manager, login_user, logout_user, current_user
from . import forms
from . import User

auth = Blueprint('auth', __name__, url_prefix='/')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/dashapp/'))

    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.User()
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template("login.html", title='Sign In', form=form, error="error")


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return "logout"