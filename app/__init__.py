import os
from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID

app = Flask(__name__)
app.config.from_object'config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


from app import views, models