import sqlite3
import logging
from flask_login import UserMixin

DATABASE = 'users.db'

# 配置日志记录
logger = logging.getLogger(__name__)

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def get_user_by_username_and_password(username, password):
        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, username FROM users WHERE username = ? AND password = ?",
                               (username, password))
                result = cursor.fetchone()
                if result:
                    return User(id=result[0], username=result[1])
        except sqlite3.Error as e:
            logger.error(f"数据库查询失败: {e}")
        return None

    @staticmethod
    def get_user_by_id(user_id):
        """根据用户ID获取用户信息"""
        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, username FROM users WHERE id = ?", (user_id,))
                result = cursor.fetchone()
                if result:
                    return User(id=result[0], username=result[1])
        except sqlite3.Error as e:
            logger.error(f"数据库查询失败: {e}")
        return None
