from flask import Blueprint, request

login_blueprint = Blueprint("login", __name__)
user_blueprint = Blueprint("user", __name__)


@login_blueprint.route('/login', methods=["POST", "GET"])  ### 0
def login():
    if request.method == "POST":  ### 1
        nickname = request.form['nickname']  ### 2
        return redirect(url_for("user.user", nick=nickname))
    else:  ### 3
        return render_template("login.html")


@user_blueprint.route('/<nick>')
def user(nick):
    return f"<h1>Hello, {nick}</h>"
