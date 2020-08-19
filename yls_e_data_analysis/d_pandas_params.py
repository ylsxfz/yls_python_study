# _*_ coding: utf-8 _*_
"""
 #  @Time : 2020/8/19 14:17 
 #  @Author : yls 
 #  @Version：V 0.1
 #  @File : d_pandas_params.py
 #  @desc : 基于 Python 和 NumPy 开发的 Pandas，在数据分析领域，应用非常广泛。而使用 Pandas 处理数据的第一步往往就是读入数据，
            比如读写 CSV 文件，Pandas 提供了强劲的读取支持，参数有 38 个之多。这些参数中，有的容易被忽略，但却在实际工作中用处很大。比如：
                1、文件读取时设置某些列为时间类型
                2、导入文件，含有重复列
                3、过滤某些列
                4、每次迭代读取 10 行
            挑选其中 30 个常用参数，分为 6 大类详细讨论数据读取那些事。以下讲解使用的 Pandas 版本为：0.25.1。

            1、filepathorbuffer：数据输入路径，可以是文件路径，
                也可以是 URL，或者实现 read 方法的任意对象。

            2、sep：数据文件的分隔符，默认为逗号。
                注意：如果分割字符长度大于 1，且不是 \s+，启动 Python 引擎解析。

            3、delimiter：分隔符的另一个名字，与 sep 功能相似。

            4、delim_whitespace：0.18 版本后新加参数，默认为 False，设置为 True 时，
                表示分割符为空白字符，可以是一个空格、两个空格，或 \t 等。

            5、header：设置导入 DataFrame 的列名称，默认为 'infer'，注意它与 names 参数的微妙关系。

            6、names：没被赋值时，header 会被 infer 为 0，即选取数据文件的第一行作为列名。
                    当 names 被赋值，header 没被赋值时会被 infer 为 None。
                    如果都赋值，就会实现两个参数的组合功能

            7、index_col：index_col 参数表示使用哪个或哪些列作为 index，这个参数也是非常实用的

            8、usecols：usecols 参数用于选取数据文件的哪些列到 DataFrame 中。

            9、mangle_dupe_cols：实际生产用的数据会很复杂，有时导入的数据会含有重名的列。
                    参数 mangle_dupe_cols 默认为 True，重名的列导入后面多一个 .1
                    如果设置为 False，会抛出不支持的异常：
                    ValueError: Setting mangle_dupe_cols=False is not supported yet

            10、prefix：prefix 参数，当导入的数据没有 header 时，设置此参数会自动加一个前缀

            11、dtype：dtype 查看每一列的数据类型

            12、engine：engine 参数，Pandas 目前的解析引擎提供两种：C、Python，默认为 C，因为 C 引擎解析速度更快，
                    但是特性没有 Python 引擎高。如果使用 C 引擎没有的特性时，会自动退化为 Python 引擎。

            13、converters：converters 实现对列数据的变化操作，

            14、true_values：true_values 参数指定数据中哪些字符应该被清洗为 True，
                            false_values 参数指定哪些字符被清洗为 False。

            15、skip_rows：skip_rows 过滤行。

            16、skip_footer：skip_footer 从文件末尾过滤行，解析器退化为 Python。

            17、nrows：nrows 参数设置一次性读入的文件行数，它在读入大文件时很有用，
                     比如 16G 内存的PC无法容纳几百 G 的大文件。

            18、na_values：na_values 参数可以配置哪些值需要处理成 Na/NaN，
                    类型为字典，键指明哪一列，值为看做 Na/NaN 的字符。

            19、skip_blank_lines： 默认为 True，则过滤掉空行，
                    如为 False 则解析为 NaN

            20、verbose：打印一些重要信息。

            21、parse_dates：如果导入的某些列为时间类型，但是导入时没有为此参数赋值，导入后就不是时间类型，
                            date 列此时类型为 object，想办法转化为时间型：

            22、date_parser：定制某种时间类型。

            23、infer_datetime_format：infer_datetime_format 参数默认为 False。
                    如果设定为 True 并且 parse_dates 可用，那么 Pandas 将尝试转换为日期类型，
                    如果可以转换，转换方法并解析，在某些情况下会快 5~10 倍。

            24、iterator：iterator 取值 boolean，default False，返回一个 TextFileReader 对象，以便逐块处理文件。

            25、chunksize：chunksize 整型，默认为 None，设置文件块的大小。

            26、compression：
                    1、compression 参数取值为 {‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}，
                        默认 ‘infer’，直接使用磁盘上的压缩文件。
                    2、如果使用 infer 参数，则使用 gzip、bz2、zip 或者解压文件名中以 ‘.gz’、‘.bz2’、‘.zip’ 或 ‘xz’ 这些为后缀的文件，否则不解压。
                    3、如果使用 zip，那么 ZIP 包中必须只包含一个文件。设置为 None 则不解压

            27、thousands：str，default None，千分位分割符，如 , 或者 .。

            28、encoding：定字符集类型，通常指定为 'utf-8'。List of Python standard encodings。

            29、error_bad_lines：如果一行包含过多的列，那么默认不会返回 DataFrame，如果设置成 False，那么会将该行剔除（只能在C解析器下使用）。

            30、warn_bad_lines：如果 error_bad_lines 设置为 False，并且 warn_bad_lines 设置为 True，那么所有的“bad lines”将会被输出（只能在 C 解析器下使用）。
 """
