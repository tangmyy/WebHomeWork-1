from flask import render_template, request, redirect, url_for, session
from . import app
import sqlite3
from .db_utils import get_user_by_username_and_password

DATABASE = 'users.db'


@app.errorhandler(500)
def internal_server_error(error):
    return "服务器出现错误，请稍后再试。", 500


@app.errorhandler(404)
def page_not_found(error):
    return "页面未找到，请检查 URL。", 404



@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # 获取密码
        if not username or not password:
            error = '用户名和密码不能为空！'
        else:
            # 使用新的函数验证用户名和密码
            user = get_user_by_username_and_password(username, password)
            if user:
                session['username'] = username
                return redirect(url_for('home'))
            else:
                error = '用户名或密码错误，请检查输入。'
    return render_template('a.html', error=error)



# 页面b: 用户主页
@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    return render_template('b.html', username=username)



