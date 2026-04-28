import os
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.config.from_object(Config)
app.config['SESSION_FILE_DIR'] = '/tmp/flask_session'
app.config['SESSION_TYPE'] = 'filesystem'
os.makedirs('/tmp/flask_session', exist_ok=True)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

Session(app)
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
login = LoginManager(app)
login.login_view = 'login'
import FlaskWebProject.views
