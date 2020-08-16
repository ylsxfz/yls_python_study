# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/16 10:12 
#  @Author: yls 
#  @Version: V 0.1
#  @File: a_numpy.py
#  @Desc: NumPy 通过这五大功能顺利入门 + 10 道练习题:
        1、numpy：NumPy 就非常适合做大规模的数值计算和数据分析。
            a、Python 的 list 是一个通用结构。它能包括任意类型的对象，并且是动态类型。
            b、NumPy 的 ndarray 是静态、同质的类型，当 ndarray 对象被创建时，元素的类型就确定。
                由于是静态类型，所以 ndarray 间的加、减、乘、除用 C 和 Fortran 实现才成为可能，
                所以运行起来就会更快。根据官当介绍，底层代码用 C 语言和 Fortran 语言实现，
                实现性能无限接近 C 的处理效率。
"""
import time
import numpy as np


def a_test_numpy():
    """
    完成同样的都对元素乘以 2 的操作，NumPy 比 Python 快了 45 倍之多。
    """
    a = list(range(1000000))
    begin_time = time.time()
    a2 = [i * 2 for i in a]
    end_time = time.time()
    run_time = end_time - begin_time
    print('运行时间：%f ms' % (run_time * 1000))

    na = np.array(range(1000000))
    begin_time = time.time()
    na2 = na * 2
    end_time = time.time()
    run_time = end_time - begin_time
    print('numpy运行时间：%f ms' % (run_time * 1000))


def numpy_use():
    # 1、通过构造函数array创建一维array
    v = np.array([1, 2, 3, 4])
    print(v)




    # 2、创建二维array
    v = np.array([[1, 2], [1, 2], [3, 4]])
    print(v)


if __name__ == '__main__':
    # a_test_numpy()
    numpy_use()
    pass
