# _*_ coding: utf-8 _*_
"""
 #  @Time : 2020/11/25 13:12 
 #  @Author : yls 
 #  @Version：V 0.1
 #  @File : h_pandas_tools.py
 #  @desc : pandas 与数据读取、选取、清洗、特征工程相关的12个实用工具
 """
import pandas as pd
import numpy as np

# 设置行不限制数量,不然会中间有省略号，数据会看不到
pd.set_option('display.max_rows', None)
# 设置列不限制数量,不然会中间有省略号，数据会看不到
pd.set_option('display.max_columns', None)
# 控制台输出的列数超过100换行，不然数据表格会折回来
pd.set_option('display.width', 1000)


def read_file_random():
    """
    如下所示，读取某 100 G 大小的 big_data.csv 数据：
        1、使用 skiprows 参数
        2、x>0 确保首行读入
        3、np.random.rand()>0.01 表示 99% 的数据都会被随机过滤掉
    """
    df = pd.read_csv("test/train.csv", skiprows=lambda x: x > 0 and np.random.rand() > 0.02)
    print(df)
    print("The shape of the df is{}."
          "it has been reduced 100 items!".format(df.shape))


def make_date_index():
    """
    与时间序列相关的问题，平时挺常见。如何用 Pandas 快速生成时间序列数据？
    使用 pd.util.testing.makeTimeDataFrame 只需要一行代码，便能生成一个 index 为时间序列的 DataFrame
    """
    df = pd.util.testing.makeTimeDataFrame(10)
    print(df)

    """
    时间序列的间隔还能配置，默认的 A、B、C、D 四列也支持配置
    """
    df = pd.DataFrame(np.random.randint(1, 1000, size=(10, 3)),
                      columns=['商品编码', '商品销量', '商品库存'])
    df.index = pd.util.testing.makeDateIndex(10, freq='H')
    print(df)


def apply_type_check():
    """
    使用 apply(type) 做类型检查
    有时肉眼所见的列类型，未必就是你预期的类型，如下 DataFrame 销量这一列，看似为浮点型。
    """
    d = {'商品': ['A', 'B', 'C', 'D', 'E'],
         '销量': [100, '100', 50, 550.20, "375.25"]}
    df = pd.DataFrame(d)
    print(df)

    # 下面的代码会报错
    # sellerSum = df['销量'].sum()
    # print(sellerSum)

    # 类型检查
    sellerType = df['销量'].apply(type)
    print(sellerType)

    # 按照对应的类型运算：使用 value_counts 统计下各种值的频次。
    sellerSum = df['销量'].apply(type).value_counts()
    print(sellerSum)


def label_action_select_data():
    """
    标签和位置选择数据
    """
    df = pd.read_csv("test/drinksbycountry.csv",index_col="country")
    print(df)

if __name__ == '__main__':
    # 读取时抽样 1%
    # read_file_random()

    # 生成时间序列的数据集
    # make_date_index()

    # 使用 apply(type) 做类型检查
    # apply_type_check()

    # 标签和位置选择数据
    label_action_select_data()
    pass
