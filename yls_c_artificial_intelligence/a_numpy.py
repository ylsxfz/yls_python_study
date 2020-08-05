# _*_ coding: utf-8 _*_
"""
#  @Time : 2020/7/24 10:50
#  @Author : yls
#  @Version：V 0.1
#  @File : a_numpy.py
#  @desc : NumPy 是基于 Python 的开源数值计算扩展库，用来存储和处理大型矩阵。
        相比于 Python 自身的嵌套列表（nested list structure）结构要高效得多。
        NumPy 数组结构也能用来表示矩阵（matrix），详情参考：
            https://numpy.org/
        主要功能包括：
            1、N 维数组对象 Array
            2、成熟的广播机制
            3、能够解决线性代数、随机数生成数相关问题
"""

import numpy as np
import numpy.linalg as lg


def numpy_fun():
    # 矩阵
    x = np.array([[2, 1], [1, 2]])
    print("x原始矩阵：")
    print(x)
    print("*******************************")

    # x的转置矩阵
    xt = x.transpose()
    print("x的转置矩阵：")
    print(xt)
    print("*******************************")

    # 矩阵赋值
    xt[0, 0] = 1.0
    print("xt赋值后转置矩阵：")
    print(xt)
    print("*******************************")

    # dot操作求两个矩阵的乘积
    x2 = xt.dot(x)
    print("矩阵x: \n%s \n" % str(x))
    print("矩阵xt: \n%s \n" % str(xt))
    print("x * xt: \n%s \n" % str(x2))
    print("*******************************")

    x3 = lg.inv(x2)
    print("x2的逆矩阵：")
    print(x3)
    print("*******************************")


if __name__ == '__main__':
    numpy_fun()
    pass
