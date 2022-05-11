from flask import Flask

app = Flask("main")

if __name__ == '__main__':
    app.debug = True
    app.run()