import bcrypt
from flask import Blueprint, redirect, render_template, request,  current_app, session, url_for


bp_user = Blueprint("bp_user", __name__)
db = current_app.config["db"]
session = current_app.config["session"]


@bp_user.route('/login')
def login():
    if 'username' in session:
        return 'You are logged in ' + session['username']

    return render_template('server/pages/login.html')


@bp_user.route('/signup', methods=['GET'])
def signup():

    if request.method == "GET" and "email" in request.args:
        email = request.args["email"]
    else:
        email = ""

    if request.method == "GET" and "password" in request.args:
        password = request.args["password"]
    else:
        password = ""

    if request.method == "GET" and "enableSession" in request.args:
        enableSession = request.args["enableSession"]
    else:
        enableSession = False

    # TODO : Server Validation

    if request.method == "GET" and email and password:
        password_hash = bcrypt.hashpw(
            str(password).encode('utf-8'), bcrypt.gensalt())

        try:
            # TODO : Check if email already there, if there respond with an error
            data = db.insert_one(
                {"email": str(email), "password": str(password_hash)})

            if (data):
                session.pop("email", None)
                session["email"] = str(email)
                print(session)
                # TODO : Return Success
                # TODO : Wait for 2 seconds then redirect to index
                # return redirect(url_for(''))
        except Exception as e:
            print(e)
            print("Error in inserting")

    print(session)
    if 'email' in session:
        print("Executing this")
        return redirect(url_for('bp_index.index'))
    else:
        return render_template('server/pages/signup.html')
