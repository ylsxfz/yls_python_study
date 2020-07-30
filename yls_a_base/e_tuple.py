# -*- coding: UTF-8 -*-
# """
# # _*_ coding: utf-8 _*_
#  @Time: 2020/7/19  20:58
#  @Author: yls
#  @Version: V 0.1
#  @File: e_tuple.py
#  @Desc: 不可变容器
# """

from numpy import random


def basciTup():
    """
    tuple：元组的基本操作
    元组既然是不可变（immutable）对象，自然也就没有增加、删除元素的方法。
    特别注意：一个整数加一对括号，比如 (10)，返回的是整数。必须加一个逗号 (10, ) 才会返回元组对象
    """
    # 空元组
    a = ()
    b = (1, 'xiaoming', 29.5, '173214234252')
    c = ('001', '2019-11-11', ['三文鱼', '电烤箱'])

    print(b)
    print(b[::-1])
    print(c)
    print(c[::-1])

    # 从[1,5)的区间内随机选择10个数
    a = random.randint(1, 5, 10)
    print("a:" + str(a))
    at = tuple(a)
    print("at：" + str(at))
    val = at.count(3)
    print("at中3出现的次数：" + str(val))


if __name__ == '__main__':
    basciTup()
