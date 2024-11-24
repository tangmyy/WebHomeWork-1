from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.db_utils import User
from . import auth  # 导入蓝图实例


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        if not username or not password:
            flash('用户名和密码不能为空！', 'error')
        else:
            user = User.get_user_by_username_and_password(username, password)
            if user:
                login_user(user)
                return redirect(url_for('auth.home'))
            else:
                flash('用户名或密码错误，请检查输入。', 'error')
    return render_template('a.html')

@auth.route('/home')
@login_required
def home():
    """用户主页"""
    return render_template('b.html', username=current_user.username)

@auth.route('/logout')
@login_required
def logout():
    """注销用户"""
    logout_user()
    return redirect(url_for('auth.login'))

