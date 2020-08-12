# _*_ coding: utf-8 _*_
"""
 #  @Time : 2020/8/10 16:09 
 #  @Author : yls 
 #  @Version：V 0.1
 #  @File : j_decorator.py
 #  @desc : Python 中使用 @函数名字，放在某些函数上面，起到增强它们功能的作用
            装饰器还在日志管理、图像绘图等有重要的应用。因此，我们很有必要掌握装饰器，逐渐能做到灵活使用。
 """
import asyncio
from functools import wraps
import time
import math
import numpy as np
from scipy.stats import beta, norm, uniform, binom
import matplotlib.pyplot as plt


@asyncio.coroutine
def asyncio_open_conn(host: str):
    """
    使用装饰器 @asyncio.coroutine，将一个生成器asyncio_open_conn 标记为 coroutine 类型。
    Args:
        host: 地址
    """
    print('using asyncio builds web connection')
    connect = yield from asyncio.open_connection(host, 80)
    print('get connect of %s' % (host,))


def call_print(f):
    def g():
        print('you\'re calling %s function' % (f.__name__,))

    return g


def call_print_wraps(f):
    @wraps(f)
    def g():
        print('you\'re calling %s function' % (f.__name__,))

    return g


@call_print
def my_fun():
    pass


@call_print_wraps
def my_fun_02():
    pass


n = 10


def execpter(f):
    """
    案例1、异常次数：
        这个装饰器，能统计出某个异常重复出现到指定次数时，历经的时长。
    Args:
        f:

    Returns:

    """
    i = 0
    t1 = time.time()

    def wrapper():
        try:
            f()
        except Exception as e:
            nonlocal i
            i += 1
            print(f'{e.args[0]}；{i}')
            t2 = time.time()
            if i == n:
                print(f'spending time:{round(t2 - t1, 2)}')

    return wrapper


@execpter
def divide_zero_except():
    time.sleep(0.1)
    j = 1 / (40 - 20 * 2)


@execpter
def outof_range_except():
    a = [1, 3, 5]
    time.sleep(0.1)
    print(a[3])


def my_plot(label0=None, label1=None, ylabel='probability density function', fn=None):
    """
    案例 2：绘图:
        定义带四个参数的画图装饰器
    Args:
        label0:
        label1:
        ylabel:
        fn:

    Returns:

    """

    def decorate(f):
        @wraps(f)
        def myplot():
            fig = plt.figure(figsize=(16, 9))
            ax = fig.add_subplot(111)
            x, y, y1 = f()
            ax.plot(x, y, linewidth=2, c='r', label=label0)
            ax.plot(x, y1, linewidth=2, c='b', label=label1)
            ax.legend()
            plt.ylabel(ylabel)
            # plt.show()
            plt.savefig('./img/%s' % (fn,))
            plt.show()
            plt.close()

        return myplot

    return decorate


@my_plot(label0='b-a=1.0', label1='b-a=2.0', fn='uniform.png')
def unif():
    """
    均匀分布
    """
    x = np.arange(-0.01, 2.01, 0.01)
    y = uniform.pdf(x, loc=0.0, scale=1.0)
    y1 = uniform.pdf(x, loc=0.0, scale=2.0)
    return x, y, y1


@my_plot(label0='n=50,p=0.3', label1='n=50,p=0.7', fn='binom.png', ylabel='probability mass function')
def bino():
    """
    二项分布
    """
    x = np.arange(50)
    n, p, p1 = 50, 0.3, 0.7
    y = binom.pmf(x, n=n, p=p)
    y1 = binom.pmf(x, n=n, p=p1)
    return x, y, y1


@my_plot(label0='u=0.,sigma=1.0', label1='u=0.,sigma=2.0', fn='guass.png')
def guass():
    """
    高斯分布
    """
    x = np.arange(-5, 5, 0.1)
    y = norm.pdf(x, loc=0.0, scale=1.0)
    y1 = norm.pdf(x, loc=0., scale=2.0)
    return x, y, y1


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # connections = [asyncio_open_conn(host) for host in ['www.sina.com', 'www.baidu.com']]
    # loop.run_until_complete(asyncio.wait(connections))
    # loop.close()

    # my_fun()
    # print(my_fun)
    # my_fun_02()
    # print(my_fun_02)

    # for _ in range(n):
    #     divide_zero_except()
    #
    # for _ in range(n):
    #     outof_range_except()

    # 均匀分布
    # unif()

    # 二项分布
    # bino()

    # 高斯分布
    guass()
    pass
