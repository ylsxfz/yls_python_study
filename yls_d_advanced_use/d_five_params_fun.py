# _*_ coding: utf-8 _*_
"""
#  @Time : 2020/7/31 10:42
#  @Author : yls
#  @Version：V 0.1
#  @File : d_five_params_fun.py
#  @desc : Python函数的5类参数使用详解
             1、位置参数
             2、关键字参数
             3、默认参数
             4、可变位置参数
             5、可变关键字参数
"""
from inspect import signature


def f(a):
    """
    定义一个函函数f，只有一个参数a，
    既可能为：位置参数 ==》f(1) ==》 positional argument
    也可能为：关键字参数 ==》f(a=1) ==》keyword argument
    这取决于调用函数f的传参
    Args:
        a: 参数
    """
    print(f'a:{a}')


def f1(a=0):
    """
    默认参数：
        函数定义的参数a，有个默认值为0
    Args:
        a: 默认值为0的参数
    """
    print(f'a:{a}')


def f2(a, *b, **c):
    """
    函数f的参数稍微显示复杂，但也是最常用的函数定义结构
    1、出现带一个星号的参数b ==》可变位置参数
    2、带两个星号的参数c ==》可变关键字参数
    注意：可变表示函数被赋值的变量个数是变化的。
    Args:
        a: 参数a
        *b: 可变位置参数b
        **c: 可变关键字参数c
    """
    print(f'a:{a},b:{b},c:{c}')


def f3(a, *b):
    print(f'a:{a},b:{b}')


def f4(*, a, **b):
    """
    参数a只能为KEYWORD_ONLY关键字参数。因为参数a前面有个星号，
    星号后面的参数a只可能是关键字参数，而不能是位置参数。
    Args:
        a:
        **b:

    Returns:

    """
    print(f'a:{a},b:{b}')


if __name__ == '__main__':
    # 位置参数
    # f(1)

    # 关键字参数
    # f(a=1)

    # 默认值参数
    # 按照a的默认值调用
    # f1()

    # 默认参数a值为1
    # f1(1)

    # 可变位置参数、可变关键字参数
    # f2(1, 2, 3, w=4, h=5)
    # f2(1, 2, w=4)

    # 查看参数类型
    for name, val in signature(f3).parameters.items():
        print(name, val.kind)

    for name,val in signature(f4).parameters.items():
        print(name,val.kind)

    f4(a=1,w=4,h=5)
    pass
