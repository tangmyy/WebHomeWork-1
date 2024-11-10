import sqlite3
from . import app

DATABASE = 'users.db'

def get_user_by_username_and_password(username, password):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            return cursor.fetchone()
    except sqlite3.Error as e:
        app.logger.error(f"数据库查询失败: {e}")
        return None
