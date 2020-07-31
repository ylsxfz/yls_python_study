# _*_ coding: utf-8 _*_
"""
#  @Time : 2020/7/31 10:42
#  @Author : yls
#  @Version：V 0.1
#  @File : d_five_params_fun.py
#  @desc :
        Python函数的5类参数使用详解
             1、位置参数
             2、关键字参数
             3、默认参数
             4、可变位置参数
             5、可变关键字参数

        函数调用时，常见的6种错误：
            1、SyntaxError: positional argument follows keyword argument：
                位置参数位于关键字参数后面。
            2、TypeError: f() missing 1 required keyword-only argument: 'b'：
                必须传递的关键字参数缺失。
            3、SyntaxError: keyword argument repeated：
                关键字参数重复。
            4、TypeError: f() missing 1 required positional argument: 'b'：
                必须传递的位置参数缺失。
            5、TypeError: f() got an unexpected keyword argument 'a'
                没有这个关键字参数。
            6、TypeError: f() takes 0 positional arguments but 1 was given：
                不需求位置参数但却传递1个

        参数传递规则：
            1、不带默认值的位置参数缺一不可。
            2、关键字参数必须在位置参数右边。
            3、对同一个形参不能重复传值。
            4、默认参数的定义应该在位置形参的右面。
            5、可变位置参数不能传入关键字参数。
            6、可变位置参数不能传入位置参数。
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


def rule_one(a):
    """
    规则1：不带默认值的位置参数缺一不可。
    最常见的参数类型
    Args:
        a: 不带默认值的位置参数
    """
    print(f'a:{a}')


def rule_two(a, b):
    """
    规则2：关键字参数必须在位置参数右边
    Args:
        a: 参数a
        b: 参数b
    """
    print(f'a:{a},b:{b}')


def rule_three(a, **b):
    """
    规则3：对同一个形参不能重复传值
    Args:
        a: 参数
        **b: 可变关键你在参数
    """
    print(f'a:{a},b:{b}')


def rule_four(a, b=1):
    """
    规则4：默认参数的定义应该在位置参数的右面
    Args:
        a: 位置参数
        b: 默认参数
    """
    print(f'a:{a},b:{b}')


def rule_five(*a):
    """
    规则5：可变位置参数不能传入关键字参数
    Args:
        *a: 可变位置参数
    """
    print(f'a:{a}')


def rule_six(**a):
    """
    规则6：可变关键字参数不能传入位置参数
    Args:
        **a: 可变位置参数
    """
    print(a)


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
    # for name, val in signature(f3).parameters.items():
    #     print(name, val.kind)

    # for name,val in signature(f4).parameters.items():
    #     print(name,val.kind)

    # f4(a=1,w=4,h=5)

    # 规则1：不带默认值得位置参数缺一不可
    rule_one(6)

    # 规则2：关键字参数必须在位置参数右边
    rule_two(1, 6)
    rule_two(1, b=6)

    # 规则3：对同一个形参不能重复传值
    # keyword argument repeated
    # rule_three(1,b=1,b=1)
    rule_three(1, b=2)

    # 规则4：默认参数的定义应该咋位置形参的右面
    rule_four(1, b=12)

    # 规则5：可变位置参数不能传入关键字参数
    rule_five(1, 2, 3)

    # 规则6：可变关键字参数不能传入位置参数
    # rule_six() takes 0 positional arguments but 1 was given
    # rule_six(1)
    rule_six(a=1)
    pass
