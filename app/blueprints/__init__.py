# blueprints\__init__.py

from .auth import auth  # 导入 auth 蓝图实例
from .admin import admin  # 导入 admin 蓝图实例
from .alipay import alipay_bp  # 导入 myalipay 蓝图实例



# 集中管理蓝图的注册逻辑
def register_blueprints(app):
    """注册所有蓝图"""

    # 注册蓝图
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(alipay_bp, url_prefix="/alipay")
