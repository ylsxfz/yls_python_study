# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         XmlToCsl
# Description:  解析xml程序
# Author:       yls
# Date:         2020/3/18
# -------------------------------------------------------------------------------
import xml.etree.ElementTree as xmlTree
import uuid
import os
import shutil
import time

# # 源文件路径
# source_folder = "sf\\"
# # 处理后的文件路径
# target_folder = "target\\"
# # 备份目录
# source_bak_folder = "bak\\"
# # 日志目录
# log_folder = "log\\"


# 源文件路径
source_folder = "/home/datafile/ORDERLIST/bak_20200701_20200728/source"
# 处理后的文件路径
target_folder = "/home/datafile/ORDERLIST/bak_20200701_20200728/target"
# 备份目录
source_bak_folder = "/home/datafile/ORDERLIST/bak_20200701_20200728/bak"
# 日志目录
log_folder = "/home/datafile/ORDERLIST/bak_20200701_20200728/log"

fileName = ""
# # 统计总量
# totalCoun = 0
# # 统计成功处理的文件数
# totalSuccessCount = 0
# # 本次扫描的文件量
# thisTimeCou = 0
# # 本次成功处理的文件量
# thisTimeSucCount = 0
#
# # 数据长度
data_len = 42
# # 数据长度正常的统计
# len_succer_count = 0
# # 数据长度不对的数据
# len_error_big_count = 0
# len_error_small_count = 0


data_count_dict = {'totalCoun': 0, 'totalSuccessCount': 0, 'thisTimeCou': 0, 'thisTimeSucCount': 0,
                   'len_succer_count': 0, 'len_error_big_count': 0, 'len_error_small_count': 0}

# 格式化时间字符串
seconds = time.time()
local_time = time.localtime(seconds)
format_time = time.strftime("%Y-%m-%d", local_time)


def dirlistOneLevel(path, allfile):
    """
    只扫描一级目录
    Args:
        path: 路径
        allfile: 文件集合

    Returns:

    """
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            allfile.append(filepath)
    return allfile


def count_init():
    global data_count_dict
    data_count_dict['thisTimeCou'] = 0
    data_count_dict['thisTimeSucCount'] = 0
    data_count_dict['len_succer_count'] = 0
    data_count_dict['len_error_big_count'] = 0
    data_count_dict['len_error_small_count'] = 0


def total_log():
    """
    统计文件数量
    """
    return "%d,%d,%d,%d" % (data_count_dict['totalCoun'], data_count_dict['totalSuccessCount'],
                            data_count_dict['thisTimeCou'], data_count_dict['thisTimeSucCount'])


def file_log(filename):
    """
    统计文件的每行的字段长度
    Args:
        filename: 文件名称
    """
    return "%s,%d,%d,%d" % (filename, data_count_dict['len_succer_count'],
                            data_count_dict['len_error_big_count'], data_count_dict['len_error_small_count'])


def write_log(content):
    try:
        fout = open(log_folder + "/" + format_time + ".csv", 'a', encoding='utf-8', errors='ignore')
        if not content.endswith("\n"):
            content = content + "\n"
        fout.write(content)
    except Exception as e:
        print(e)
    finally:
        fout.close()


def dirlist(path, allfile):
    """
    扫描文件
    Args:
        path: 文件的路径
        allfile: 待返回的数据。建议传入 []

    Returns:
        文件集合
    """
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            print("scan:" + filepath)
            dirlist(filepath, allfile)
        else:
            if len(allfile) > 50000:
                break
            allfile.append(filepath)
    return allfile


def jwkj_get_filePath_fileName_fileExt(filename):
    """
    获取文件的路径（），文件名（不带后缀），文件类型（后缀）
    Args:
        filename: 文件名

    Returns:

    """
    [filepath, tempfilename] = os.path.split(filename);
    [shotname, extension] = os.path.splitext(tempfilename);
    return filepath, shotname, extension


