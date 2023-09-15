from flask import render_template, session, redirect, url_for, flash
from . import main
from .. import db
from .forms import AuthForm, LoginForm
from .helpers import hash_password, is_password_complex, check_password, login_required
from ..models import User


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        print(username)

        user = User.query.filter_by(username=username).first()

        if user and check_password(password, user.password):
            session["user_id"] = user.id
            flash('Login Successful', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'error')
            return redirect(url_for("main.login"))

    return render_template("login.html", login_form=login_form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    auth_form = AuthForm()

    if auth_form.validate_on_submit():
        username = auth_form.username.data
        email = auth_form.email.data
        password = auth_form.password.data
        first_name = auth_form.first_name.data
        last_name = auth_form.last_name.data
        organization = auth_form.organization.data

        if is_password_complex(password) and password == auth_form.password.data:
            hashed_password = hash_password(password)
            user = User(username=username, email=email, password=hashed_password, first_name=first_name, last_name=last_name, organization=organization)

            db.session.add(user)
            db.session.commit()

            flash('Registration Successful. You can now login.', 'success')
            return redirect(url_for('main.login'))
        else:
            flash('Password and confirmation do not match or do not meet complexity requirements.', 'error')

    return render_template('register.html', auth_form=auth_form)

@main.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.login"))

@main.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    user = User.query.get(session["user_id"])

    return render_template("dashboard.html", user=user)