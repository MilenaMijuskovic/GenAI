from flask import Flask, render_template
from flask_cors import CORS
import sys 
from web_ui.utils.logger import applogger 
from web_ui.config import AppConfig

def create_app(config_class=AppConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    app.logger = applogger 
    with app.app_context():
        from web_ui.main import bp as main_bp
        app.register_blueprint(main_bp, url_prefix=app.config['URL_PREFIX'])
    return app
