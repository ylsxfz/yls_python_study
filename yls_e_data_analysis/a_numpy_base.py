# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/16 10:12 
#  @Author: yls 
#  @Version: V 0.1
#  @File: a_numpy_base.py
#  @Desc: NumPy 通过这五大功能顺利入门 + 10 道练习题:
        1、numpy：NumPy 就非常适合做大规模的数值计算和数据分析。
            a、Python 的 list 是一个通用结构。它能包括任意类型的对象，并且是动态类型。
            b、NumPy 的 ndarray 是静态、同质的类型，当 ndarray 对象被创建时，元素的类型就确定。
                由于是静态类型，所以 ndarray 间的加、减、乘、除用 C 和 Fortran 实现才成为可能，
                所以运行起来就会更快。根据官当介绍，底层代码用 C 语言和 Fortran 语言实现，
                实现性能无限接近 C 的处理效率。
"""
import time
from numpy import e
import seaborn as sns

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


def numpy_create():
    """
    创建 NumPy 数组
    """
    # 1、通过构造函数array创建一维array
    v = np.array([1, 2, 3, 4])
    print(v)

    # 2、创建二维array
    v = np.array([[1, 2], [1, 2], [3, 4]])
    print(v)

    # 3、arange数组
    ara = np.arange(1, 10)
    print(ara)

    # 4、linspace数组，15个元素
    lins = np.linspace(1, 10, 15)
    print(lins)

    # 5、组合ndarray对象
    a = np.arange(10).reshape(2, -1)
    print(a)
    print(np.where(a > 3))
    print(np.array(np.where(a > 3)))
    tuple_to_arrau = np.array(np.where(a > 3))
    result = np.transpose(tuple_to_arrau)
    print(result)


def numpy_arr_attr():
    """
    NumPy 数组属性
    """
    # 一维数组
    v = np.zeros(10)
    print("一维数组：")
    print(v)
    print(v.shape)
    # 二维数组
    m = np.zeros((3, 4))
    print("二维数组：")
    print(m)
    print("shapes =》 属性返回数组的形状信息，是一个元组对象：%s" % str(m.shape))
    print("size =》属性获取元素个数：%d" % m.size)
    print("dtype =》获取数组内元素的类型：%s" % m.dtype)

    # dtype 更多取值：int、complex、bool、object，
    # 还可以显示的定义数据位数的类型，
    # 如：int64、int16、float128、complex128。
    m = np.array([1, 2, 3], dtype='float')
    print("创建数组时，通过dtype赋值，指定元素类型：%s " % str(m))


def numpy_array_fun():
    # 1、arrange函数：起始点、终点、步长。特别注意，不包括终点，[start,end)
    v = np.arange(0, 10, 2)
    print("arrange函数")
    print(v)
    print()

    # 2、linspace函数：起始点、终点、分割份数。特别注意：包括终点，[start,end]
    ar = np.linspace(0, 10, 5)
    print("linspace函数：")
    print(ar)
    print()

    # 3、logspace函数：创建以e为底，指数为1,2...,长度为10的数组：(start,stop,num,base=)
    print("logspace函数：")
    logs = np.logspace(1, 10, 10, base=e)
    print(logs)
    print()

    # 4、diag函数：创建对角数组
    dig = np.diag([1, 2, 3])
    print('diag函数：')
    print(dig)
    print()

    #     v : array_like
    #         If `v` is a 2-D array, return a copy of its `k`-th diagonal.
    #         If `v` is a 1-D array, return a 2-D array with `v` on the `k`-th
    #         diagonal.
    #     k : int, optional 偏移量
    #         Diagonal in question. The default is 0. Use `k>0` for diagonals
    #         above the main diagonal, and `k<0` for diagonals below the main
    #         diagonal.
    dig = np.diag([1, 2, 3], k=1)
    print("diag函数，偏移量为1：")
    print(dig)
    print()

    # 5、zeros函数：创建元素全部为0的数组
    ze = np.zeros((3, 3))
    print("zeros函数：")
    print(ze)
    print()

    # 6、ones函数：创建元素全部为1的数组
    print("ones函数：")
    one = np.ones((3, 3))
    print(one)
    print()

    # 7、np.random：生成随机数组
    rad = np.random.rand(3, 5)
    print("随机数组：")
    print(rad)
    print()


def numpy_index_filter():
    """
    索引和筛选
    """
    m = np.arange(18).reshape(2, 3, 3)
    print(m)
    print()

    # : 表示此维度的所有元素全部获取
    print(": 表示此维度的所有元素全部获取：")
    print(m[:, 1:3, :])
    print()

    m[:, 0, :] = -1
    print(" m[:, 0, :] = -1 赋值后")
    print(m)
    print()

    print("m[:, :, 0]：")
    mt = m[:, :, 0]
    print(mt)
    print("判断上面切片 m[:,:,0] 中大于 5 的元素，"
          "写法简洁，无需写 for 循环：")
    print(mt[mt > 5])


def numpy_practice():
    # 1、创建一个[3,5]所有元素为True的数组
    m = np.ones((3, 5), dtype=bool)
    print("1、创建一个[3,5]所有元素为True的数组：")
    print(m)
    print()

    # 2、一维数组转二维
    m = np.linspace(1, 5, 10).reshape(5, 2)
    print("2、一维数组转二维：")
    print(m)
    print()

    # 3、数组所有奇数替换为-1
    m = np.arange(10).reshape(2, 5)
    m[m % 2 == 1] = -1
    print("3、数组所有奇数替换为-1：")
    print(m)
    print()

    # 4、提取出数组中所有奇数
    m = np.arange(10).reshape(5, 2)
    print(" 4、提取出数组中所有奇数：")
    print(m[m % 2 == 1])
    print()

    # 5、求2个NumPy 数组的交集
    m, n = np.arange(10), np.arange(1, 15, 3)
    print(" 5、求2个NumPy 数组的交集：")
    print(np.intersect1d(m, n))
    print()

    # 6、求2个NumPy 数组的差集
    m, n = np.arange(10), np.arange(1, 15, 3)
    print("6、求2个NumPy 数组的差集：")
    print(np.setdiff1d(m, n))
    print()

    # 7、筛选出指定区间内2<m<7的所有元素
    # 注意：(m >2)，必须要添加一对括号
    m = np.arange(10).reshape(2, 5)
    print("7、筛选出指定区间内2<m<7的所有元素：")
    print(m[(m > 2) & (m < 7)])
    print()

    # 8、二维数组交换 2 列
    m = np.arange(10).reshape(2, 5)
    print("8、二维数组交换 2 列：")
    print(m)
    print("二维数组交换 2 列后:")
    print(m[:, [1, 0, 2, 3, 4]])
    print("二维数组交换 多 列后:")
    print(m[:, [1, 0, 2, 4, 3]])
    print()

    # 9、二维数组，反转行
    m = np.arange(10).reshape(2, 5)
    print("9、二维数组，反转行：")
    print(m)
    print("二维数组，反转行后：")
    print(m[::-1])
    print()

    # 10、生成数值 5~10、shape 为 (3,5) 的随机浮点数
    np.random.seed(100)
    m = np.random.randint(5, 10, (3, 5)) + np.random.rand(3, 5)
    print("10、生成数值 5~10、shape 为 (3,5) 的随机浮点数：")
    print(m)
    print()


def numpy_example_one():
    # 1、下载数据
    # url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    # wid = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[1])
    wid = np.genfromtxt("archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", delimiter=',',
                        dtype='float', usecols=[1])
    print(wid)

    # 2、归一化：s = ( wid - smin ) / ( smax - smin )
    # 还有一个更简便的方法，使用 ptp 方法，
    # 它直接求出最大值与最小值的差：s = (wid - smin) / wid.ptp()
    smax = np.max(wid)
    smin = np.min(wid)
    print("最大值、最小值：")
    print(smax, smin)

    s = (wid - smin) / (smax - smin)
    # 3、NumPy的打印设置：
    # 只打印小数点后三位的设置方法：
    np.set_printoptions(precision=3)
    print("归一化结果：只打印小数点后三位")
    print(s)

    sns.distplot(s, kde=False, rug=True)

    sns.distplot(s, hist=True, kde=True, rug=True)


if __name__ == '__main__':
    # a_test_numpy()
    # 创建 NumPy 数组
    # numpy_create()

    #  NumPy 数组属性
    # numpy_arr_attr()

    # 数组函数
    # numpy_array_fun()

    # 索引和筛选
    # numpy_index_filter()

    # 案例一：数据归一化
    numpy_example_one()

    # 10道NumPy基础题
    # numpy_practice()
    pass
