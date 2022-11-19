
import bcrypt
from pymongo import MongoClient
from flask import Flask, redirect, render_template, session, request, url_for
import os
from app.user.models import User


app = Flask(__name__, static_url_path="/_next", static_folder='_next')
app.secret_key = "57929HSBKK987M9JKK"


def init_db():
    _uri = str(os.environ.get('MONGO_SERVER_URI'))
    client = MongoClient(_uri)

    client.server_info()
    print("Hello")
    print("about")

    return client


with app.app_context():
    try:
        db = init_db()
        print(db)
        print("Sucessfully connected to database")
        mydb = db["Users"]
        mycol = mydb["user"]
        # mycol.insert_one({"name": "Jhon", "address": "Highway 37"})
    except:
        print("Error in connecting db")
        db = None


@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in ' + session['username']

    return render_template('server/pages/index.html')


@app.route('/login')
def login():
    if 'username' in session:
        return 'You are logged in ' + session['username']

    return render_template('server/pages/login.html')


@app.route('/signup', methods=['GET'])
def signup():

    # if(request.method)
    print(request.method)
    # eamil = ""
    # password = ""
    # enableSession = False

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

    # db.start_session()

    password_hash = bcrypt.hashpw(
        str(password).encode('utf-8'), bcrypt.gensalt())
    print(email)
    print(password_hash)

    try:
        mycol.insert_one({"email": str(email), "password": str(password_hash)})
        session.pop("email", None)
        session['email'] = str(email)
        # return redirect(url_for(''))
    except:
        print("Error in inserting")

    print(session)

    if 'username' in session:
        return 'You are logged in ' + session['username']

    return render_template('server/pages/signup.html')


if __name__ == "__main__":

    app.run(debug=True)
