# _*_ coding: utf-8 _*_
# """
#  @Time : 2020/7/22 13:11
#  @Author : yls
#  @Version：V 0.1
#  @File : l_file_operation.py
#  @desc : Python 文件 IO 操作：
#             涉及文件读写操作
#             获取文件后缀名
#             批量修改后缀名
#             获取文件修改时间
#             压缩文件
#             加密文件等常用操作
#  """
import os
import re
from collections import defaultdict
import argparse
from datetime import datetime
import zipfile
import hashlib


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
    file_name = "./data/py/yls_work_count.py"
    file_ext = os.path.split(file_name)
    ipath, ifile = file_ext
    file_extension = os.path.splitext(file_name)
    print("'%s'文件路径：%s" % (file_name, ipath))
    print("'%s'文件名：%s " % (file_name, ifile))
    print("'%s'后缀名：%s " % (file_name, file_extension))


def get_parser():
    """
    定义脚本参数：
    """
    parser = argparse.ArgumentParser(description="工作目录中后缀名修改")
    parser.add_argument("work_dir", metavar='WORK_DIR', type=str, nargs=1, help='修改后缀名的文件目录')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='原来的后缀')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='新的后缀')
    return parser


def batch_rename(work_dir, old_ext, new_ext):
    """
    后缀名批量修改，实现思路：
        1、遍历目录下的所有文件。
        2、拿到此文件的后缀名。
        3、如果后缀名命中为 old_ext，rename 重命名。
    Args:
        work_dir: 传递当前目录。
        old_ext: 原来的后缀名。
        new_ext: 新的后缀名。

    """
    for filename in os.listdir(work_dir):

        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # 定位后缀名为old_ext的文件
        if old_ext == file_ext:
            # 修改后文件的完整名称
            newfile = split_file[0] + new_ext
            # 实现重命名操作
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )

    print("完成重命名")
    print(os.listdir(work_dir))


def main_batch_rename():
    """
    命令行运行的时候
    """
    # 命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())
    # 从命令行参数中依次解析出参数
    work_dir = args['work_dir'][0]

    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = '.' + old_ext

    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir, old_ext, new_ext)


def xls_to_xlsx(work_dir):
    """
    仅对 XLS 文件后缀修改。
    Args:
        work_dir: 工作的目录
    """
    old_ext, new_ext = '.xls', '.xlsx'
    for filename in os.listdir(work_dir):
        # 获取得到文件后缀
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]

        # 定位后缀名为 old_ext 的文件
        if old_ext == file_ext:
            # 修改后文件的完整名称
            newfile = split_file[0] + new_ext
            # 实现重命名操作
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print('完成重命名')
    print(os.listdir(work_dir))


def get_file_modify_time(indir):
    """
    获取文件最后一次修改的时间
    Args:
        indir: 扫描的目录
    """
    print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    # 循环目录和子目录
    for root, _, files in os.walk(indir):
        for file in files:
            whole_file_name = os.path.join(root, file)
            # 1581164725.991523，这种时间格式太不人性化
            file_modify_time = os.path.getmtime(whole_file_name)
            # 转化为人性化的时间显示格式：2020-02-08 20:25:25.991523
            nice_show_time = datetime.fromtimestamp(file_modify_time)
            print("文件: %s =》最后一次修改的时间为：%s " % (file, nice_show_time))


def file_batch_zip(start_dir):
    """
    压缩整个文件夹以及下面的文件
    Args:
        start_dir: 待压缩的文件夹

    Returns:

    """
    # 要压缩的文件夹路径
    start_dir = start_dir
    # 压缩后的文件夹名称
    file_news = start_dir + '.zip'

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        f_path = dir_path.replace(start_dir, '')
        # 实现当前文件夹以及包含的所有文件压缩
        f_path = f_path and f_path + os.sep
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)

    z.close()
    return file_news


def file_hash_cry32(s):
    """
    对字符串s实现32位加密
    Args:
        s: 需要加密的字符串

    Returns:
        返回加密后的字符串
    """
    m = hashlib.md5()
    m.update(str(s).encode('utf-8'))
    return m.hexdigest()


def file_starLineCnt(statfile,encoding='utf-8'):
    """
    统计文件的行数
    Args:
        statfile: 文件

    Returns:
        返回文件的总行数
    """
    print("文件名：" + statfile)
    cnt = 0
    with open(statfile, encoding=encoding) as f:
        while f.readline():
            cnt += 1
        return cnt


def file_diff(more, cnt, less):
    """
    统计文件不同之处的子函数
    Args:
        more: 更多行数的文件
        cnt: 总数
        less: 较少行数的文件

    Returns:

    """
    difflist = []
    with open(less, encoding='utf-8') as l:
        with open(more, encoding='utf-8') as m:
            lines = l.readlines()
            for i, line in enumerate(lines):
                if line.strip() != m.readline().strip():
                    difflist.append(i)
    if cnt - i > 1:
        difflist.extend(range(i + 1, cnt))
    return [no + 1 for no in difflist]


def file_diff_line_nos(fileA, fileB):
    """
    比较两个文件不同之处
    Args:
        fileA: 文件A
        fileB: 文件B

    Returns:
        返回的结果行号从 1 开始
        list 表示 fileA 和 fileB 不同的行的编号
    """
    try:
        cntA = file_starLineCnt(fileA)
        cntB = file_starLineCnt(fileB)
        if cntA > cntB:
            return file_diff(fileA, cntA, fileB)
        return file_diff(fileB, cntB, fileA)

    except Exception as e:
        print(e)


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

    # 获取文件的路径、文件名、后缀名
    # get_file_name()

    # 批量重命名
    # batch_rename('file','.csv','.txt')
    # xls_to_xlsx('file')

    # 获取文件修改的时间
    # get_file_modify_time('file')

    # 压缩文件
    # file_batch_zip('file/notZip')

    # 文件32位加密
    # print(file_hash_cry32(1))  # c4ca4238a0b923820dcc509a6f75849b
    # print(file_hash_cry32('hello'))  # 5d41402abc4b2a76b9719d911017c592

    # 统计文件函数
    print(file_starLineCnt('C:\\Users\\26896\\Desktop\\淘宝\\xml\\yls_work_count','gbk'))

    # 统计文件不同之处
    # diff = file_diff_line_nos("file\\a.txt", "file\\b.txt")
    # print(diff)
    pass
