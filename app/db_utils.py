import sqlite3
import logging
from flask_login import UserMixin
from . import bcrypt  # 导入 bcrypt 实例

DATABASE = 'users.db'

# 配置日志记录
logger = logging.getLogger(__name__)

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @staticmethod
    def create_user(username, password):
        """用于创建新用户并保存哈希密码到数据库"""
        try:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')  # 生成哈希密码
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
                conn.commit()
                return True
        except sqlite3.Error as e:
            logger.error(f"用户创建失败: {e}")
            return False

    @staticmethod
    def get_user_by_username_and_password(username, password):
        """通过用户名和密码验证用户"""
        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, username, password FROM users WHERE username = ?", (username,))
                result = cursor.fetchone()
                if result and bcrypt.check_password_hash(result[2], password):  # 验证密码
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
