# coding=utf-8


# 导入Flask
from flask import Flask
from src.web.flask_demo.controller.recommend_controller import recommend
from common.error_handler import exception

# 实例化Flask
app = Flask(__name__)

# 注册统一的异常处理器
app.register_blueprint(exception, url_prefix='/error')
# app给蓝图注册路由
app.register_blueprint(recommend, url_prefix="/recommend")

# 让Flask跑起来
app.run(host='localhost', port=8080)
