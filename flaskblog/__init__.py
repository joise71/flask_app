import os
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


dotenv_path = Path(Path.cwd(), '.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskblog.sqlite3'  # /// means that database "site.db" will be
# created in the same CWD as this project
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes
