# _*_ coding: utf-8 _*_
"""
 #  @Time : 2020/8/14 15:33 
 #  @Author : yls 
 #  @Version：V 0.1
 #  @File : k_logging_pit_point.py
 #  @desc : python 常见的10个坑点合集和logging日志管理模块的使用总结。
        1、列表和 * 操作:
            原来 * 操作复制出的 a[0]、a[1]、...、a[5]，在内存中标识符是相等的，实现的仅仅是浅复制。
            不使用 *，使用列表生成式，复制出 5 个不同 id 的内嵌列表，这样就能避免赋值互不干扰的问题。

        2、列表内元素可重复出现，讨论如何删除列表中的某个元素:
            遍历 lst、remove 一次，移掉位置 i 后的所有元素索引都要减一。
            一旦删除的元素，重复出现在列表中，就总会漏掉一个该删除的元素。

        3、Python 函数的参数可设为默认值，如果一个默认参数类型为list，默认值为设置为[]
          为了避免这个隐藏的坑，函数的默认参数值切记不能设置为 []，而是为 None。这样即便按照默认值调用多次，也会规避此风险。

        4、{} 和 ()：
            初始创建的元组对象，若只有一个元素，只用一对括号是不够的，下面 single 对象不会被解释为元组，而是 float 型。
            还有创建集合与字典，它们都用一对 {}，但是默认返回字典，而不是集合。
            要想创建空集合，可使用内置函数 set()。

        5、解包：Python 中，支持多值赋值给多变量的操作。最常见的用法，一行代码交换两个变量。
            记住一点：多值赋值是先计算出等号右侧的所有变量值后，再赋值给等号左侧变量。
            这种多值赋值，是一种解包（unpack）操作。
            既然是解包，那么就得先有打包。的确，等号右侧的多个变量，会被打包（pack）为一个可迭代对象。
            赋值操作，就相当于解包。

        6、访问控制：
            a、Python 是一门动态语言，支持属性的动态添加和删除。
            而 Python 面向对象编程（OOP）中，提供很多双划线开头和结尾的函数，
            它们是系统内置方法，被称为魔法方法。
            如 __getattr__ 和 __setattr__ 是关于控制属性访问的方法。
            b、重写 __getattr__ 方法，会定义不存在属性时的行为。如下，访问类不存在属性时，程序默认会抛出 AttributeError 异常。
 """


def list_more():
    """
    列表和 * 操作:
        原来 * 操作复制出的 a[0]、a[1]、...、a[5]，在内存中标识符是相等的，实现的仅仅是浅复制。
        不使用 *，使用列表生成式，复制出 5 个不同 id 的内嵌列表，这样就能避免赋值互不干扰的问题。
    """
    print(['|'] * 10)
    print([[]] * 5)
    a = []
    a = [[]] * 5
    a[0].extend([1, 3, 5])
    a[1].extend([2, 4, 6])
    print(a)

    b = [[] for _ in range(5)]
    b[0].extend([1, 3, 5])
    b[1].extend([2, 4, 6])
    print(b)


def list_del(lst, e):
    """
    列表内元素可重复出现，讨论如何删除列表中的某个元素:
        遍历 lst、remove 一次，移掉位置 i 后的所有元素索引都要减一。
        一旦删除的元素，重复出现在列表中，就总会漏掉一个该删除的元素。
    """
    i = 0
    while i < len(lst):
        if lst[i] == e:
            lst.remove(lst[i])
        else:
            i += 1
    return lst


# def delta_val(val, volume=[]):
def delta_val(val, volume=None):
    """
    Python 函数的参数可设为默认值，如果一个默认参数类型为list，默认值为设置为[]

    为了避免这个隐藏的坑，函数的默认参数值切记不能设置为 []，而是为 None。这样即便按照默认值调用多次，也会规避此风险。
    Args:
        val: 参数
        volume: 默认为空的参数
    """
    print(id(volume))
    if volume is None:
        volume = []
    size = len(volume)
    for i in range(size):
        volume[i] = i + val
    return volume


def dict_tuple():
    point = (1.0, 3.0)
    # 初始创建的元组对象，若只有一个元素，只用一对括号是不够的，
    # 下面 single 对象不会被解释为元组，而是 float 型。
    single = (1.0)
    print(type(single))
    # 要想被解释为元组，在后面必须要加一个逗号：
    single = (1.0,)
    print(type(single))


def fix_points(pts):
    for i in range(len(pts)):
        t = pts[i]
        if isinstance(t, tuple):
            t = t if len(t) == 2 else (t[0], 0.0)
            pts[i] = t
        else:
            raise TypeError('pts 的元素类型要求为元组')
    return pts


def set_dict():
    """
    还有创建集合与字典，它们都用一对 {}，但是默认返回字典，而不是集合。
    要想创建空集合，可使用内置函数 set()。
    """
    d = {}
    print(type(d))

    s = set()
    print(type(s))


def unpack():
    """
    支持多值赋值给多变量的操作:
        多值赋值是先计算出等号右侧的所有变量值后，再赋值给等号左侧变量。
        这种多值赋值，是一种解包（unpack）操作。
        既然是解包，那么就得先有打包。的确，等号右侧的多个变量，会被打包（pack）为一个可迭代对象。
        赋值操作，就相当于解包。
    """
    a, b = 1, 2
    a, b = b + 1, a + b
    print(a, b)

    def foo():
        result = [1, 'xiaoming', 'address', 'telephone', ['', '', '...']]
        return result

    sid, name, *others = foo()
    print(sid)
    print(name)
    print(others)


if __name__ == '__main__':
    # list和 * 操作
    # list_more()

    # list删除元素
    # reult = list_del([1, 2, 4, 53, 2, 2, 23, 2, 523, 5], 2)
    # print(reult)

    # 函数的默认参数为空
    # result = delta_val(10)
    # print(result)
    # result.append(1)
    # result.append(2)
    # print(result)
    # result = delta_val(10)
    # print(result)

    # {} 和 ()
    # dict_tuple()
    # 下面这行调用会报错：TypeError: pts 的元素类型要求为元组
    # fix_points([(1.0,3.0),(2.0),(5.0,4.0)])
    # result = fix_points([(1.0, 3.0), (2.0,), (5.0, 4.0)])
    # print(result)

    # 集合和字典
    # set_dict()

    # 解包
    unpack()
    pass
