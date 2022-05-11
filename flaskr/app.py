from flask import Flask
import flask


app = Flask(__name__, template_folder='flaskr/templates')

@app.route('/')
def home():
    return flask.render_template('views/home.html')

if __name__ == '__main__':
    app.debug = True
    app.run()