import sqlite3
import logging
from flask_login import UserMixin

DATABASE = 'users.db'

# 配置日志记录
logger = logging.getLogger(__name__)

class User(UserMixin):
    def __init__(self, id, username, password, is_admin):
        self.id = id
        self.username = username
        self.password = password
        self.is_admin = is_admin

    @staticmethod
    def get_user_by_username_and_password(username, password):
        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, username, password, is_admin FROM users WHERE username = ?", (username,))
                result = cursor.fetchone()
                if result and password == result[2]:  # 明文密码比较
                    return User(id=result[0], username=result[1], password=result[2], is_admin=result[3])
        except sqlite3.Error as e:
            logger.error(f"数据库查询失败: {e}")
        return None

    @staticmethod
    def get_user_by_id(user_id):
        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, username, password, is_admin FROM users WHERE id = ?", (user_id,))
                result = cursor.fetchone()
                if result:
                    return User(id=result[0], username=result[1], password=result[2], is_admin=result[3])
        except sqlite3.Error as e:
            logger.error(f"数据库查询失败: {e}")
        return None

