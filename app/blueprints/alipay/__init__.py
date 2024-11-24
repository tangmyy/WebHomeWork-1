# alipay\__init__.py

from flask import Blueprint

# 创建 Blueprint 对象
alipay_bp = Blueprint('alipay', __name__)

from . import routes  # 导入 alipay 蓝图的路由
