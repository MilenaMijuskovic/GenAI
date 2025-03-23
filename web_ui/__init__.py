from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    @app.route("/all_good")
    def hello_world():
        return render_template('all_good.html', title='Home')
    
    @app.route("/all_bad")
    def all_bad():
            return render_template('danger.html', title='Home')
    
    
    return app
