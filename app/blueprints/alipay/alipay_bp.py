# alipay\alipay_bp.py

from flask import Blueprint


# 创建蓝图
alipay_bp = Blueprint('alipay', __name__)


# 定义路由
@alipay_bp.route('/pay', methods=['GET', 'POST'])
def pay():
    return "This is the payment page"

@alipay_bp.route('/payment_success', methods=['GET'])
def payment_success():
    # 处理支付成功后的逻辑
    pass

# 注册蓝图到 Flask app
# app.register_blueprint(alipay_bp, url_prefix='/alipay')
