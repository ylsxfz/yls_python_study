# _*_ coding: utf-8 _*_
"""
 @Time : 2020/7/24 12:59 
 @Author : yls 
 @Version：V 0.1
 @File : f_scikit_learn.py
 @desc : scikit-learn 是适用于数据处理和机器学习处理非常强大的库。提供数据降维、回归、聚类、分类等功能，是机器学习从业者的必备库之一。详情参考：
            https://scikit-learn.org/
        案例：鸢尾属植物数据集（iris）分类。
            鸢尾属植物数据集一共有 4 个特征，target 值有 3 类，每一类都有 50 个样本。
            四维数据集为了在二维平面内展示方便，只选取其中两个维度。
 """

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    sns.set(style='ticks')
    df = sns.load_dataset('files\\iris')
    df02 = df.iloc[:,[0,2,4]]
    print(df02)
    sns.pairplot(df02,hue='species')
    plt.show()
    pass
