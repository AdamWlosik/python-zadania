from datetime import datetime

from flask import Blueprint, request, session, redirect, render_template
from .models import Users
from . import db

login_blueprint = Blueprint("login", __name__)
registration_blueprint = Blueprint("registration", __name__)
home_page_blueprint = Blueprint("home_page", __name__)
logout_blueprint = Blueprint("logout", __name__)


@login_blueprint.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = Users.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["username"] = username
            return redirect('/home_page')
    return render_template('login.html')


@registration_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = Users(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('register.html')


@home_page_blueprint.route('/home_page')
def home_page():
    if 'username' in session:
        user = Users.query.filter_by(username=session['username']).first()
        days_since_registration = (datetime.now() - user.registered_on).days
        return f"Hello, {session['username']}. You’re with us for {days_since_registration} days."
