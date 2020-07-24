# -*- coding: UTF-8 -*-
"""
 @Time: 2020/7/20 22:53
 @Author: yls 
 @Version: V 0.1
 @File: h_dict_set.py
 @Desc: dict和set的15个经典使用例子
"""

from heapq import nlargest
from collections import defaultdict
from collections import ChainMap


def dict_update():
    """
    更新字典
    """
    d = {'a': 1, 'b': 2}
    d.update({'c': 3, 'd': 4, 'e': 5})
    print(d)

    d.update([('c', 3), ('d', 4), ('e', 6)])
    print(d)

    d.update([('c', 4), ('d', 5)], e=5)
    print(d)


def dict_setdefault():
    """
    如果仅当字典中不存在某个键值对时，才插入到字典中；如果存在，不必插入（也就不会修改键值对）。
    这种场景，使用字典自带方法 setdefault
    """

    d = {'a': 1, 'b': 2}
    r = d.setdefault('c', 3)
    print(r)
    print(d)

    r = d.setdefault('b', 23)
    print(r)
    print(d)


def dict_union(d1, d2):
    """
    合并字典
    Args:
        d1: 字典d1
        d2: 字典d2

    Returns:
        字典d1和字典d2的并集
    """
    return {**d1, **d2}


def dict_difference(d1, d2):
    """
    字典的差集
    Args:
        d1: 字典d1
        d2: 字典d2

    Returns:
        字典d1和字典d2的差集
    """
    return dict([(k, v) for k, v in d1.items() if k not in d2])


def dict_sort_by_key(d):
    """
    字典按键排序
    Args:
        d: 字典d

    Returns:
        返回字典d按照键排序的结果
    """
    return sorted(d.items(), key=lambda x: x[0])


def dict_sort_by_value(d):
    """
    字典按值排序：
        与按照键排序原理相同，按照值排序时，key 函数定义为按值（x[1]）比较。
        为照顾小白，解释为什么是 x[1]。
        d.items() 返回元素为 (key, value) 的可迭代类型（Iterable），
        key 函数的参数 x 便是元素 (key, value)，所以 x[1] 取到字典的值。
    Args:
        d: 字典d

    Returns:
        返回字典d按照值排序的结果
    """
    return sorted(d.items(), key=lambda x: x[1])


def dict_max_key(d):
    """
    获取最大键
    通过 keys 拿到所有键，获取最大键，返回 (最大键,值) 的元组
    Args:
        d: 字典d

    Returns:
        返回(最大键,值) 的元组
    """
    if len(d) == 0:
        return []
    max_key = max(d.keys())
    return (max_key, d[max_key])


def dict_max_value(d):
    """
    最大值的字典，可能有多对：
    Args:
        d: 字典d

    Returns:
        返回(最大键,值) 的元组

    """
    if len(d) == 0:
        return []
    max_val = max(d.values())
    return [(key, max_val) for key in d if d[key] == max_val]


def set_max_min(s):
    """
    获取字典的最值：(最小值，最大值)
    Args:
        s: 集合s

    Returns:
        返回(最小值,最大值) 的元组

    """
    return (min(s), max(s))


def set_single(string):
    """
    若组成字符串的所有字符仅出现一次，则被称为单字符串。
    Args:
        string: 字符串

    Returns:
        True：表示为单字符串
        False：表示不是单字符串
    """
    return len(set(string)) == len(string)


def set_logger(s1, s2):
    """
    key 函数定义为按照元素长度比较大小，找到更长的集合：
    Args:
        s1: 集合s1
        s2: 集合s2

    Returns:
        返回较长的集合
    """
    return max(s1, s2, key=lambda x: len(x))


def set_max_overlap(lst1, lst2):
    """
    在两个列表中，找出重叠次数最多的元素。默认只返回一个。
    解决思路：
        1、求两个列表的交集
        2、遍历交集列表中的每一个元素，min(元素在列表 1 次数, 元素在列表 2 次数) ，就是此元素的重叠次数
        3、求出最大的重叠次数
    Args:
        lst1: 列表lst1
        lst2: 列表lst2

    Returns:
        返回重叠次数最多的元素
    """
    overlap = set(lst1).intersection(lst2)
    ox = [(x, min(lst1.count(x), lst2.count(x))) for x in overlap]
    return max(ox, key=lambda x: x[1])


def dict_topn(d, n):
    """
    找出字典前 n 个最大值，对应的键。
    导入 Python 内置模块 heapq 中的 nlargest 函数，获取字典中的前 n 个最大值。
    Args:
        d: 字典d
        n: 前nge

    Returns:
        返回字典中的前 n 个最大值
    """
    return nlargest(n, d, key=lambda k: d[k])


def dict_defauldict():
    """
    一键对多个值的实现方法:
        可以使用 collections 模块中的 defaultdict，它能创建属于某个类型的自带初始值的字典。使用起来更加方便：
    Returns:
        返回字典
    """
    d1 = {}
    lst = [(1, 'apple'), (2, 'orange'), (1, 'compute')]
    for k, v in lst:
        if k not in d1:
            d1[k] = []
        d1[k].append(v)
    print(d1)

    d2 = {}
    d2 = defaultdict(list)
    for k, v in lst:
        d2[k].append(v)
    print(d2)


def dict_merged():
    """
    修改 merged['x']=10，dic1 中的 x 值不变，merged 是重新生成的一个“新字典”。
    """
    dic1 = {'x': 1, 'y': 2}
    dic2 = {'y': 3, 'z': 4}
    merged1 = {**dic1, **dic2}
    print(merged1)

    """
    collections 模块中的 ChainMap 函数却不同，它在内部创建了一个容纳这些字典的列表。
    使用 ChainMap 合并字典，修改 merged['x']=10 后，dic1 中的 x 值改变。
    """
    merged2 = ChainMap(dic1, dic2)
    print(merged2)

    # dic1的值也会改变，共用内存的结果
    merged2['x'] = 10
    print(dic1)


if __name__ == '__main__':
    # 更新
    # dict_update()

    # setdefault()方法
    # dict_setdefault()

    # 字典的并集
    # print(dict_union({'a': 1, 'b': 2}, {'c': 4, 'd': 5}))

    # 字典的差集
    # print(dict_difference({'a': 1, 'b': 2}, {'c': 4, 'd': 5}))

    # 字典按照键排序
    # print(dict_sort_by_key({'c': 4, 'd': 5, 'aL': 1, 'b': 2}))

    # 字典按照值排序
    # print(dict_sort_by_value({'c': 4, 'd': 5, 'a': 67, 'b': 2}))

    # 获取最大键
    # print(dict_max_key({'c': 4, 'd': 5, 'a': 67, 'b': 2}))

    # 获取最大字典值
    # print(dict_max_value({'c': 4, 'd': 5, 'a': 67, 'b': 67}))

    # 获取集合最小值，最大值
    # print(set_max_min({4, 5, 67, 67}))

    # 单字符串
    # print(set_single("love_python"))
    # print(set_single('python'))

    # 更长的集合
    # print(set_logger({1, 2, 3, 45, 56, 52}, {1, 21, 12412, 4}))

    # 重复最多
    print(set_max_overlap([1, 2, 2, 2, 3, 3], [2, 2, 3, 2, 2, 3]))

    # 获取字典中的前 n 个最大值
    print(dict_topn({'a': 10, 'b': 8, 'c': 9, 'd': 10}, 3))

    # 一键对多值字典
    dict_defauldict()

    # 逻辑上的字典合并
    dict_merged()
    pass