def redxml(source_file, file_name):
    """
    解析xml
    Args:
        source_file: 源文件
        target_folder: 目标文件夹
        file_name: 文件前缀名称
    """
    with open(source_file, encoding='gbk', errors='ignore') as fp:
        text = fp.read()
    tree_text = xmlTree.fromstring(text.encode('utf-8'))
    buf = []
    for item in tree_text.find("ordersElement").findall("requestOrder"):
        line = ""
        is_write = True
        # if "," not in str(item.find("remark").text):
        #     continue
        is_need_write, line = item_iterator(item, line, is_write)
        if '\n' not in line:
            line = line + '\n'
        # if is_need_write:
        buf.append(line)
        # 统计字段长度
        line_count(line)
    filepath, shotname, extension = jwkj_get_filePath_fileName_fileExt(source_file)

    if len(buf) > 0:
        try:
            fout = open(target_folder + "/" + file_name + str(shotname) + "_" + str(uuid.uuid1()) + ".csv", 'a',
                        encoding='utf-8', errors='ignore')
            fout.writelines(buf)
        except Exception as e:
            print(e)
        finally:
            fout.close()

    try:

        # 记录统计数据
        data_count('thisTimeSucCount', 1)
        data_count('totalSuccessCount', 1)
        # 文件备份
        move_file = source_file.replace(source_folder, source_bak_folder)
        # 解析文件路径、文件名称、文件后缀
        bak_path, bak_name, bak_ext = jwkj_get_filePath_fileName_fileExt(move_file)
        if not os.path.exists(bak_path):
            os.makedirs(bak_path)
        shutil.move(source_file, move_file)
    except Exception as e:
        print(e)


def line_count(line):
    """
    统计字段长度
    Args:
        line: 行
    """
    line_arr = line.split(',')
    line_len = len(line_arr)
    if line_len == data_len:
        data_count('len_succer_count', 1)
    elif line_len > data_len:
        data_count('len_error_big_count', 1)
    else:
        data_count('len_error_small_count', 1)


def data_count(count_field, num):
    """
    修改统计数据
    Args:
        count_field: 统计的字段
        num: 修改的值

    Returns:

    """
    global data_count_dict
    data_count_dict[count_field] = data_count_dict[count_field] + num


def item_iterator(item, line, is_need_write):
    """
    递归迭代xml的标签
    Args:
        item: 标签
        line: 行数据

    Returns:
        返回行数据
    """
    items = list(item)
    for item in items:
        if list(item):
            is_need_write,line = item_iterator(item, line, is_need_write)
        else:
            val = str(item.text)
            if val == 'None':
                val = ""
            #if "," in val:
                # valis_need_write = True
            val = val.replace(",", "|")
            if line != "":
                line = line + "," + val
            else:
                line = val
    return is_need_write, line


def folder_flag(file_path):
    """
    文件路径处理
    Args:
        file_path: 文件路径

    Returns:
        返回处理后的文件路径
    """
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    if "\\" in file_path and not file_path.endswith("\\"):
        file_path = file_path + "\\"

    if "/" in file_path and not file_path.endswith("/"):
        file_path = file_path + "/"


def main_job(source_fol):
    allFiles = []
    # 遍历文件夹
    dirlist(source_fol, allFiles)
    thisTimeCou = len(allFiles)
    while thisTimeCou > 0:
        data_count('totalCoun', thisTimeCou)
        data_count('thisTimeCou', thisTimeCou)
        # 解析xml文件
        for file in allFiles:
            print("开始解析：" + file)
            redxml(file, fileName)
            filepath, shotname, extension = jwkj_get_filePath_fileName_fileExt(file)
            line_content = file_log(shotname)
            write_log(line_content)
            count_init()

        allFiles = []
        allFiles = dirlist(source_fol, allFiles)
        thisTimeCou = len(allFiles)

    log_content = total_log()
    write_log(log_content)


if __name__ == "__main__":
    folder_flag(source_folder)
    folder_flag(source_bak_folder)
    folder_flag(target_folder)
    folder_flag(log_folder)

    oneLevelFolder = []
    dirlistOneLevel(source_folder, oneLevelFolder)
    for fol in oneLevelFolder:
        print("开始处理：%s " % fol)
        main_job(fol)
