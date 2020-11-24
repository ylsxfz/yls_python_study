# _*_ coding: utf-8 _*_
"""
 #  @Time : 2020/11/11 16:05 
 #  @Author : yls 
 #  @Version：V 0.1
 #  @File : Test.py
 #  @desc :
 """

import re


def cover(text):
    text = re.sub(r'(\\u[0-9a-fA-F]{4})', lambda matched: matched.group(1).encode('utf-8').decode('unicode_escape'),
                  text)
    print(text)


if __name__ == '__main__':
    text = "      # \u8BBE\u7F6E\u4E0E Eureka Server\u7684\u4EA4\u4E92\u5730\u5740\uFF0C\u591A\u4E2A\u5730\u5740\u53EF\u4EE5\u7528 \u9017\u53F7\uFF08,\uFF09\u5206\u5272";
    cover(text)

    text = "    # \u662F\u5426\u4ECE Eureka Server\u4E2D\u83B7\u53D6\u6CE8\u518C\u4FE1\u606F\uFF0C\u9ED8\u8BA4\u4E3A true\uFF0C\u7531\u4E8E\u8FD9\u662F\u4E00\u4E2A\u5355\u4E00\u7684 Eureka Server\uFF0C\u4E0D\u9700\u540C\u6B65\u6570\u636E\uFF0C\u6545\u8BBE\u7F6E\u4E3A false"
    cover(text)

    text = "    # \u662F\u5426\u628A\u81EA\u5DF1\u6CE8\u518C\u5230 Eureka Server\uFF0C\u9ED8\u8BA4\u4E3A true\u3002\u7531\u4E8E\u5F53\u524D\u4E3AEureka Server,\u6545\u8BBE\u4E3A false"
    cover(text)
    pass
