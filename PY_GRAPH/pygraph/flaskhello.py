from flask import Flask 
app = Flask(__name__) 
 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:////tmp/test/db'
db = SQLAlchemy(app)


@app.route("/")
def flaskhello():
	return "Hello FLASKworld!"

#  $FLASK_APP=flaskhello.py flask run

''' 
class BlogPost(db.Model):
	title = db.Column(db.String(200))
	content = db.Column(db.Text)
	pub_date = db.Column(db.DateTime)
'''

''' 
bp = BlogPost()
bp.title = "djdata"
db.session.add(bp)
db.session.commit()
'''

from flask_login import UserMixin

class User(db.Model, UserMixin):
	id = db.Column(
		db.Integer, primary_key=True)
	username = db.Column(
		db.String(255), unique=True)
	password = db.Column(db.String(255))
	active = db.Column(db.Boolean)





from flask_login import current_user

@app.route('/')
def index():
	if current_user.is_anonymous:
		return render_templates("splash.html")
	else:
		return render_template("user_home.html")





from flask import Flask
app = Flask(__name__)

@app.route("/")
def flaskhello():
	return "Well Well, Flaskhello"







from flask import Blueprint
flaskhello_bp = Blueprint('flaskhello', __name__)

@flaskhello_bp.route("/")
def flaskhello():
	return "flaskhello Route"

from flask_marshmallow import flask_marshmallow
from flask_login import current_user, login_required
from yourapp.models import User

ma = Marshmallow(app)

class UserSchema(ma.ModelSchema):
	class Meta:
		model = User
		exclude = ['password']


@app.route("/me")
@login_required
def me():
	return UserSchema().jsonify(current_user)

# {"id":1, "username": "example", "active":true}