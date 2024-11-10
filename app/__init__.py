from flask import Flask
import os
import secrets
import logging
from .init_db import init_db

app = Flask(__name__)

DATABASE = 'users.db'


# 生成一个 32 字节的随机字符串
app.secret_key = secrets.token_hex(32)
app.logger.setLevel(logging.DEBUG)

# 调用数据库初始化
if not os.path.exists(DATABASE):
    init_db()

from . import routes  # 导入路由模块



