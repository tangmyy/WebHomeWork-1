from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

from . import routes  # 导入 auth 蓝图的路由
