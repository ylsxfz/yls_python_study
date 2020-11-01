# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/11/01 20:07 
#  @Author: yls 
#  @Version: V 0.1
#  @File: f_pandas_kaggle_titanic.py
#  @Desc: pandas实战Kaggle titanic幸存预测之7步数据清洗
#  1、读取csv数据
#  2、预览数据
#  3、统计每一列的空值
#  4、填充空值
#  5、特征工程，子步骤包括删除一些特征列，创建新的特征列，创建数据分箱
#  6、对分类列编码，常用的包括，调用Sklearn中的LabelEncode编码、Pandas编码
#  7、再验证核实
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder


def readFile():
    """
    info：统计数据的每一列类型，是否为null和个数
    Returns:

    """

    '''
    1、读入数据
    '''
    data_raw = pd.read_csv('test/train.csv')
    # print(data_raw)

    '''
    2、数据预览
    '''
    # info()：统计数据的每一列类型，是否为null和个数
    data_raw.info()
    # describe()：统计数据每一列的统计学属性信息，平均值、方差、中位数、分位数等
    count = data_raw.describe(include='all')
    print(count)
    # print(data_raw)

    '''
    3、检查null值
    '''
    # isnull()：逐行逐元素查找元素值是否为null
    # sum()：默认在axis为0上完成一次reduce求和.
    nullCount = data_raw.isnull().sum()
    print(nullCount)

    x_raw = data_raw.columns
    data_null = data_raw.isnull().sum()
    null_rate = data_null.values / len(data_raw)
    plt.bar(x_raw, null_rate)
    plt.xticks(rotation=90)
    # plt.show()

    '''
    4、补全空值
    '''
    plt.figure(figsize=[10, 8])
    notnull_age_index = data_raw['Age'].notnull()
    plt.subplot(221)
    plt.hist(x=data_raw[notnull_age_index]['Age'], color=['orange'])
    plt.subplot(222)
    plt.boxplot(x=data_raw[notnull_age_index]['Age'], showmeans=True, meanline=True)
    # plt.show()

    data_raw['Age'].fillna(data_raw['Age'].median(), inplace=True)
    data_raw['Embarked'].fillna(data_raw['Embarked'].mode()[0], inplace=True)
    null_rate = data_raw.isnull().sum()
    print(null_rate)

    '''
    5、特征工程
    5.1 删除特征列
        axis：参数设置为1，表示轴为列方向
        inplace：True表示就地删除
    '''
    data_raw.drop('Cabin', axis=1, inplace=True)
    drop_column = ['PassengerId', 'Ticket']
    data_raw.drop(drop_column, axis=1, inplace=True)
    print("删除特征值：", data_raw)

    # 增加3个特征列
    data_raw['FamilySize'] = data_raw['SibSp'] + data_raw['Parch'] + 1
    print(data_raw.head(3))
    data_raw['IsAlone'] = np.where(data_raw['FamilySize'] > 1, 0, 1)
    data_raw['Title'] = data_raw['Name'].str.split(", ", expand=True)[1].str.split(".", expand=True)[0]

    '''
    5.3 分箱
    Pandas 提供两种数据分箱方法：qcut、cut
    qcut：方法是基于分位数的分箱技术
    cut：基于区间长度切分为若干    
    '''
    a = [3, 1, 5, 7, 6, 5, 4, 6, 3]
    temp = pd.qcut(a, 3)
    print(temp)

    dfa = pd.DataFrame(a)
    len1 = dfa[(0.999 < dfa[0]) & (dfa[0] <= 3.667)].shape
    len2 = dfa[(3.667 < dfa[0]) & (dfa[0] <= 5.333)].shape
    len3 = dfa[(5.333 < dfa[0]) & (dfa[0] <= 7.0)].shape
    print(len1, len2, len3)

    temp = pd.cut(a, 3)
    print(temp)

    data_raw['FareCut'] = pd.qcut(data_raw['Fare'], 4)
    data_raw['AgeCut'] = pd.cut(data_raw['Age'].astype(int), 6)
    print(data_raw.head(3))

    '''
    6、编码
    6.1 LabelEncoder 方法
        使用 Sklearn 的 LabelEncoder 方法，对分类型变量完成编码。
    '''
    label = LabelEncoder()
    label = LabelEncoder()
    data_raw['Sex_Code'] = label.fit_transform(data_raw['Sex'])
    data_raw['Embarked_Code'] = label.fit_transform(data_raw['Embarked'])
    data_raw['Title_Code'] = label.fit_transform(data_raw['Title'])
    data_raw['AgeBin_Code'] = label.fit_transform(data_raw['AgeCut'])
    data_raw['FareBin_Code'] = label.fit_transform(data_raw['FareCut'])
    print(data_raw.head(3))

    '''
    6.2 get_dummies 方法
        Pandas 的 get_dummies 方法，也能实现对分类型变量实现哑编码，将长 DataFrame 变为宽 DataFrame。
        数据集中 Sex 分类型列取值有 2 种：female、male。
    '''
    temp = pd.get_dummies(data_raw['Sex'])
    print(temp)
    data1_dummy = pd.get_dummies(data_raw[['Sex', 'Embarked', 'Title', 'AgeCut', 'FareCut']])
    print("结果集：", data1_dummy)

    data_raw.info()
    print('-' * 10)
    data1_dummy.info()


if __name__ == '__main__':
    readFile()
    pass
