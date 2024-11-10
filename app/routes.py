from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from . import app
from .db_utils import User


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            error = '用户名和密码不能为空！'
        else:
            user = User.get_user_by_username_and_password(username, password)
            if user:
                login_user(user)
                return redirect(url_for('home'))
            else:
                error = '用户名或密码错误，请检查输入。'
    return render_template('a.html', error=error)


@app.route('/home')
@login_required
def home():
    return render_template('b.html', username=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
