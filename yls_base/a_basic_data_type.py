# -*- coding: UTF-8 -*-
"""
# _*_ coding: utf-8 _*_
 @Time: 2020/7/19 0019 15:03 
 @Author: yls 
 @Version: V 0.1
 @File: a_basic_data_type.py
 @Desc:
"""
from random import randint, sample


class Book(object):
    """
    类的练习
    """

    # 定义类的参数
    def __init__(self, book_id, book_name, book_store_count):
        self.book_id = book_id
        self.book_name = book_name
        self.book_store_count = book_store_count

    # 重写加法操作
    def __add__(self, book):
        return self.book_store_count + book.book_store_count


def score_mean(lst1):
    """
    去掉列表中的一个最大值和一个最小值，然后计算剩余元素的平均值
    Args:
        lst1: list列表对象

    Returns:
        val: 平均值

    """
    lst1.sort()
    lst2 = lst1[1:-1]
    val = round((sum(lst2) / len(lst2)), 1)
    return val


def multiplicationTable():
    """
    九九乘法表
    """
    for i1 in range(1, 10):
        for j in range(1, i1 + 1):
            print('%d*%d=%d' % (j, i1, j * i1), end='\t')
        print()


def sampleSampling():
    """
    样本抽样
    """
    lst3 = [randint(0, 50) for _ in range(100)]
    print(lst3[:5])
    lst_sample = sample(lst3, 10)
    print(lst_sample)


if __name__ == '__main__':
    # 新建两个Book类的实例
    python_intro_book = Book(1, "python入门书", 100)
    ml_intro_book = Book(2, "机器学习入门书", 200)
    # 两本书的总销量
    sales_cnt = python_intro_book + ml_intro_book
    print(sales_cnt)

    i = 3
    print(1 < i < 3)
    print(1 < i <= 3)

    '''
    容器型： list：列表对象
            tuple：元组对象
            dict：字典对象
            set：集合对象
    '''
    # list变量：
    lst = [1, 3, 5]

    # tuple型对象，右侧容器是闭合的，一旦创建元组后，便不能再向容器中增删元素
    tup = (1, 3, 5)
    # 单元素的元组后面必须保留一个逗号，才能被解释为元组
    tup = (1,)
    print(type(tup))
    # tup = (1)
    # print(type(tup))

    # 使用一对花括号 {} ，另外使用冒号:，创建一个dict对象
    dic = {'a': 1, 'b': 3, 'c': 5}

    # 仅仅使用一对花括号 {}，创建一个set对象
    st = {1, 3, 5}

    value = score_mean(lst1=[9.1, 9, 10, 234, 1, 90])
    print(value)

    # 九九乘法表
    multiplicationTable()

    # 样本抽样
    sampleSampling()

