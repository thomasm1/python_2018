from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
        return render_template("index.jinja2")
        # return "hellow 2"

@app.route('/home')
def home():
        return render_template("home.jinja2")
                #"Home"
                
@app.route('/home/messages')
def messages():
        return render_template("messages.jinja2")

@app.route('/home/<input>')
def input(input):
        return "Input: {}".format(input)

@app.route('/home/<input>/<message>')
def home_input_message(input, message):
        return render_template("home_input_message.jinja2",
                               input=input,
                               message=message)
        # return "{0}, {1}".format(name, message)

# URL: http://localhost:5000/query?a=test&b=123
@app.route('/query') 
def query():
        a = request.args.get('a')
        b = request.args.get('b')
        return "<h4>Variable a = {0}<br />while Variable b = {1}</h4>".format(a,b)
 