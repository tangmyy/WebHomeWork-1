# alipay\routes.py

from flask import Blueprint

# my51eshop_alipayandupload
alipay_bp = Blueprint("alipay", __name__, template_folder="templates")


@alipay_bp.route("/paysuccess")
def paysuccess():
    return "pay success"

@alipay_bp.route("/payfailed")
def payfail():
    return "pay fail"




#
# # 下订单
# @user_bp.route("/placeorder/<int:subtotal>", methods=["POST", "GET"])
# @login_required
# def place_order(subtotal):
#     cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     order = Order(user_id=current_user.id, total_price=subtotal, time=cur_time)
#     db.session.add(order)
#     db.session.commit()
#
#     alipay = alipay_obj()
#     order = Order.query.order_by(Order.id.desc()).first()
#     order_string = alipay.api_alipay_trade_page_pay(
#         out_trade_no="202411285777" + str(order.id),
#         total_amount=subtotal,
#         subject="大钻戒",
#         # 支付成功回调
#         return_url=ALIPAY_SETTING.get('ALIPAY_RETURN_URL'),
#         # 支付失败回调
#         notify_url=ALIPAY_SETTING.get('ALIPAY_NOTIFY_URL'),
#     )
#     # 拼接完整支付链接
#     pay_url = ALIPAY_SETTING['APIPAY_GATEWAY'] + "?" + order_string
#
#     # 返回支付链接或重定向到支付页面
#     return redirect(pay_url)
#
#
# @user_bp.route("/alipay/success_result", methods=["GET"])
# def alipay_success_result():
#     alipay = alipay_obj()
#     data = request.args.to_dict()
#     signature = data.pop("sign", None)
#     success = alipay.verify(data, signature)
#
#     if success:
#         flash("Payment successful! Thank you for your order.", "success")
#         return redirect(url_for("user.home"))
#     else:
#         flash("Payment verification failed.", "danger")
#         return redirect(url_for("user.cart"))
#
#
# @user_bp.route("/alipay/notify_result", methods=["POST"])
# def alipay_notify_result():
#     alipay = alipay_obj()
#     data = request.form.to_dict()
#     signature = data.pop("sign", None)
#     success = alipay.verify(data, signature)
#
#     if success and data["trade_status"] in ["TRADE_SUCCESS", "TRADE_FINISHED"]:
#         # 记录回调信息
#         print("Payment Notification Received:", data)
#         return "success"
#     return "failure"
#
