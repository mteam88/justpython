from flask import Flask, request
import flask, flask_login
from flaskr.logic import stockwidgets
from .blueprints.account import account_bp


app = Flask(__name__,
            static_url_path='', 
            static_folder='static/',
            template_folder='templates/')
app.register_blueprint(account_bp)

@app.route('/')
def homehandler():
    return flask.render_template('views/home.html', stockwidgets=stockwidgets)

if __name__ == '__main__':
    app.debug = True
    app.run()