# _*_ coding: utf-8 _*_
"""
 #  @Time : 2020/8/4 14:21 
 #  @Author : yls 
 #  @Version：V 0.1
 #  @File : mvFile.py
 #  @desc :
 """

import os
import shutil
import time


def dirlist(path, allfile):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
            # 控制每次扫描的文件数量限制：暂时是每扫描10W个文件处理一次
            if len(allfile) > 100:
                break
        else:
            if len(allfile) > 100:
                break
            print(len(allfile))
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


if __name__ == '__main__':
    time_sleep = 120
    allFile = []
    sourcePath = "/home/datafile/ORDERLIST/bak_20200701_20200728/result/mergers-120"
    taretPath = "/var/ftp/pub/ORDERLIST/mergers-120"
    # 对应的目标目录
    while True:
        allFile = dirlist(sourcePath, allFile)
        for file in allFile:
            try:
                print("开始移动文件："+file)
                # 文件备份
                move_file = file.replace(sourcePath, taretPath)
                # 解析文件路径、文件名称、文件后缀
                bak_path, bak_name, bak_ext = jwkj_get_filePath_fileName_fileExt(move_file)
                if not os.path.exists(bak_path):
                    os.makedirs(bak_path)
                shutil.move(file, move_file)
                print("文件移动结束："+file)
                time.sleep(0.5)
            except Exception as e:
                print(e)
        print("开始睡眠：" + str(time_sleep) + "s")
        time.sleep(time_sleep)
        print("睡眠结束：" + str(time_sleep) + "s")
