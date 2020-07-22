# _*_ coding: utf-8 _*_
"""
 @Time : 2020/7/22 13:11 
 @Author : yls 
 @Version：V 0.1
 @File : l_file_operation.py
 @desc : Python 文件 IO 操作：
            涉及文件读写操作
            获取文件后缀名
            批量修改后缀名
            获取文件修改时间
            压缩文件
            加密文件等常用操作
 """
import os
import re
from collections import defaultdict


def read_file(filename, encoding='utf-8'):
    """
    读取文件
    Args:
        filename: 文件路径
        encoding: 文件编码

    Returns:
        文件的所有内容
    """
    if os.path.exists(filename) is False:
        raise FileNotFoundError("%s not exists" % filename)
    f = open(filename, encoding=encoding)
    text = f.read()
    f.close()
    return text


def read_file_by_with(filename, encoding='utf-8'):
    """
    读取文件
    Args:
        filename: 文件路径
        encoding: 文件编码

    Returns:
        文件的所有内容
    """
    if os.path.exists(filename) is False:
        raise FileNotFoundError("%s not exists" % filename)
    with open(filename, encoding=encoding) as f:
        text = f.read()
    return text


def read_file_by_line(filename, encoding='utf-8'):
    """
    如下，读取文件 a.txt，r+ 表示读写模式。代码块实现：
        1、每次读入一行。
        2、选择正则 split 分词，注意观察 a.txt，单词间有的一个空格，有的多个。这些情况，实际工作中确实也会遇到。
        3、使用 defaultdict 统计单词出现频次。
        4、按照频次从大到小降序。
    Args:
        filename: 文件路径
        encoding: 文件编码

    Returns:
        按行读取文件
    """
    rec = re.compile('\s+')
    dd = defaultdict(int)
    with open(filename, 'r+') as f:
        for line in f:
            clean_line = line.strip()
            if clean_line:
                words = rec.split(clean_line)
                for word in words:
                    dd[word] += 1
    dd = sorted(dd.items(), key=lambda x: x[1], reverse=True)
    print('---print start---')
    print(dd)
    print('---print end---')


def write_to_file(file_path, file_name):
    """
    这段代码思路：
        1、路径不存在，创建路径
        2、写文件
        3、读取同一文件
        4、验证写入到文件的内容是否正确
    Args:
        file_path: 文件路径
        file_name: 文件名称

    """
    if os.path.exists(file_path) is False:
        os.mkdir(file_path)
    whole_path_filename = os.path.join(file_path, file_name)
    to_write_content = ''' 
                            Hey, Python
                            I just love Python so much,
                            and want to get the whole python stack by this 60-days column
                            and believe!
                            '''
    with open(whole_path_filename, mode='w', encoding='utf-8') as f:
        f.write(to_write_content)
    print('------write done---------')

    print('------bejin reding-------')
    with open(whole_path_filename, encoding='utf-8') as f:
        text = f.read()
        print(text)
        if to_write_content == text:
            print('content is equal by reading and writing')
        else:
            print('------waring: No Equal-----------')


def get_file_name():
    """
    获取文件路径、文件名称、文件的后缀名
    """
    file_name = "./data/py/test.py"
    file_ext = os.path.split(file_name)
    ipath, ifile = file_ext
    file_extension = os.path.splitext(file_name)
    print("'%s'文件路径：%s" % (file_name,ipath))
    print("'%s'文件名：%s " % (file_name,ifile))
    print("'%s'后缀名：%s " % (file_name, file_extension))


if __name__ == '__main__':
    # read_file("file\\a.txt")
    # read_file("pyechart\\echarts.min.js")

    # content = read_file("pyechart\\echarts.min.js",encoding='utf-8')
    # print(content)

    # content = read_file_by_with("pyechart\\echarts.min.js", encoding='utf-8')
    # print(content)

    # 按行读取文件
    # read_file_by_line('file\\a.txt')

    # 写文件
    # write_to_file('file\\', 'b.txt')

    get_file_name()
    pass
