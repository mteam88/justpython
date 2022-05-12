from flask import Flask, request
import flask
from flaskr.logic import stockwidgets


app = Flask(__name__,
            static_url_path='', 
            static_folder='static/',
            template_folder='templates/')

@app.route('/')
def homehandler():
    app.logger.critical(request.__dict__)
    return flask.render_template('views/home.html', stockwidgets=stockwidgets)

if __name__ == '__main__':
    app.debug = True
    app.run()