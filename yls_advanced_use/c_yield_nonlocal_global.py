# # _*_ coding: utf-8 _*_
"""
#  @Time : 2020/7/30 10:18
#  @Author : yls
#  @Version：V 0.1
#  @File : c_yield_nonlocal_global.py
#  @desc : 很多 Python 开发者，尤其是新手，对 yield 关键字总是望而生畏，
        据 Stack Overflow 网站统计，yield 关键字的被提问频次高居Python类首位。
"""
from math import ceil


def yield_fun():
    """
    直观理解 yield
        要想通俗理解 yield，可结合函数的返回值关键字 return，yield 是一种特殊的 return。说是特殊的 return，是因为执行遇到 yield 时，
        立即返回，这是与 return 的相似之处。
        不同之处在于：下次进入函数时直接到 yield 的下一个语句，而 return 后再进入函数，还是从函数体的第一行代码开始执行。
        带 yield 的函数是生成器，通常与 next 函数结合用。下次进入函数，意思是使用 next 函数进入到函数体内。
    Returns:
    """

    # return 的用法
    def f():
        print("enter f...")
        return 'hello'

    ret = f()
    print(ret)

    # yield 的用法
    def f1():
        print('enter f...')
        yield 4
        print('i am next sentence of yield')

    g = f1()
    print(g)

    next(g)
    # 抛出一个StopIteration异常，表示已经迭代结束。
    # 此处确实已经迭代完毕，所以该异常无须理会。
    next(g)


def yield_myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


def not_yield_myrange(stop):
    start = 0
    result = []
    while start < stop:
        result.append(start)
        start += 1
    return result


def yeild_send():
    """
    带 yield 的生成器对象里还封装了一个 send 方法:
        1、g = f()：创建生成器对象，什么都不打印
        2、print(next(g))：进入 f，打印enter f...，并 yield 后返回值 4，并打印 4
        3、print('ready to send')
        4、print(g.send(10))：send 值 10 赋给 result，执行到上一次 yield 语句的后一句打印出 send me a value is:10
        5、遇到 return 后返回，因为 f 是生成器，同时提示 StopIteration
        注意：
            通过以上分析，能体会到 send 函数的用法：它传递给 yield 左侧的 result 变量。
            return 后抛出迭代终止的异常，此处可看作是正常的提示。
    """
    print('enter f....')
    while True:
        result = yield 4
        if result:
            print('send me a value is:%d' % (result,))
            return
        else:
            print('no send')


def yield_list(lst):
    """
    完全展开list
    Args:
        lst: 列表
    """
    for i in lst:
        if type(i) == list:
            yield from yield_list(i)
        else:
            yield i


def yield_list_group(lst, n):
    if n < 0:
        yield lst
        return
    i, div = 0, ceil(len(lst) / n)
    while i < n:
        yield lst[i * div:(i + 1) * div]
        i += 1


def nonlocal_fun():
    """
    关键词：nonlocal常用于函数嵌套中，声明变量为：非局部变量。
    """
    i = 0

    def auto_increase():
        nonlocal i
        if i >= 10:
            i = 0
        i += 1

    ret = []
    for _ in range(28):
        auto_increase()
        ret.append(i)
    print(ret)


i = 5


def global_fun():
    """
    global：一个变量被多个函数引用，想让全局变量被所有函数共享
    """

    def f():
        print(i)

    def g():
        print(i)
        pass

    f()
    g()

    def h():
        """
        在函数 h 内，显示地告诉解释器 i 为全局变量，
        然后，解释器会在函数外面寻找 i 的定义，执行完 i+=1 后，
        i 还为全局变量，值加 1
        """
        global i
        i += 1

    h()
    f()


if __name__ == '__main__':
    # yield_fun()
    # 使用yeild，整个过程的复杂度都是O(1)
    # for i in yield_myrange(10):
    #     print(i)

    # 不使用yeild，采用普通的方法，创建一个序列，空间复杂度都是O(n)
    # for i in not_yield_myrange(10):
    #     print(i)

    # 带 yield 的生成器对象里还封装了一个 send 方法
    # g = yeild_send()
    # print('*******************》g《**********************')
    # print(g)
    # print('*******************》next(g)《******************')
    # print(next(g))
    # print('*******************》g.send(10)《******************')
    # print(g.send(10))

    # 使用yield：完全展开list
    # gen = yield_list([1, ['s', 3], 23, 423, 4, 2])
    # print(gen)
    # for i in gen:
    #     print(i)

    # 使用yield：对列表分组
    # print(list(yield_list_group([1, 2, 3, 4, 5], 0)))
    # print(list(yield_list_group([1, 2, 3, 4, 5], 2)))

    # 关键词 nonlocal 常用于函数嵌套中，声明变量为：非局部变量
    # nonlocal_fun()

    # global：一个变量被多个函数引用，想让全局变量被所有函数共享
    global_fun()
    pass
