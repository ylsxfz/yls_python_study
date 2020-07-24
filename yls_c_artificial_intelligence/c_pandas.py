# _*_ coding: utf-8 _*_
"""
 @Time : 2020/7/24 12:28 
 @Author : yls 
 @Version：V 0.1
 @File : c_pandas.py
 @desc : Pandas 是 Python 中，功能强大的数据分析库。提供关于数据分析高级的数据结构，各种各样的分析工具，确保整个数据处理的过程更加容易。详情参考：
            https://pandas.pydata.org/
        Pandas 两大数据结构：
            1、一维 Series
            2、二维 DataFrame
 """
import pandas as pd

def pandas_base():
    s1 = pd.Series([3,5,7])
    print("创建Series：")
    print(s1)
    print("**********************************")

    s2 = pd.Series([3,5,7],index=list('ABC'),name="s3")
    print("指定index、name：")
    print(s2)
    print("**********************************")

    df = pd.DataFrame([[9,0,1],[7,3,10]],index=['a','b'],columns=['A','B','C'])
    print("通过嵌套列表，创建DataFrame:")
    print(df)
    print("**********************************")

    df = pd.DataFrame({'A':[9,7],'B':[0,3],'C':[1,10]},index=['a','b'])
    print("通过字典，创建DataFrame：")
    print(df)
    print("**********************************")



if __name__ == '__main__':
    pandas_base()
    pass
