from flask.blueprints import Blueprint
from flask import render_template, request

home_bp = Blueprint('home',__name__)


@home_bp.route('/', defaults={'send_path': ''})
@home_bp.route('/<path:send_path>')
def home(send_path):
    return render_template('index.html')
