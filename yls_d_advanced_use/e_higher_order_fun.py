# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/02 09:42 
#  @Author: yls 
#  @Version: V 0.1
#  @File: e_higher_order_fun.py
#  @Desc: 5个常用的高阶函数、3个创建迭代器的函数，共8个内置函数。
        1、filter(function,iterable):过滤器，过滤掉不满足函数function的元素，重新返回一个新的迭代器。
            该函数定义：def filter_self(function,iterable):
                            return iter([ item for item in iterable if function(item) ])
            filter_self函数接收一个function作为参数，满足条件的元素才得以保留。

        2、map(function,itreable):它将function映射于iterable中的每一项，并返回一个新的迭代器。

        3、
"""


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

    map_self()
    pass
