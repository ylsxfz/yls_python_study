# _*_ coding: utf-8 _*_
"""
#  @Time : 2020/7/24 11:25
#  @Author : yls
#  @Version：V 0.1
#  @File : b_scipy.py
#  @desc : SciPy基于Python，是用于数学计算的工具包。
         详情参考：https://www.scipy.org/
"""
from scipy.stats import norm, uniform, binom
import numpy as np
import matplotlib.pyplot as plt
from functools import wraps


def scipy_fun():
    print()


def my_plot(label0=None, label1=None,
            ylabel='probability density function', fn=None):
    """
    绘图装饰器，带有四个参数，分别表示：legend 的 2 类说明文字、y 轴 label、保存的 PNG 文件名称
    Args:
        label0: legend 的 2 类说明文字
        label1: legend 的 2 类说明文字
        ylabel: y 轴 label
        fn: 保存的 PNG 文件名称

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
            plt.close()

        return myplot

    return decorate


@my_plot(label0='b-a=1.0', label1='b-a=2.0', fn='uniform.png')
def unif():
    """
    均匀分布函数
    """
    x = np.arange(-0.01, 2.01, 0.01)
    y = uniform.pdf(x, loc=0.0, scale=1.0)
    y1 = uniform.pdf(x, loc=0.0, scale=2.0)
    return x, y, y1


@my_plot(label0='n=50,p=0.3', label1='n=50,p=0.7',
         fn='binom.png', ylabel='probability mass function')
def bino():
    """
    二项分布概率密度图
    """
    x = np.arange(50)
    n, p, p1 = 50, 0.3, 0.7
    y = binom.pmf(x, n=n, p=p)
    y1 = binom.pmf(x, n=n, p=p1)
    return x, y, y1


if __name__ == '__main__':
    # 数学计算的包
    # scipy_fun()

    # 均匀分布函数
    # unif()

    # 二项分布
    bino()
    pass
