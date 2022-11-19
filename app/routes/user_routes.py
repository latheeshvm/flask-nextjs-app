import bcrypt
from flask import Blueprint, render_template, request, session, current_app


bp_user = Blueprint("bp_user", __name__)
db = current_app.config["db"]


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
            db.insert_one(
                {"email": str(email), "password": str(password_hash)})
            session.pop("email", None)
            session['email'] = str(email)
            # return redirect(url_for(''))
        except:
            print("Error in inserting")

    print(session)

    if 'username' in session:
        return 'You are logged in ' + session['username']

    return render_template('server/pages/signup.html')
