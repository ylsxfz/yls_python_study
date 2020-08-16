# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/16 09:33 
#  @Author: yls 
#  @Version: V 0.1
#  @File: views.py
#  @Desc:
"""
from . import calc
from flask import render_template, request
import re


@calc.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@calc.route('/api/getresult',methods=['POST'])
def get_calc_result():
    data = request.get_json()
    expr_val = data['expr']
    return str(eval(expr_val))
