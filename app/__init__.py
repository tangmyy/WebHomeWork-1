import secrets

from flask import Flask, redirect
from .extensions import bcrypt, login_manager
# app\__init__.py

from .blueprints import register_blueprints
from .db_utils import User

# Flask 应用工厂函数，用于创建和配置 Flask 应用实例

def create_app():
    app = Flask(__name__)

    # 自动生成随机密钥
    app.secret_key = secrets.token_hex(32)

    # 初始化扩展
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # 注册蓝图
    register_blueprints(app)

    # 添加根路径重定向
    @app.route('/')
    def index():
        return redirect('/auth')

    return app

@login_manager.user_loader
def load_user(user_id):
    """Flask-Login 加载用户回调"""
    return User.get_user_by_id(user_id)

