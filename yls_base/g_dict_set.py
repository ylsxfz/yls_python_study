# _*_ coding: utf-8 _*_
"""
 @Time : 2020/7/20 13:28 
 @Author : yls 
 @Version：V 0.1
 @File : g_dict_set.py
 @desc : dict(字典) 和 set(集合对象)
 """


def dict_create():
    # 1、手动创建
    empty = {}
    dic = {'a': 1, 'b': 3, 'c': 12}
    print(dic)

    # 2、使用dict()构造函数
    dit = dict(a=1, b=11, c=22)
    print(dit)

    # 3、键值对 + 关键字参数：第一个参数为字典，后面是一系列关键字参数，如 c=3
    dit = dict({'a': 1, 'b': 2}, c=3, d=4)
    print(dit)

    # 4、迭代对象
    dit = dict([('a', 1), ('b', 2)], c=3)
    print(dit)

    {}.fromkeys(['k1','k2','k2'])


if __name__ == '__main__':
    dict_create()
    pass
