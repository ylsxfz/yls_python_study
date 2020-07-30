# _*_ coding: utf-8 _*_
# """
#  @Time : 2020/7/24 12:55
#  @Author : yls
#  @Version：V 0.1
#  @File : e_seaborn.py
#  @desc : Seaborn 是一个基于 Matplotlib 的 Python 数据可视化库，
#         提供绘制更加高层和优美的图形接口。详情参考：
#             http://seaborn.pydata.org/
#         如下，绘制模型拟合后的残差图，y 值添加一个正态分布的误差。
#  """

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


if __name__ == '__main__':
    """
    残差图看出，y 值误差符合均值 0、方差 0.1 的正态分布规律。
    """
    sns.set(style='whitegrid')
    rs = np.random.RandomState(1)
    x = rs.normal(2,0.1,50)
    y = 2 + 1.6*x+rs.normal(0,0.1,50)
    sns.residplot(x,y,lowess=True,color='orange')
    plt.show()
    pass
