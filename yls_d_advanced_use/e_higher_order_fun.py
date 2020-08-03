# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/02 09:42 
#  @Author: yls 
#  @Version: V 0.1
#  @File: e_higher_order_fun.py
#  @Desc: 5个常用的高阶函数、3个创建迭代器的函数，共8个内置函数。
        **********************************************》高阶函数《************************************************************
        1、filter(function,iterable):过滤器，过滤掉不满足函数function的元素，重新返回一个新的迭代器。
            该函数定义：def filter_self(function,iterable):
                            return iter([ item for item in iterable if function(item) ])
            filter_self函数接收一个function作为参数，满足条件的元素才得以保留。

        2、map(function,itreable):它将function映射于iterable中的每一项，并返回一个新的迭代器。
            注意：map函数支持传入多个可迭代对象。当传入多个可迭代对象时，输出元素的个数等于较短序列长度。

        3、reduce(function,iterable[,initializer]):map生成映射关系，reduce实现归约。
            reduce函数位于functools模块中，使用前需要导入。

        4、reversed(seq):重新生成一个迭代器，对输入的序列实现反转。

        5、sorted(iterable,*,key=None,reverse=False)：实现对序列化对象的排序。
            注意：key参数和reverse参数必须为关键字参数，都可以省略。
                如果可迭代对象的元素是一个复合元素，例如为字典，依据字典键的值，sorted的key函数就会被用到。

        **********************************************》生成迭代器《************************************************************
        1、iter(object[,sentinel])：返回一个严格意义上的可迭代对象，其中，参数sentinel可有可无。
            注意：1、迭代结束后，在 __next__ 时，触发 StopIteration 异常，即迭代器已经执行到最后。
                 2、只要 iterable 对象支持可迭代协议，即自定义了 __iter__ 函数，便都能配合 for 依次迭代输出其元素。

        2、next(iterator,[,default])：返回可迭代对象的下一个元素。

        3、enumerate(iterable,start=0)：enumerate是很有用的一个内置函数，尤其要用到列表索引时。

        总结：
        5 个 重要的高阶函数
            （1）filter：根据条件筛选元素
            （2）map：映射可迭代对象
            （3）reduce：归约可迭代对象
            （4）reversed：反转可迭代对象
            （5）sorted：排序可迭代对象

        3 个 有用的迭代器函数
            （1）iter：返回一个迭代器
            （2）next：返回迭代器的下一项
            （3）enumerate：返回对象的枚举迭代器

"""

from functools import reduce
from collections.abc import Iterator

def filter_self(function, iterable):
    return iter([item for item in iterable if function(item)])


class Student():
    def __init__(self, name, sex, height):
        self.name = name
        self.sex = sex
        self.height = height


def hight_condition(stu):
    if stu.sex == 'male':
        return stu.height > 1.75
    else:
        return stu.height > 1.65


def map_self():
    mylst = [1, 23, 4325, 4235, 25, 5]
    result = map(lambda x: x + 1, mylst)
    print(result)
    print(list(result))

    """
    同时注意到，map 函数支持传入多个可迭代对象。
    当传入多个可迭代对象时，输出元素个数等于较短序列长度
    如下，传入两个列表，function 就需要接受两个参数，取值分别对应第一、第二个列表中的元素。
    找到同时满足第一个列表的元素为奇数，第二个列表对应位置的元素为偶数的元素。
    """
    xy = map(lambda x, y: x % 2 == 1 and y % 2 == 0, [1, 3, 2, 4, 1], [3, 2, 1, 2])
    for i in xy:
        print(i)


def map_vecor_add(x, y):
    """
    借助 map 函数，还能实现向量级运算。
    """
    return list(map(lambda i, j: i + j, x, y))


def reduce_test():
    result = reduce(lambda x, y: x + y, list(range(10)))
    print(result)


def reversed_test():
    result = reversed([1, 4, 2, 3, 1])
    for i in result:
        print(i)


def sorted_test():
    a = [1, 4, 2, 3, 1]
    a = sorted(a, reverse=True)
    print(a)

    a = [{'name': 'xiaoming', 'age': 20, 'gender': 'male'},
         {'name': 'xiaohong', 'age': 18, 'gender': 'female'},
         {'name': 'xiaoli', 'age': 19, 'gender': 'male'}]
    b = sorted(a, key=lambda x: x['age'], reverse=False)
    print(b)


def next_test():
    it = iter([5, 3, 4, 1])
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))


class TestIter(object):
    def __init__(self):
        self._lst = [1, 3, 2, 3, 4, 5]

    def __iter__(self):
        print("__iter__ is called!")
        return iter(self._lst)


def iter_test():
    lst = [1, 3, 4, 5, 6]
    it = iter(lst)
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())


def enumerate_test():
    s = ["a","b","c"]
    for i,v in enumerate(s):
        print(i,v)

    print("手动执行next,依次输出一个tuple：")
    enum = enumerate(s)
    print(next(enum))
    print(next(enum))
    print(next(enum))
    # print(next(enum))


class Decrease(Iterator):
    """
    定制一个递减迭代器：
        编写一个迭代器，通过循环语句，对某个正整数，依次递减1，直到0.
    """
    def __init__(self,init):
        self.init = init

    def __iter__(self):
        return self

    def __next__(self):
        while 0 < self.init:
            self.init -= 1
            return self.init
        raise StopIteration


if __name__ == '__main__':
    # students = [Student('xiiaoming', 'male', 1.74),
    #             Student('xiaoming', 'female', 1.68),
    #             Student('xiaoli', 'male', 1.80)]
    # students_satisfy = filter(hight_condition, students)
    # for stu in students_satisfy:
    #     print(stu.name)
    #
    # students_satisfy = filter_self(hight_condition, students)
    # for stu in students_satisfy:
    #     print("name:%s,height:%s" % (stu.name, str(stu.height)))

    # map_self()

    # lst1 = [1,2,3,4,5,6]
    # lst2 = [3,4,5,6,1,2]
    # result = map_vecor_add(lst1,lst2)
    # print(result)

    # reduce_test()

    # reversed_test()

    # sorted_test()

    # iter_test()

    # next_test()

    # enumerate_test()

    descend_iter = Decrease(6)
    for i in descend_iter:
        print(i)
    pass
