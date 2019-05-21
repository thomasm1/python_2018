from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app1 = Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/pi/Public/login/login.db'
app1.config['SECRET_KEY'] = 'Thisissecret!' 

db = SQLAlchemy(app1)
login_manager = LoginManager()
login_manager.init_app(app1)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app1.route('/')
def index():
    user = User.query.filter_by(username='Thomas').first()
    login_user(user)
    return 'You are now logged in'

@app1.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out'

@app1.route('/home')
@login_required
def home():
    return 'the current user is ' + current_user.username

if __name__ == '__main__ ':
    app1.run(debug=True)
    
