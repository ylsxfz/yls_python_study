# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/10/25 14:13 
#  @Author: yls
#  @Version: V 0.1
#  @File: e_pandas_iterrows_itertuples.py
#  @Desc: Pandas 两个核心数据结构 iterrows 和 itertuples 比较，特有的 set_index、reset_index、reindex 操作
"""
import pandas as pd
import numpy as np

"""
一维数组 Series:
    1、Series 是 Pandas 两大数据结构中（DataFrame、Series）的一种，先从 Series 的定义说起。
        Series 是一种类似于一维数组的对象，它由一组数据域以及一组与之相关联的数据标签和索引组成。
    2、Series 对象也是一个 NumPy 的数组，因此 NumPy 的数组处理函数可以直接对 Series 进行处理。
    3、与此同时，Series 除了可以使用位置索引作为下标存取元素之外，还可以使用“标签下标”存取元素，
    这一点和字典相似，每个 Series 对象都由两个数组组成：
        . index：它是从 NumPy 数组继承的 Index 对象，保存标签信息。
        . values：保存值的 NumPy 数组。
    
    4、构造函数： Series 的标准构造函数，列举常用的几个参数：
        Series(data=None, index=None, dtype=None, name=None)
        . data：数据部分
        . index：标签部分，默认为自增整数索引
        . dtype：str、numpy.dtype 或者 ExtensionDtype

二维数组 DataFrame：
    1、DataFrame，Pandas 两个重要数据结构中的另一个，可以看做是 Series 的容器。
    2、DataFrame 同时具有行、列标签，是二维的数组，行方向轴 axis 为 0，列方向 axis 为 1，如下：
        . axis : {0 or 'index', 1 or 'columns'}
    3、构造函数：DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
