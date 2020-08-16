# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/16 09:32 
#  @Author: yls 
#  @Version: V 0.1
#  @File: __init__.py.py
#  @Desc:
"""
from flask import Blueprint


# 创建一个Blueprint类对象
print('__name__')
calc = Blueprint('calc',__name__)

from . import views