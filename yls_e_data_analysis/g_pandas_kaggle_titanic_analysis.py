# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/11/08 15:10 
#  @Author: yls 
#  @Version: V 0.1
#  @File: g_pandas_kaggle_titanic_analysis.py
#  @Desc: Pandas 实战 Kaggle titanic 数据探索性分析
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def demo_melt_pivot_table():
    """
    1、melt：透视

    2、pivot 将长 DataFrame 透视为宽 DataFrame，与 melt 函数透视方向相反。函数的主要参数说明：
        a. index 指明哪个列变为新 DataFrame 的 index；
        b. columns 指明哪些列变为 columns；
        c. values 指明哪些列变为新 DataFrame 的数据域，如果不指明，则默认除了被指明 index 和 columns 的其他列。

    3、
    """
    d = {
        "district_code": [12345, 56789, 101112, 131415],
        "apple": [5.2, 2.4, 4.2, 3.6],
        "banana": [3.5, 1.9, 4.0, 2.3],
        "orange": [8.0, 7.5, 6.4, 3.9]
    }

    df = pd.DataFrame(d)
    print(df)
    print("**********************************************************************************************")

    """
    1、合并列
    """
    dfm = df.melt(
        id_vars="district_code",
        var_name="fruit_name",
        value_name="price"
    )
    print(dfm)
    print("**********************************************************************************************")

    """
    2、pivot 将长 DataFrame 透视为宽 DataFrame，与 melt 函数透视方向相反。
    """
    dfp = dfm.pivot(index='district_code', columns='fruit_name', values='price')
    print(dfp)
    print("**********************************************************************************************")

    print(dfp.columns)
    print("**********************************************************************************************")

    d = { \
        "district_code": [12345, 12345, 56789, 101112, 131415, 12345, 12345, 56789, 101112, 131415],
        "fruit_name": ['apple', 'apple', 'orange', 'banana', 'orange', 'apple', 'apple', 'orange', 'banana', 'orange'],
        "price": [3.5, 3.7, 1.9, 4.0, 2.3, 4.5, 4.7, 2.9, 5.0, 3.3]
    }

    """
    3、pivot_table 函数，不仅具有 pivot 函数将长 DataFrame 透视为宽 DataFrame，同时还具有 sum 聚合功能
    """
    df2 = pd.DataFrame(d)
    print(df2)
    print("**********************************************************************************************")

    dfp2 = df2.pivot_table(index='district_code', columns='fruit_name', values=['price'], aggfunc=[np.sum])
    print(dfp2)
    print("**********************************************************************************************")

    dfp3 = df2.pivot_table(index='district_code', columns='fruit_name', values=['price'], aggfunc=[np.sum, np.mean])
    print(dfp3)
    print("**********************************************************************************************")


def demo_crosstab():
    """
    1、crosstab 透视频次：有 2 个必传递的参数 index、colmns，分别为透视后的行、列索引

    值得注意，这些透视函数，melt、pivot、pivot_table、crosstab，都基于 groupby 分组基础上，
    而分组大家是更容易理解的，所以在理解这些透视函数时
    """
    a = np.array(['apple', 'apple', 'orange', 'banana', 'orange'], dtype=object)
    b = np.array(['china', 'china', 'ameri', 'ameri', 'korea'], dtype=object)
    c = np.array(['good', 'good', 'good', 'good', 'better'], dtype=object)
    result = pd.crosstab(a, [b, c])
    print(result)
    print("**********************************************************************************************")

    for it in zip(a, b, c):
        print(it)
    print("**********************************************************************************************")

    result2 = pd.crosstab([a, b], [c])
    print(result2)
    print("**********************************************************************************************")

    df = pd.DataFrame({'类别': ['水果', '水果', '水果', '蔬菜', '蔬菜', '肉类', '肉类'],
                       '产地': ['美国', '中国', '中国', '中国', '新西兰', '新西兰', '美国'],
                       '水果': ['苹果', '梨', '草莓', '番茄', '黄瓜', '羊肉', '牛肉'],
                       '数量': [5, 5, 9, 3, 2, 10, 8],
                       '价格': [5, 5, 10, 3, 3, 13, 20]})
    print(df)
    print("**********************************************************************************************")

    # “类别”列设置为 index，“产地”列设置为 columns，统计词条出现频次
    result3 = pd.crosstab(df['类别'], df['产地'], margins=True)
    print(result3)
    print("**********************************************************************************************")

    # crosstab 本质：按照指定的 index 和 columns 统计 DataFrame 中出现 index、columns 的频次。
    result4 = pd.crosstab(df['类别'], df['产地'], values=df['价格'], aggfunc=np.max, margins=True)
    print(result4)
    print("**********************************************************************************************")


