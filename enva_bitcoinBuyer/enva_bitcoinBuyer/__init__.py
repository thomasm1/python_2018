from flask import Flask, request, render_template

app = Flask(__name__)
members = []


@app.route('/')
def index():
        return render_template("index.jinja2")
        # return "Console"

@app.route('/home')
def home():
        return render_template("home.jinja2")
                #"ArmChair Bitcoinist"
           
@app.route('/home/console')
def console():
        return render_template("console.jinja2")
               
@app.route('/home/messages')
def messages():
        return render_template("messages.jinja2")

@app.route('/home/<input>')
def input(input):
        return "Input: {} <br /><br /><a href='/home'>back</a>".format(input)

@app.route('/home/<input>/<message>')
def home_input_message(input, message):
        return render_template("home_input_message.jinja2",
                               input=input,
                               message=message)
        # return "{0}, {1}".format(name, message)

@app.route('/register')
def register(): 
        return render_template("register.jinja2")

@app.route('/registrants')
def registrants(): 
        return render_template("registered.html", members=members)

@app.route('/registerPost') #, methods=["POST"])
def registerPost():
        members = []
        name = request.args.get("name")
        gender = request.args.get("gender") 
        if not name or not gender:
                return render_template("failure.jinja2")
        members.append(f"{name} with gender {gender}")
        return redirect("/registrants") 

# URL: http://localhost:5000/query?a=test&b=123
@app.route('/query') 
def query():
        a = request.args.get('a')
        b = request.args.get('b')         
        return "<h4>Variable a = {0}<br />while Variable b = {1}</h4><a href='/home'>back</a>".format(a,b)
 