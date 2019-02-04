#Front Page :: FLASK
#sandbox Scraper
'''pip install Flask
pip install Flask-PyMongo
pip install SQLAlchemy  # use flask-restful/flask-restful.git #cd fla* #python setup.py devpipelop
pip install Flask-Mail
pip install flask-restful # use flask-restful/flask-restful.git #cd fla* #python setup.py develop #
 
'''
from flask import Flask

app = Flask(__name__)
@app.route('/tom\Login')
def NewLogin():
	return 'new item'
if __name__ == '__main__':
	#app.run(debug=True)
	app.run(host='0.0.0.0', port=4000)
	# ROUTING 
@app.route('/tom/<string:name>')# example.com/hello/t
def NewLogin(name):
	return 'Welcome ' + name + '
#Allowed Request Methods
@app.route('/test')
@app.route('/test/, methods=['GET', 'POST])
@app.route('/test', methods=['PUT'])
#Configuration
app.config['CONFIG_NAME'] = 'config value'
app.config.from_envvar('ENV_VAR_NAME') # import from exported env var w pth to config
#Templates
from flask import render_template
@app.route('/')
def index():
	return render_template('template_file.html', var1=value1)
#JSON Resonponses
import jsonify
@app.route('/A')
def A():
	num_list = [1,2,3,4,5]
	num_dict = {'number' : num_list, 'name' : 'Numbers')}
	return jsonify({'output' : num_dict})
##set session
import session
app.config['SECRET_KEY'] = 'Any random string'
@app.route('/login_success')
def login_success():
	session['key_name'] = 'key_value'
	return redirect(url_for('index'))
#read session@app.route('/')
def index():
	if 'key_name' in session:  #session exist and has key
		session_var = session[key_value']
	else: #session does not exist...

def index():
	if 'key_name' in session: 
		session_var = session['key_value']
