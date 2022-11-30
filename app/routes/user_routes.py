import bcrypt
from flask import Blueprint, jsonify, make_response, redirect, render_template, request,  current_app, session, url_for

bp_user = Blueprint("bp_user", __name__)
db = current_app.config["db"]
session = current_app.config["session"]


@bp_user.route('/login')
def login():
    if 'username' in session:
        return 'You are logged in ' + session['username']

    return render_template('server/pages/login.html')


@bp_user.route('/signup', methods=['POST', 'GET'])
def signup():

    if request.method == "POST" and "email" in request.args:
        email = request.args["email"]
    else:
        email = ""

    if request.method == "POST" and "password" in request.args:
        password = request.args["password"]
    else:
        password = ""

    if request.method == "POST" and "enableSession" in request.args:
        enableSession = request.args["enableSession"]
    else:
        enableSession = False

    # TODO : Server Validation

    if request.method == "POST" and email and password:

        try:
            email_check = db.find_one({"email": str(email)})

            if email_check:
                return make_response(jsonify({"error": "User already exists"}), 422)
            else:
                password_hash = bcrypt.hashpw(
                    str(password).encode('utf-8'), bcrypt.gensalt())
                data = db.insert_one(
                    {"email": str(email), "password": str(password_hash)})

                if (data):
                    session.pop("email", None)
                    session["email"] = str(email)
                    print(session)

                return make_response(jsonify({"success": "User Registred"}), 200)
        except Exception as e:
            return make_response(jsonify({"error": "Server eroror"}), 404)

    if 'email' in session:
        return redirect(url_for('bp_index.index'))
    else:
        return render_template('server/pages/signup.html')
