from flask import Flask
application = Flask(__name__)


@application.route("/")
def hello():
    return "<div style='background-color:lightblue;'><h1 style='text-align:center;color:green'>TMM September Flask</h1></div>"


@application.route("/health")
def health():
    return "<div style='background-color:lightsteelblue;'><h1 style='text-align:center;color:blue'>TMM September Flask</h1></div>"


if __name__ == "__main__":
    application.run(host='0.0.0.0')