import pandas as pd
import numpy as np


def pandas_param_base():
    print("读取文件：")
    data = pd.read_csv('file/iris.data')
    print(data)

    d = {'id': [1, 2], 'name': ['gz', 'lh'], 'age': [10, 12], 'id': [7, 8], }
    df = pd.DataFrame(d)
    df.to_csv('file/test.csv', sep='\t')

    print()
    print("默认是逗号分割：")
    df = pd.read_csv('file/test.csv')
    print(df)
    print()

    print("指定为\\t分割：")
    df = pd.read_csv('file/test.csv', sep='\t')
    print(df)
    print()

    df = pd.DataFrame(d)
    df.to_csv('file/test.csv', sep=' ')
    df = pd.read_csv('file/test.csv', delim_whitespace=True)
    print(df)


def pandas_params_name():
    """
    1、name没有被赋值，header也没有赋值：
    """
    print("1、name没有被赋值，header也没有赋值：")
    df = pd.read_csv('file/test.csv', delim_whitespace=True)
    print(df)
    print()

    """
    2、name没有被赋值，header被赋值：
    """
    print("2、name没有被赋值，header被赋值：")
    df = pd.read_csv('file/test.csv', delim_whitespace=True,
                     header=1)
    print(df)
    print()

    """
    3、name被赋值，header没有赋值：
    """
    print("3、name被赋值，header没有赋值：")
    df = pd.read_csv('file/test.csv', delim_whitespace=True,
                     names=['id', 'name', 'age'])
    print(df)
    print()

    """
    4、name被赋值，header也被赋值：
    """
    print("4、name被赋值，header没有赋值：")
    df = pd.read_csv('file/test.csv', delim_whitespace=True,
                     header=0, names=['id', 'name', 'age'])
    print(df)
    print()


def pandas_params_col():
    print("index_col：")
    df = pd.read_csv('file/test.csv', delim_whitespace=True,
                     index_col=1)
    print(df)
    print()

    print("usecols：")
    df = pd.read_csv('file/test.csv', delim_whitespace=True,
                     usecols=['id', 'name'])
    print(df)
    print()

    print("mangle_dupe_cols：")
    # Setting mangle_dupe_cols=False is not supported yet
    df = pd.read_csv('file/test01.csv', delim_whitespace=True,
                     mangle_dupe_cols=True)
    print(df)
    print()

    print("prefix：")
    df = pd.read_csv('file/test.csv', sep=' ',
                     prefix='col', header=None)
    print(df)
    print()


def pandas_params_common():
    print("dtypes：")
    df = pd.read_csv('file/test.csv', sep='\s+')
    print(df.dtypes)
    print()

    df = pd.read_csv('file/test.csv', sep='\s+', dtype={'age': float})
    print(df)
    print(df.dtypes)
    print()

    print("dtypes：完成对 age 列的数据加 1，"
          "注意 int(x)，此处解析器默认所有列的类型为 str，所以需要显示类型转换。")
    df = pd.read_csv('file/test.csv', sep='\s+')
    print(df)
    df = pd.read_csv('file/test.csv', sep='\s+',
                     converters={'age': lambda x: 1 + int(x)})
    print(df)
    print()

    print("true_values：")
    d = {'id': [1, 2], 'name': ['gz', 'lh'], 'age': [10, 12], 'label': ['YES', 'NO']}
    df = pd.DataFrame(d)
    df.to_csv('file/test_label.csv', index=False)
    df = pd.read_csv('file/test_label.csv')
    print(df)
    print()
    df = pd.read_csv('file/test_label.csv',
                     true_values=['YES'], false_values=['NO'])
    print(df)
    print()

    print('skip_rows：')
    df = pd.read_csv('file/test.csv', sep='\s+')
    print("源数据：")
    print(df)
    print("过滤掉 index 为 0 的行：")
    df = pd.read_csv('file/test.csv', sep='\s+', skiprows=[0])
    print(df)
    print("过滤掉 index 为 0 的行，同时header=None：")
    df = pd.read_csv('file/test.csv', sep='\s+',
                     header=None, skiprows=[0])
    print(df)
    print()

    df = pd.read_csv('file/iris.data', sep=',', nrows=2)
    print(df)


