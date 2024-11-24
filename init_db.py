import os
import sqlite3

from app import bcrypt

# 定义数据库路径（确保指向 app/users.db）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'users.db')


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # 创建 users 表，列名为 is_admin
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            is_admin BOOLEAN NOT NULL DEFAULT 0
        )''')

        # 插入普通用户
        cursor.execute("INSERT OR IGNORE INTO users (username, password, is_admin) VALUES ('lwj', '2220676', 0)")
        cursor.execute("INSERT OR IGNORE INTO users (username, password, is_admin) VALUES ('zhangxing', '2220677', 0)")
        cursor.execute("INSERT OR IGNORE INTO users (username, password, is_admin) VALUES ('cjcj', '2220678', 0)")
        conn.commit()

        # 插入管理员用户
        cursor.execute("INSERT OR IGNORE INTO users (username, password, is_admin) VALUES ('admin', '123', 1)")
        conn.commit()
        print("数据库初始化完成")


# 初始化数据库
init_db()

def check_table_structure():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(users)")
        columns = cursor.fetchall()
        for column in columns:
            print(column)

check_table_structure()