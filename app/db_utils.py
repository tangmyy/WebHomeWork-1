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
        """通过用户名和密码验证用户"""
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

    @staticmethod
    def get_all_non_admin_users():
        """获取所有非管理员用户"""
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username FROM users WHERE is_admin = 0")
            results = cursor.fetchall()
            users = [{'id': row[0], 'username': row[1]} for row in results]
            return users

    @staticmethod
    def update_user(user_id, new_username):
        """更新用户信息"""
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET username = ? WHERE id = ?", (new_username, user_id))
            conn.commit()

    @staticmethod
    def delete_user(user_id):
        """删除用户"""
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()

    @staticmethod
    def create_user(username, password):
        """新增普通用户"""
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
                (username, password, 0)  # 新增用户默认不是管理员
            )
            conn.commit()


