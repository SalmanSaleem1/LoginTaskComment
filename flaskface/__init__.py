from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flaskface.config import BaseConfig
from flask_mail import Mail

app = Flask(__name__, template_folder='template')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'

from flaskface.user.Routes import user
from flaskface.post.Routes import post
from flaskface.main.Routes import main
from flaskface.error.CustomeError import errors
from flaskface.comments.route import comment

app.register_blueprint(user)
app.register_blueprint(post)
app.register_blueprint(main)
app.register_blueprint(errors)
app.register_blueprint(comment)
