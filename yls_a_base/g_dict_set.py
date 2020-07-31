# _*_ coding: utf-8 _*_
# -------------------------------------------------------------------------------
#  @Time : 2020/7/20 13:28
#  @Author : yls
#  @Version：V 0.1
#  @File : g_dict_set.py
#  @desc : dict(字典) 和 set(集合对象)
#         基本操作包括：
#             1、创建字典
#             2、遍历字典
#             3、获取所有键集合（keys）
#             4、获取所有值集合（values）
#             5、获取某键对应的值
#             6、添加、修改或删除一个键值对
# -------------------------------------------------------------------------------


def dict_create():
    """
    创建字典(dict)的5种方式
    Returns:

    """
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

    # fromkeys()方法，已知键集合(keys),vlaues为初始值
    dit = {}.fromkeys(['k1', 'k2', 'k3'], [1, 2, 3])
    print(dit)

    dit = {'a': 1, 'b': 2}.fromkeys(['c', 'd'], [1, 2])
    print(dit)


def dict_base_operation():
    """
    字典的基本操作：增删改查
    """
    # 创建字典
    d = {'a': 1, 'b': 2, 'c': 3}

    # 字典的遍历
    for key, val in d.items():
        print(key, val)

    print("获取所有的key：" + str(set(d)))
    print("获取所有的key：" + str(set(d.keys())))
    print("获取所有的value：" + str(set(d.values())))

    # 判断键是否在字典中
    if 'c' in d:
        print("键c在字典d中！")

    if 'e' not in d:
        print("键e不在字典e中！")

    print("获取键b的value：" + str(d.get('b')))

    d['d'] = 4
    print("添加键d：" + str(d))

    d['a'] = 11
    print("修改键a：" + str(d))

    del d['b']
    print("del方法删除键b：" + str(d))

    d.pop('c')
    print('pop方法删除键c：' + str(d))


def dict_view():
    """
    字典视图：
        字典自带的三个方法 d.items()、d.keys()、d.values()
        它们都是原字典的视图，修改原字典对象，视图对象的值也会发生改变

        特别注意：哈希的对象才能作为字典的键，不可哈希的对象不能作为字典的键。
                因为列表是可变对象，而可变对象是不可哈希的
                如果把lst作为键，会抛出异常：不可哈希的类型 list。
    """
    d = {'a': 1, 'b': 2, 'c': 3}
    print(d)

    print(d.keys())
    print(d.values())
    print(d.items())

    try:
        lst = [1, 2]
        d = {lst: 'ok?'}
    except Exception as e:
        # 会打印：unhashable type: 'list'
        print(e)


def set_basic_operation():
    """
    集合是一种不允许元素出现重复的容器
        1、判断一个列表中是否含有重复元素，便可借助集合这种数据类型
        2、与字典（dict）类似，集合（set）也是由一对花括号（{}）创建。但是，容器内的元素不是键值对
        3、同字典类似，集合内的元素必须是可哈希类型（hashable）：这就意味着 list、dict 等不可哈希的对象不能作为集合的元素。
    """

    lst = [1, 2, 3, 56, 12, 1, 4]
    print(str(lst) + "中是否包含重复元素：" + str(len(lst) != len(set(lst))))

    # 创建set
    a = {1, 2, 34, 55, 326, 2346, 23, 2}
    print(a)

    # 另一种创建集合的方法，是通过 Python 的内置的 set 函数，参数类型为可迭代对象 Iterable
    a = set([1, 2, 342, 425, 523, 2, 1, 23512])
    print(a)


def set_common_method():
    a = {1, 3, 5, 7}
    b, c = {3, 4, 5, 6}, {6, 7, 8, 9}
    print("a:" + str(a))
    print("b:" + str(b))
    print("c:" + str(c))

    # 并集
    e = a.union(b)
    print("a,b的并集：" + str(e))
    d = a.union(b, c)
    print("a,b,c的并集" + str(d))

    # 差集
    d = a.difference(b, c)
    print("a,b,c的差集：" + str(d))

    # 交集
    d = a.intersection(b, c)
    print("a,b,c的交集：" + str(d))

    d = a.intersection(b)
    print("a,b的交集：" + str(d))

    print("a是b的子集：" + str(a.issubset(b)))


if __name__ == '__main__':
    # 创建字典
    # dict_create()

    # 字典的基本操作
    # dict_base_operation()

    # 字典视图
    # dict_view()

    # set的基本操作
    # set_basic_operation()

    # set的常用方法
    set_common_method()
    pass
