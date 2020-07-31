# _*_ coding: utf-8 _*_
# -------------------------------------------------------------------------------
#  @Time : 2020/7/23 14:06
#  @Author : yls
#  @Version：V 0.1
#  @File : count.py
#  @desc :
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


def file_starLineCnt(statfile, encoding='utf-8'):
    """
    统计文件的行数
    Args:
        statfile: 文件

    Returns:
        返回文件的总行数
    """
    cnt = 0
    with open(statfile, encoding=encoding,errors="ignor") as f:
        for line in f:
            if '<requestOrder>' in line:
                cnt += 1
        return cnt


if __name__ == '__main__':
    sourceFilePath = 'C:\\Users\\26896\\Desktop\\淘宝\\xml\\'
    allFile = dirlist(sourceFilePath,[])
    totalCount = 0
    for file in allFile:
        count = file_starLineCnt(file, 'gbk')
        print("%s =》%d "%(file,count))
        totalCount += count
    print("%s 文件夹，合计：%d" % (sourceFilePath,totalCount))
    pass
