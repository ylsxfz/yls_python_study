# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         FileMerge
# Description:  
# Author:       yls
# Date:         2019/8/30
# -------------------------------------------------------------------------------
import os
import uuid
import shutil
import time

target_bak = "/home/datafile/ORDERLIST/bak_20200701_20200728/target_bak"
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
            # 控制每次扫描的文件数量限制：暂时是每扫描10W个文件处理一次
            if len(allfile) > 50000:
                break
        else:
            if len(allfile) > 50000:
                break
            print(len(allfile))
            allfile.append(filepath)
    return allfile


'''
 path:文件的路径
 allfile:待返回的数据。建议传入 []
'''


def dirlistOneLevel(path, allfile):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
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


'''获取文件大小'''


def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return formatSize(size)
    except Exception as err:
        print(err)


'''
合并文件
'''


def megerFile(sourceFile, targetFolder, fileName, fileSize, sourEncoding='utf-8'):
    # 判断文件夹是否存在，如果不存在，创建
    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder)
    while True:
        allFiles = dirlist(sourceFile, [])
        if len(allFiles) < 1:
            break
        if len(allFiles) < 49999:
            break
        buf = []
        try:
            for file in allFiles:
                msg = '**开始处理文件：' + file
                print(msg)
                fin = open(file, 'r', encoding=sourEncoding)
                for line in fin:
                    if '\n' not in line:
                        line = line + '\n'
                    line = line.replace('None','')
                    buf.append(line)
                    if len(buf) == fileSize:
                        fout = open(targetFolder + '/' + fileName + str(uuid.uuid1())  + ".csv", 'a',
                                    encoding='utf-8', errors='ignore')
                        try:
                            fout.writelines(buf)
                        finally:
                            fout.close()
                        buf = []
                fin.close()
                # 删除合并的文件
                # os.remove(file)
                try:

                    # 文件备份
                    move_file = file.replace(sourceFile, target_bak)
                    # 解析文件路径、文件名称、文件后缀
                    bak_path, bak_name, bak_ext = jwkj_get_filePath_fileName_fileExt(move_file)
                    if not os.path.exists(bak_path):
                        os.makedirs(bak_path)
                    shutil.move(file, move_file)
                except Exception as e:
                    print(e)
            if len(buf) != 0:
                fout = open(targetFolder + '/' + fileName + str(uuid.uuid1())  + ".csv", 'a',
                            encoding='utf-8', errors='ignore')
                try:
                    fout.writelines(buf)
                finally:
                    fout.close()
        finally:
            print('处理完毕。')


def megerFileController(sourcefolder, nowTargetFolder, fileName, fileSize, sourEncoding='utf-8'):
    global errorLink
    # 开始合并文件
    try:
        print("开始处理：")
        print("源数据目录：" + sourcefolder)
        print("目标目录：" + nowTargetFolder)
        megerFile(sourcefolder, nowTargetFolder, fileName, fileSize, sourEncoding='utf-8')
    except Exception as error:
        print(error)
        print("程序出现异常，将睡眠3分钟，然后尝试重新连接。")
        time.sleep(10)
        errorLink = errorLink + 1
        print("第" + str(errorLink) + "次重连")
        megerFileController(sourcefolder, nowTargetFolder, fileName, fileSize, sourEncoding='utf-8')


if __name__ == '__main__':
    sourceFile = "/home/datafile/ORDERLIST/bak_20200701_20200728/target"
    fileSize = 100000
    fileName = 'merge_'
    targetFolder = "/home/datafile/ORDERLIST/bak_20200701_20200728/mergers"
    errorLink = 0
    time_sleep = 180

    # 对应的目标目录
    while True:
        megerFileController(sourceFile, targetFolder, fileName, fileSize, sourEncoding='utf-8')
        print("开始睡眠："+str(time_sleep)+"s")
        time.sleep(time_sleep)
        print("睡眠结束：" + str(time_sleep) + "s")

    # time.sleep(10)