def demo_eda():
    data_eda = pd.read_csv("test/titanic_eda_data.csv")
    print(data_eda)
    print("**********************************************************************************************")

    print(data_eda.dtypes)
    print("**********************************************************************************************")
    eda_cols = ['Survived', 'Pclass', 'Sex', 'AgeBin', 'IsAlone', 'Title', 'Embarked']
    for x in eda_cols[1:]:
        print(x)
        pivot_x = data_eda.pivot_table(index=data_eda.index,
                                       columns=[x], values=['Survived']).agg(['count', 'mean'])
        print(pivot_x)
        print('*' * 100)

    plt.figure(figsize=[8, 4])
    for i, x in enumerate(eda_cols[1:]):
        gx = data_eda[[x, 'Survived']].groupby(x, as_index=False).mean()
        plt.subplot(int('23' + str(i + 1)))
        sns.barplot(x=gx[x], y=gx['Survived'])
        plt.title(x + ' Survived')
        plt.xlabel(x)
        plt.ylabel('Survived')
    plt.show()

    for x in eda_cols[1:]:
        print(x)
        pivot_x = data_eda.pivot_table(index=data_eda.index, columns=[x], values=['Survived']).agg(['mean'])
        print(pivot_x.iloc[0, :].std())

    stds = []
    for x in eda_cols[1:]:
        print(x)
        pivot_x = data_eda.pivot_table(index=data_eda.index, columns=[x], values=['Survived']).agg(['mean'])
        stds.append((x, pivot_x.iloc[0, :].std()))
    sns.barplot(x=[e[0] for e in stds], y=[e[1] for e in stds])
    plt.title('std of mean survived')
    plt.show()
    print("**********************************************************************************************")

    feature_pair = [(e1, e2) for i, e1 in enumerate(eda_cols[1:]) for e2 in eda_cols[i + 1:] if e1 != e2]
    print(feature_pair)
    print("**********************************************************************************************")

    plt.figure(figsize=[8, 6])
    i = 0
    for e1, e2 in feature_pair[:9]:
        pair = data_eda[[e1, e2, 'Survived']].groupby([e1, e2], as_index=False).mean()
        plt.subplot(int('33' + str(i + 1)))
        sns.barplot(x='(' + pair[e1].astype('str') + ',' + pair[e2].astype('str') + ')', y=pair['Survived'],
                    palette="rocket")
        plt.title('(%s,%s) mean of Survived ' % (e1, e2))
        plt.ylabel('Survived')
        plt.xticks([])
        i += 1
    plt.show()
    print("**********************************************************************************************")

    sex_title_count = data_eda[['Sex', 'Title', 'Survived']].groupby(
        ['Sex', 'Title'], as_index=False).agg(['count'])
    print(sex_title_count)
    print("**********************************************************************************************")

    sex_title_count = data_eda[['Pclass', 'Title', 'Survived']].groupby(
        ['Pclass', 'Title'], as_index=False).agg(['count'])
    print(sex_title_count)
    print("**********************************************************************************************")

    # plt.figure(figsize=[8, 6])
    # for e1, e2 in feature_pair:
    #     pair = data_eda[[e1, e2, 'Survived']].groupby([e1, e2], as_index=False).mean()
    #     sns.catplot(x=e1, y="Survived", hue=e2, data=pair,
    #                 kind="bar", palette="muted")
    #     plt.ylabel('Survived')
    # plt.show()
    # print("**********************************************************************************************")

    # plt.figure(figsize=[8, 6])
    g = sns.PairGrid(data_eda, hue="Survived")
    g.map_diag(plt.hist)
    g.map_offdiag(plt.scatter)
    g.add_legend()
    plt.show()


if __name__ == '__main__':
    # demo_melt_pivot_table()
    # demo_crosstab()
    demo_eda()
    pass
