from flask import render_template
from . import admin

@admin.route('/dashboard')
def dashboard():
    return render_template('admin_dashboard.html')

@admin.route('/settings')
def settings():
    return "管理后台设置页面"
