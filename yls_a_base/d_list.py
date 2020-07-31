# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/7/19 20:23
#  @Author: yls
#  @Version: V 0.1
#  @File: d_list.py
#  @Desc: 列表的基本操作：增删改查，可变容器
"""

from copy import deepcopy


def basicList():
    """
    list的基本操作：
        append：在尾部添加元素
        insert：指定索引位置插入元素
        remove：根据值移除所有对应的元素
    """

    # list的基本操作
    empty = []
    lst = [1, 'xiaoming', 29.5, '13712345678']
    lst2 = ['001', '2019-11-11', ['三文鱼', '电烤箱']]
    print(len(empty))
    print(len(lst))
    print(len(lst2))

    # 遍历list
    for _ in lst:
        print(f'{_}的类型为：{type(_)}')

    # 添加元素，同时会修改lst2的值
    sku = lst2[2]

    # 使用列表的append方法增加元素，append默认增加元素在sku列表的尾部
    sku.append('烤鸭')
    sku.append('三文鱼')
    print("sku：" + str(sku) + "\nlst2：" + str(lst2) + "\n")

    # insert指定索引1处插入“牛腱子”
    sku.insert(1, '牛腱子')
    print("sku：" + str(sku) + "\nlst2：" + str(lst2) + "\n")

    # pop方法可以直接移除列表尾部的元素
    sku.pop()
    print("sku：" + str(sku) + "\nlst2：" + str(lst2) + "\n")

    # remove方法可以移除指定的元素，remove会移除所以叫“三文鱼”的值
    sku.remove('三文鱼')
    print("sku：" + str(sku) + "\nlst2：" + str(lst2) + "\n")


def depthCopy():
    """
    copy：浅拷贝
    deepcopy：深拷贝
    """
    # 在basicList操作sku的元素时，lst2的索引为2的元素也在随着变化，
    # 因为sku和lst2指向的内存区域是一样的
    lst2 = ['001', '2019-11-11', ['三文鱼', '电烤箱']]

    # 浅拷贝
    # copy函数：仅仅是对内嵌对象的一层拷贝，属于shallow copy
    sku_deep = lst2[2].copy()
    sku_deep.append('鲤鱼')
    print("sku_deep：" + str(sku_deep) + "\nlst2：" + str(lst2) + "\n")

    a = [1, 2, [3, 4, 5]]
    ac = a.copy()
    ac[0] = 10
    ac[2][1] = 40
    print("a：" + str(a) + "\nac：" + str(ac))
    print("a[0] == ac[0]：" + str(a[0] == ac[0]))
    print("a[2][1] == ac[2][1]：" + str(a[2][1] == ac[2][1]) + "\n")

    # 深拷贝
    b = [1, 2, [3, 4, 5]]
    bc = deepcopy(b)
    b[0] = 10
    bc[2][1] = 40
    bc[0] = 10
    bc[2][1] = 40
    print("b：" + str(b) + "\nbc：" + str(bc))
    print("b[0] == bc[0]：" + str(b[0] == bc[0]))
    print("b[2][1] == bc[2][1]：" + str(b[2][1] == bc[2][1]))


def section():
    """
    切片
    使用 a[:3] 获取列表 a 的前三个元素，形象称这类操作为“切片”，切片本身也是一个列表 [1,4,7]：
    使用 a[-1] 获取 a 的最后一个元素，返回 int 型，值为 19；
    使用 a[:-1] 获取除最后一个元素的切片 [1, 4, 7, 10, 13, 16]；
    使用 a[1:5] 生成索引为 [1,5)（不包括索引 5）的切片 [4, 7, 10, 13]；
    使用 a[1:5:2] 生成索引 [1,5) 但步长为 2 的切片 [4,10]；
    使用 a[::3] 生成索引 [0,len(a)) 步长为 3 的切片 [1,10,19]；
    使用 a[::-3] 生成逆向索引 [len(a),0) 步长为 3 的切片 [19,10,1]。
    逆向：从列表最后一个元素访问到第一个元素的方向。
    """
    # 利用内置函数range(start,stop,step)生成序列数据
    a = list(range(1, 20, 3))
    print(a)
    # 列表的逆向切片
    print(reverse(a))


def reverse(lst):
    """
    列表的逆向切片
    Args:
        lst: list列表
    """
    return lst[::-1]


if __name__ == '__main__':
    # list的基本操作
    # basicList()
    # 浅拷贝和深拷贝
    # depthCopy()
    # 切片
    section()
