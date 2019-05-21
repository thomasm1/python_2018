from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
#routing
@app.route('/hello/<string:name>') 
def hello(name):
    return 'hello ' + name +  '!' 
@app.route('/test')  #only allows GET
#configuration
app.config.from _envvar('ENV_VAR_NAME')
#templates
from flask import render_template

@app.route('/')
def index():
    return render_template('template_file.html')
#JSON responses
import jsonify
@app.route('/returnstuff')
def returnstuff():
    num_list = [1,2,3,4,5]
    num_dict = {'numbers' : {'numbers' : [1,2,3,4,5], 'name' : 'Numbers'}}
    return jsonify({'output' : num_dict})
#access request data
request.args['name'] #query stirng
#redirexct
from flask import url_for, redirect
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/redirct')
def redirect_example():
    return redirect(url_for('index')) 

