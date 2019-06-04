from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
        return render_template("index.jinja2")
        # return "hellow 2"

@app.route('/hi')
def page1():
        return "Page 2"

@app.route('/hi/<name>')
def hi_name(name):
        return "Hello {}".format(name)

@app.route('/hi/<name>/<message>')
def hi_name_message(name, message):
        return render_template("hi_name_message.jinja2",
                               name=name,
                               message=message)
        # return "{0}, {1}".format(name, message)

@app.route('/query') # /query?a=test&b=123
def query():
        a = request.args.get('a')
        b = request.args.get('b')
        return "a={0} b={1}".format(a,b)