"""


def series_study():
    """
    注意：
        1、不管是append（添加），还是drop操作，都发生在原始数据的副本上，不是原始数据
        2、通过标签修改数据的时候，标签相同的数据都会被修改成对应的数据
    """
    print("\n***************************初始化************************************")
    ps = pd.Series(data=[-3, 2, 1], index=['a', 'f', 'b'], dtype=np.float32)
    print("原始数据 ps = \n", ps)

    print("\n***************************增加元素************************************")
    print("ps 增加元素后 psn = ")
    # Pandas 是允许重复的元素
    psn = ps.append(pd.Series(data=[-8.0], index=['f']))
    print(psn)
    print()
    print("psn['f'] = \n", psn['f'])

    print("\n***************************删除元素************************************")
    psd = ps.drop('f')
    print("psd = \n", psd)

    print("\n***************************修改元素************************************")
    psn['f'] = 10.0
    print("psn= \n", psn)

    print("\n***************************访问元素************************************")
    print("通过索引访问：ps[2] = %f" % ps[2])
    print("通过标签访问：ps['b'] = %f " % ps['b'])

    print("\n***************************原始数据************************************")
    print(ps)


def dataFrame_study():
    df = pd.DataFrame([['gz', 4.0, '2019-01-01'], ['lg', 1.2, '2019-06-01']], index=['a', 'f'],
                      columns=['nm', 'y', 'da'])
    print("\n***************************原始数据************************************")
    print("df =")
    print(df)

    df2 = pd.DataFrame({'nm': ['gz', 'lg'], 'y': [4.0, 1.2], 'da': ['2019-01-01', '2019-06-01']}, index=['a', 'f'])
    print("\ndf2 =")
    print(df2)

    print("\n***************************增加数据************************************")
    dfn = df.append(pd.Series(data=['zx', 3.6, '2020-09-08'], index=['nm', 'y', 'da'], name='b'))
    print("dfn = ")
    print(dfn)

    print("\n***************************删除数据--行************************************")
    df_drop_row = dfn.drop('b')
    print(df_drop_row)

    print("\n***************************删除数据--列************************************")
    df_drop_column = dfn.drop('da', axis=1)
    print(df_drop_column)

    print("\n***************************修改数据************************************")
    dfn.loc['b', 'da'] = '2020-11-11'
    print(dfn)

    print("\n***************************原始数据************************************")
    print("df =")
    print(df)


def chain_operation():
    """
    链式操作
    """
    df = pd.DataFrame({'a': [1, 3, 5], 'b': [4, 2, 7], 'c': [0, 3, 1]})
    print(df)

    tmp = df[df.a < 4]
    tmp['c'] = 200
    print('----原 df 没有改变----')
    print(df)

    print("\n链式操作：tmp是df的copy，而并非view")
    df.loc[df.a < 4, 'c'] = 100
    print(df)


def data_access():
    df = pd.DataFrame([['gz', 4.0, '2019-01-01'], ['lg', 1.2, '2019-06-01']], index=['a', 'f'],
                      columns=['nm', 'y', 'da'])
    print("\n***************************原始数据************************************")
    print("df =")
    print(df)

    print("\n***************************iloc************************************")
    print("\ndf.iloc[1,:] = ")
    print(df.iloc[1, :])

    print("\n***************************loc************************************")
    print("\ndf.loc['f',:] = ")
    print(df.iloc[1, :])

    print("\ndf.loc['f','nm'] = ")
    print(df.loc['f', 'nm'])

    # [] 操作符支持 list 对象，对列索引支持。对行索引不支持：
    print("\n***************************[]************************************")
    np.random.seed(1)
    df1 = pd.DataFrame(np.random.randint(1, 10, (4, 3)),
                       index=['r1', 'r2', 'r3', 'r4'],
                       columns=['c1', 'c2', 'c3'])
    print("原始数据：")
    print(df1)

    print("df1[['c1','c3']] = ")
    print(df1[['c1', 'c3']])

    # 利用行切片整数索引，获取 DataFrame，Pandas 依然延续了原生 Python 的风格
    print("行切片：df1[1:3] = ")
    print(df1[1:3])

    # Pandas 还对此做了增强，同时支持行切片标签索引获取 DataFrame，注意包括终止标签。
    print("终止标签：df1['r1','r3'] = ")
    print(df1['r1':'r3'])

    # 标量结合
    print("df1 > 4 = \n")
    print(df1 > 4)

    # 结合 Pandas 的方括号 [] 后，便能实现元素级的操作，不大于 4 的元素被赋值为 NaN：
    print("df1[df1 > 4] = \n")
    print(df1[df1 > 4])

    # df1>4 操作返回一个元素值为 True 或 False 的 DataFrame，(df1>4).values.tolist() 得到原生的 python list 对象
    inner = ((df1 > 4).values).tolist()
    print("((df1 > 4).values).tolist() = \n")
    print(inner)

    # DataFrame、[] 和 list 实例结合
    print("df1[inner]\n")
    print(df1[inner])

    # 遍历
    print("\n***************************iterrows-遍历************************************")
    print("\niterrows 遍历")
    for i, row in df1.iterrows():
        print(row)

    print("\n***************************itertuples-遍历************************************")
    print("\nitertuples 遍历")
    for nt in df1.itertuples():
        print(nt)


def index_fun():
    print("\n***************************原始数据************************************")
    df1 = pd.DataFrame({'a': [1, 3, 5], 'b': [9, 4, 12]})
    print(df1)

    print("\n***************************列转index************************************")
    df2 = df1.set_index('a', drop=False)
    print(df2)

    print("\n***************************列转index************************************")
    df3 = df1.set_index('a', drop=True)
    print(df3)

    print("\n***************************index转列************************************")
    df4 = df1.set_index('a', drop=True).reset_index('a', drop=False)
    print(df4)

    print("\n***************************index转列************************************")
    df5 = df1.set_index('a', drop=True).reset_index('a', drop=True)
    print(df5)

    # 如果想按照某种规则，按照行重新排序数据，靠 reindex 函数可以实现
    print("\n***************************reindex************************************")
    print("\nprint(df1.reindex([0, 3, 2, 1])) = ")
    print(df1.reindex([0, 3, 2, 1]))

    print("\nprint(df1.reindex(columns=['b', 'a', 'c', 'd'])) = ")
    print(df1.reindex(columns=['b', 'a', 'c', 'd']))


if __name__ == '__main__':
    # series_study()

    # dataFrame_study()

    # chain_operation()

    # data_access(

    index_fun()
    pass