def pandas_params_null():
    d = {'id': [1, 2, ''], 'name': ['gz', 'lh', ''], 'age': [10, 12, ''], 'date': ['2020-03-10', '#', '']}
    df = pd.DataFrame(d)
    df.to_csv('file/test_date.csv', sep=' ', index=False)
    df = pd.read_csv('file/test_date.csv', sep='\s+')
    print(df)
    print("na_values：")
    df = pd.read_csv('file/test_date.csv', sep='\s+',
                     na_values=['#'])
    print(df)
    print()

    print("skip_blank_lines：")
    df = pd.read_csv('file/test_date.csv', sep='\s+',
                     skip_blank_lines=False)
    print(df)
    print()

    print('verbose：')
    df = pd.read_csv('file/test_date.csv', sep='\s+',
                     header=0, verbose=True)
    print(df)


def pandas_param_date():
    print("parse_dates：")
    df = pd.read_csv('file/test_date.csv', sep='\s+', header=0,
                     na_values=['#'])
    print(df)
    print(df.dtypes)
    print()

    df = pd.read_csv('file/test_date.csv', sep='\s+', header=0,
                     na_values=['#'], parse_dates=['date'])
    print(df)
    print(df.dtypes)
    print()

    print('date_parser：')
    d = {'id': [1, 2], 'name': ['gz', 'lh'], 'age': [10, 12], 'date': ['2020-3-10', '2020-3-12']}
    df = pd.DataFrame(d)
    df.to_csv('file/test_date2.csv', sep=' ', index=False)
    df = pd.read_csv('file/test_date2.csv', sep='\s+')
    print(df)
    print("转换为标准时间：")
    df = pd.read_csv('file/test_date2.csv', sep='\s+', parse_dates=['date'],
                     date_parser=lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d'))
    print(df)


def pandas_param_file_iterator():
    print("iterator：")
    df = pd.read_csv('file/iris.data', sep='\s+', iterator=True)
    print(df.get_chunk(1))
    print("再获取：")
    print(df.get_chunk(1))
    print()

    print("iterator：")
    df = pd.read_csv('file/iris.data', sep='\s+', chunksize=2)
    print(df.get_chunk())
    print("再获取：")
    print(df.get_chunk())


def pandas_param_zip():
    print("compression：")
    df = pd.read_csv('file/test.zip', sep='\s+', compression='zip')
    print(df)
    print()

    print("不使用thousands：")
    df = pd.read_csv('file/test_thousands.csv', sep='\s+')
    print(df)
    print("使用thousands：")
    df = pd.read_csv('file/test_thousands.csv', sep='\s+',
                     thousands=',')
    print(df)
    print()

    print("error_bad_lines：")
    df = pd.read_csv('file/test_err_bad_line.csv', sep=',', error_bad_lines=False)
    print(df)
    print()

    print("warn_bad_lines：")
    df = pd.read_csv('file/test_err_bad_line.csv', sep=',',
                     error_bad_lines=False, warn_bad_lines=True)
    print(df)
    print()


def pandas_example():
    """
    如下所示，读取某 100G 大小的 big_data.csv 数据：
        1、使用 skiprows 参数；
        2、x>0 确保首行读入；
        3、np.random.rand()>0.01 表示 99% 的数据都会被随机过滤掉。
    """
    df = pd.read_csv("file/iris.data",
                     skiprows=lambda x: x > 0 and np.random.rand() > 0.01)
    print("The shape of the df is {}."
          "It has been reduced 100 times!".format(df.shape))


if __name__ == '__main__':
    # pandas的基本参数
    # pandas_param_base()

    # pandas的name和header参数
    # pandas_params_name()

    # pandas的col相关参数
    # pandas_params_col()

    # pandas的通用解析参数
    # pandas_params_common()

    # 空值处理相关参数
    # pandas_params_null()

    # 时间相关参数
    # pandas_param_date()

    # 分块读入相关参数
    # pandas_param_file_iterator()

    # 格式和压缩相关参数
    # pandas_param_zip()

    # 案例分析
    pandas_example()
    pass
