from flask import Blueprint, render_template, session

bp_index = Blueprint("bp_index", __name__)


@bp_index.route('/')
def index():
    if 'email' in session:
        return "Logged In"
    else:
        return render_template('server/pages/index.html')
