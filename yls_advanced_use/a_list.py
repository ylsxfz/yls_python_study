# -*- coding: UTF-8 -*-
"""
 @Time: 2020/07/26 09:32 
 @Author: yls 
 @Version: V 0.1
 @File: a_list.py
 @Desc: 列表使用：
            使用 [] 创建一个列表。
            容器类型的数据进行运算和操作，生成新的列表最高效的办法——列表生成式。

"""
from random import random, uniform
import os
from math import floor


def list_data_operatioin():
    """
    数据再运算：实现对每个元素的乘方操作，利用列表生成式返回一个新的列表。
    """
    a = range(0, 11)
    b = [x ** 2 for x in a]
    print(b)

    a = range(0, 10)
    b = [str(i) for i in a]
    print(b)


def list_to_random():
    """
    一串随机数
    """
    a = [round(random(), 2) for _ in range(10)]
    print(a)

    a = [round(uniform(0, 10), 2) for _ in range(10)]
    a.sort()
    print(a)


def list_if_for():
    """
    对一个列表里面的数据筛选，只计算[0.11)中偶数的平方
    """
    a = range(11)
    c = [x ** 2 for x in a if x % 2 == 0]
    print(c)


def list_zip():
    """
    实现 iter1 和 iter2 的对应索引处的元素拼接。
    """
    a = range(5)
    b = ['a', 'b', 'c', 'd', 'e']
    c = [str(y) + str(x) for x, y in zip(a, b)]
    print(c)


def list_key_value():
    """
    打印键值对
    """
    a = {'a': 1, 'b': 2, 'c': 3}
    # 改行会报错，v必须用str转换为字符串，才能混合字符串输出
    # b = [k + '=' + v for k, v in a.items()]
    b = [k + '=' + str(v) for k, v in a.items()]
    print(b)


def list_files():
    """
    isdir/isfile: 接受的参数需要是绝对路径，否则判断不出来
    """
    filePath = "..\\yls_a_base\\file"
    dirs = [d for d in os.listdir(filePath) if os.path.isdir(os.path.join(filePath, d))]
    print(dirs)

    files = [f for f in os.listdir(filePath) if os.path.isfile(os.path.join(filePath, f))]
    print(files)


def list_to_lower():
    """
    python的列类型可以不同
    会出现 int 对象没有方法 lower 的问题，先转化元素为 str 后再操作
    更友好的做法，使用 isinstance，判断元素是否为 str 类型，如果是，再调用 lower 做转化：
    """
    a = ['Hello', 'World', 2342, '2019Python']
    b = [str(w).lower() for w in a]
    print(b)

    b = [s.lower() for s in a if isinstance(s, str)]
    print(b)


def list_filter_non_unique(lst):
    """
    保留唯一值
    Args:
        lst: 列表

    Returns:
        返回列表中不重复，唯一的值
    """
    return [item for item in lst if lst.count(item) == 1]


def list_bifurcate(lst, filter):
    """
    筛选分组：
        enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
                 同时列出数据和数据下标，一般用在 for 循环当中。
    Args:
        lst: 列表
        filter: 筛选规则

    Returns:
        返回筛选的分组结果
    """
    return [
        [x for i, x in enumerate(lst) if filter[i] == True],
        [x for i, x in enumerate(lst) if filter[i] == False]
    ]


def list_bifurcate_by_fun(lst, fn):
    """
    函数分组
    Args:
        lst: 列表
        fn: 函数规则

    Returns:
        返回函数分组的结果
    """
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]


def list_difference(a, b):
    """
    两个列表的差集
    Args:
        a: 列表a
        b: 列表b

    Returns:
        返回列表1和列表b的差集
    """
    _a, _b = set(a), set(b)
    return [item for item in _a if item not in _b]


def list_difference_by_fn(a, b, fn):
    _b = set(map(fn, b))
    print(_b)
    return [item for item in a if fn(item) not in _b]


if __name__ == '__main__':
    # 数据再运算
    # list_data_operatioin()

    # 一串随机数
    # list_to_random()

    # if和for嵌套
    # list_if_for()

    # list和zip
    # list_zip()

    # 打印键值对
    # list_key_value()

    # 打印文件列表
    # list_files()

    # 转为小写
    # list_to_lower()

    # 保留唯一值
    # lst = list_filter_non_unique([1,1,1,232,42,1,421,5,1,125,13])
    # print(lst)

    # 筛选分组
    # lst = list_bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
    # print(lst)

    # 筛选出首字母为‘u’的字符串
    # lst = list_bifurcate_by_fun(['Python3', 'up', 'users', 'people'],lambda x : x[0] == 'u')
    # print(lst)

    # 求两个列表的差集
    # lst = list_difference([1,231,24,12,4,12,412,1],[124,12,12,41,4,1,231])
    # print(lst)

    # 函数差集：列表元素为单个元素
    # lst = list_difference_by_fn([2.1, 1.2], [2.3, 3.4], floor)
    # print(lst)

    # 函数差集：列表元素为字典
    lst = list_difference_by_fn([{'x': 2}, {'x': 1}], [{'x': 1}], lambda v: v['x'])
    print(lst)
    pass
