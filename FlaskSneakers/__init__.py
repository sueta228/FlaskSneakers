from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xa4\x93\x96\x9e\xd5o\x1d\xe0C\xac<\x93S\x98\xe5\xfd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from FlaskSneakers import routes
