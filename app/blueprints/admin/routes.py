from flask import render_template, abort
from flask_login import login_required, current_user
from . import admin
from functools import wraps

# 自定义管理员权限装饰器
def admin_required(f):
    """仅允许管理员访问"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:  # 假设 User 模型有 is_admin 字段
            abort(403)  # Forbidden
        return f(*args, **kwargs)
    return decorated_function

# 管理后台首页
@admin.route('/dashboard')
@login_required
@admin_required  # 仅允许管理员访问
def dashboard():
    """管理员首页，显示系统的基本信息"""
    return render_template('dashboard.html')

# 用户管理页面
@admin.route('/users')
@login_required
@admin_required  # 仅允许管理员访问
def manage_users():
    """管理员管理用户"""
    return render_template('manage_users.html')

# 系统设置页面
@admin.route('/settings')
@login_required
@admin_required  # 仅允许管理员访问
def settings():
    """管理系统设置"""
    return render_template('settings.html')
