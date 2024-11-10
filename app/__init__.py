import secrets

from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from .db_utils import User

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

bcrypt = Bcrypt(app)  # 初始化 Bcrypt
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get_user_by_id(user_id)

from . import routes
