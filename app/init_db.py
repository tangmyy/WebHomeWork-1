import sqlite3

DATABASE = 'users.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')
        # 插入一个示例用户记录，密码可以使用明文或加密存储（这里简化为明文）
        cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('lwj', '22206776')")
        cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('zhangxing', '22206777')")
        cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('cjcj', '22206778')")
        conn.commit()


init_db()
