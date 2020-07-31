# _*_ coding: utf-8 _*_
"""
#  @Time : 2020/7/24 12:43
#  @Author : yls
#  @Version：V 0.1
#  @File : d_matplotib.py
#  @desc : Matplotlib 是 Python 中非常强大的 2D 绘图工具。
        提供方便易用的绘图接口，能使用在 Python 脚本，
        IPython shell、Jupyter Notebook、Web 应用服务器等。详情参考：
            https://matplotlib.org/
"""
import numpy as np
import matplotlib.pyplot as plt


def setup_axes():
    """
    绘制三类折线图
    """
    fig, axes = plt.subplots(ncols=3, figsize=(6.5, 3))
    for ax in fig.axes:
        ax.set(xticks=[], yticks=[])
    fig.subplots_adjust(wspace=0, left=0, right=0.93)
    return fig, axes


if __name__ == '__main__':
    """
    绘制三类折线图
    """
    x = np.linspace(0,10,100)
    fig,axes = setup_axes()
    for ax in axes:
        ax.margins(y=0.10)

    for i in range(1, 6):
        axes[0].plot(x, i * x)

    for i, ls in enumerate(['-', '--', ':', '-.']):
        axes[1].plot(x, np.cos(x) + i, linestyle=ls)

    for i, (ls, mk) in enumerate(zip(['', '-', ':'], ['o', '^', 's'])):
        axes[2].plot(x, np.cos(x) + i * x, linestyle=ls, marker=mk, markevery=10)
    plt.show()