# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/16 09:31 
#  @Author: yls 
#  @Version: V 0.1
#  @File: __init__.py.py
#  @Desc:
"""
from flask import Flask
from flask_cors import CORS
from flask_bootstrap import Bootstrap

cors = CORS()  # 跨站请求伪造保护
bootstrap = Bootstrap()  # 引入著名的 CSS 前端框架

def create_app():
    app = Flask(__name__)

    bootstrap.init_app(app)
    cors.init_app(app,supports_credentials=True)

    from .calc import calc
    app.register_blueprint(calc)

    return app