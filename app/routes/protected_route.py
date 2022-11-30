from flask import Blueprint, render_template, session
bp_protected = Blueprint("protected", __name__)


@bp_protected.route('/dashboard')
def dashboard():
    return render_template('server/pages/login.html')
