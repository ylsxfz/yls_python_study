# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         SearchWork
# Description:  
# Author:       yls
# Date:         2019/4/15
# -------------------------------------------------------------------------------

import os

'''
 path:文件的路径
 allfile:待返回的数据。建议传入 []
'''


def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile


'''
字节bytes转化kb\m\g
'''


def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fkb" % (kb)


'''获取文件大小'''


def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return formatSize(size)
    except Exception as err:
        print(err)


def getFileCount(filepath, encoding='utf-8'):
    count = 0
    for index, line in enumerate(open(filepath, 'r', encoding=encoding, errors='ignore')):
        count += 1
    print(filepath + "文件总计行数：" + str(count))
    return count


if __name__ == '__main__':
    total = 0
    allFiles = dirlist("/home/datafile/ORDERLIST/bak_20200701_20200728/target", [])
    for file in allFiles:
        try:
            count = getFileCount(file)
            print(file + ":" + str(count))
            total = total + count
        except Exception as error:
            count = getFileCount(file, encoding='utf-8')
            total = total + count
            print(file + "error")
    print("总计：" + str(total))
