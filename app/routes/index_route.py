from flask import Blueprint, render_template, session

bp_index = Blueprint("bp_index", __name__)


@bp_index.route('/')
def index():
    if 'username' in session:
        return 'You are logged in ' + session['username']

    return render_template('server/pages/index.html')
