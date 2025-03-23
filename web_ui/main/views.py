from web_ui.main import bp 
from flask import render_template

@bp.route("/")
def index():
    return render_template('main/index.html', title='Wildfire')
@bp.route("/all_good")
def all_good():
    return render_template('main/all_good.html', title='Home')
@bp.route("/danger")
def danger():
    return render_template('main/danger.html', title='Home')