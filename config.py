import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'smsMail-secret-form-key'

SQLALCHEMY_DATABASE_URI = "sqlite:///smsmail.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
