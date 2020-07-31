# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/7/19  15:30
#  @Author: yls
#  @Version: V 0.1
#  @File: b_str.py
#  @Desc:
"""

import re


def strTest():
    """
    字符串的相关方法
    Returns:

    """
    tmpStr = " I love python;  "
    print("原始str：" + tmpStr)
    print("去除前后的空格：" + tmpStr.strip())
    print("原始str：" + tmpStr)
    print("替换所有空格：" + tmpStr.replace(' ', ''))
    print("原始str：" + tmpStr)
    print("合并字符串：" + (''.join([tmpStr, "But I don't love math"])))
    print("原始str：" + tmpStr)
    print("首字母大写：" + tmpStr.title())
    print("返回起始位置：" + str(tmpStr.find("python")))


def is_rotation(s1: str, s2: str) -> bool:
    """
    判断字符串 str1 是否为 str2 旋转而来
    Args:
        s1: 字符串1
        s2: 字符串2

    Returns:
        bool类型的值：true 表示 str1 是 str2 旋转而来
                    false 表示 str1 不是 str2 旋转而来

    """
    if s1 is None or s2 is None:
        return False
    if len(s1) != len(s2):
        return False

    def is_substring(s1: str, s2: str) -> bool:
        return s1 in s2

    return is_substring(s1, s2 + s2)


def reTest():
    pat = re.compile(r'[\da-zA-Z]{6,20}')
    # 返回None，长度小于6
    print(pat.fullmatch('qaz12'))
    # 返回None
    print(pat.fullmatch("asfarqwrqwrqwetqwetqewtqwe124125215125"))
    # 返回None，包含下划线
    print(pat.fullmatch("qaz_123"))
    # 完全符合规则：<_sre.SRE_Match object; span=(0, 10), match='asda123214'>
    print(pat.fullmatch("asda123214"))


if __name__ == '__main__':
    strTest()
    print(is_rotation("yls_xfz", "zfx_sly"))
    print(is_rotation("yls_xfz", "xfzyls_"))

    reTest()
    pass
