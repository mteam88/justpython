from flask import Flask
import flask


app = Flask(__name__,
            static_url_path='', 
            static_folder='static/',
            template_folder='templates/')

@app.route('/')
def homehandler():
    return flask.render_template('views/home.html', stockwidgets=['AAPL', 'TSLA', 'SPY'])

if __name__ == '__main__':
    app.debug = True
    app.run()