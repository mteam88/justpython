from flask import Flask

app = Flask("main")

@app.route('/')


if __name__ == '__main__':
    app.debug = True
    app.run()