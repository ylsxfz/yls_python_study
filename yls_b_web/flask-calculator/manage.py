# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/16 09:32 
#  @Author: yls 
#  @Version: V 0.1
#  @File: manage.py.py
#  @Desc: 模拟计算器
"""
from app import create_app

if __name__ == '__main__':
   app = create_app()
   app.run(host='127.0.0.1',debug=True,port=8080)
