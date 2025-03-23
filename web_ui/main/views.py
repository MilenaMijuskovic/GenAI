from web_ui.main import bp 
from flask import render_template

from data_processor import temperature, humidity, pressure, gas, chanceofwildfire # Import variables

@bp.route("/")
def index():
    return render_template(
        'main/homepage.html',
        title='Wildfire Escaper',
        temperature=temperature,
        humidity=humidity,
        pressure=pressure,
        gas=gas,
        chanceofwildfire=chanceofwildfire
    )
@bp.route("/all_good")
def all_good():
    return render_template('main/all_good.html', title='Home')
@bp.route("/danger")
def danger():
    return render_template('main/danger.html', title='Home')