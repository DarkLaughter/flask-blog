from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from blog import db
from blog.models import User, Post
from blog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from blog.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)


# registration
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User.(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration Sucessful')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

# Log In


# Log Out
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))

# Account


# Users list of Blog Posts
