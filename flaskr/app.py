from flask import Flask

app = Flask("main")
import db

@app.route('/')
def index():
  return "Hello world!" #if you want to render a .html file, 
                        # import render_template from flask and use 
                        #render_template("index.html") here.

if __name__ == '__main__':
    app.debug = True
    app.run()