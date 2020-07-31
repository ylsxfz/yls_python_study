# _*_ coding: utf-8 _*_
"""
#  @Time : 2020/7/24 10:03
#  @Author : yls
#  @Version：V 0.1
#  @File : a_app.py
#  @desc : Flask 是一个轻量级的 WSGI Web 应用框架，
        适合搭建轻量级的 Web 应用程序
"""

from flask import Flask

App = Flask(__name__)


@App.route('/')
def index():
    """
    写一个 index 页的入口函数，返回 hello world。
    通过装饰器 App.route('/') 创建 index 页的路由，
    一个 / 表示 index 页：
    Returns:
        返回 hello world
    """
    return "hello world"


if __name__ == '__main__':
    App.run(debug=True)
    pass
