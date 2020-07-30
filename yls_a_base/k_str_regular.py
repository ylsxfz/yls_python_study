# _*_ coding: utf-8 _*_
# """
#  @Time : 2020/7/22 8:46
#  @Author : yls
#  @Version：V 0.1
#  @File : k_str_regular.py
#  @desc : 字符串和正则介绍：
#             1、基本的字符串操作
#             2、高级字符串操作之正则部分
#  """
import re


def str_basic_operation():
    """
    字符串基本操作：
        reversed：反转字符串。

        join：串联字符串。

        split：分割字符串。

        replace：字符串替换。

        in：判断a字符串是否为b字符串的子串。

        find：返回字符串b中匹配a字符串的最小索引。

        strip()：清理字符串开头和结尾的空格和制表符。

        encode()：字符串编码。

    """
    # 反转字符串
    s = "python"
    rs = ''.join(reversed(s))
    print(s + "反转后：%s" % rs)

    java, python = "java", "python"
    jl, pl = len(java), len(python)
    print()

    print("字符串切片操作：")
    lst = [str(java[i % 3 * jl:] + python[i % 5 * pl:] or i) for i in range(1, 10)]
    print(lst)
    print()

    mystr = ['1', 'love', 'python']
    joinStr = '_'.join(mystr)
    print(str(mystr) + "用_连接后：" + joinStr)
    splitStr = joinStr.split('_')
    print(joinStr + "用_分割后：" + str(splitStr))
    print()

    print(joinStr + "替换小写的o为大写的O：" + joinStr.replace('o', 'O'))
    print()

    a = 'our'
    b = 'flourish'
    r = True if a in b else False
    print(a + "是否为 %s 的子串：%s " % (b, str(r)))
    r = b.find(a)
    print(a + "在 %s 中的最小索引为：%d " % (b, r))

    a = ' \tI love python  \b\n'
    print("a = %s" % a)
    print(a + "使用strip()方法后：%s" % a.strip())
    print()

    mystr_byte = joinStr.encode('utf-8')
    print(len(mystr_byte))


def regex_expression():
    """
    正则表达式：
        元字符：
            .：匹配除了“\n”和"\r"之外的任务单个字符。
            ^：匹配字符串开始的位置。
            $：匹配字符串结束的位置。
            *：前面的原子重复0次、1次、多次。
            ？：前面的原子重复0次或者1次。
            +：前面的原子重复1次或多次。
            {n}：前面的原子出现了n次。
            {n,}：前面的原子至少出现n次。
            {n,m}：前面的原子出现次数介于n-m之间。
            ()：分组，输出需要的部分。

        通用字符：
            \s：匹配空白字符。
            \w：匹配任意字母/数字/下划线。
            \W：和\w相反，匹配任意字母/数字/下划线以外的字符。
            \d：匹配十进制数字。
            \D：匹配除了十进制以外的值。
            [0-9]：匹配一个0-9之间数字。
            [a-z]：匹配小写英文字母。
            [A-Z]：匹配大写英文字母。

        search()：找出子串第一个匹配位置。注意：在字符串的任意位置匹配。
        match()：找出子串第一个匹配位置。注意：在字符串的开始位置匹配。

        finditer()：匹配迭代器。返回所有子串匹配位置的迭代器。
                通过返回对象 re.Match,使用它的方法 span 找出匹配的位置。

        findall()：所有匹配，找出所有子串的所有匹配。

        split()；分割单词。正则模块中 split 函数强大，
                能够处理复杂的字符串分割任务。
                如果一个规则简单的字符串，直接使用字符串，split 函数。

        sub()：正则模块，sub方法，替换匹配的子串。

        compile()：预编译。如果要用同一匹配模式，做很多次匹配，可以使用 compile 预先编译串。

    """
    # search()：找出子串第一个匹配位置。注意：在字符串的任意位置匹配。
    s = 'I love python very much.'
    pat = 'python'
    r = re.search(pat, s)
    index = r.span()
    print("search()：%s 在 %s 中第一次出现的位置：%s" % (pat, s, str(index)))
    print()

    # match()：找出子串第一个匹配位置。注意：在字符串的开始位置匹配
    recom = re.compile(pat)
    r = recom.match(s)
    print("match()：%s 在 %s 是否在开始出现的位置：%s" % (pat, s, str(r)))
    print()

    # finditer()：匹配迭代器。返回所有子串匹配位置的迭代器。
    s = "山东省潍坊市青州第1中学高三1班"
    pat = '1'
    r = re.finditer(pat, s)
    print('"%s" 中所有的子串 "%s" ：' % (s, pat))
    for i in r:
        print(i)
    print()

    # findall()：找出所有匹配的字符串
    s = '一共20行代码运行2次，每次时间13.59s'
    # 找出所有的数字：通用字符 \d 匹配
    pat = r'\d+'
    r = re.findall(pat, s)
    print('"%s"中所有的数字：%s' % (s, str(r)))

    # split()：分割
    s = 'id\\tname\\taddress'
    print("s = %s 执行 s.split('\\t')后：%s" % (s, str(s.split('\\t'))))
    s = 'This,,,   module ; \t   provides|| regular ; '
    words = re.split('[,\\s;|]+', s)
    print(words)
    print()

    # sub()：替换字符串
    content = "hello 12345, hello 456321"
    pat = re.compile(r'\d+')
    m = pat.sub('666', content)
    print("'%s' 替换所有的数字为666后：%s" % (content, m))

    # compile()：预编译。如果要用同一匹配模式，
    # 做很多次匹配，可以使用 compile 预先编译串。
    s = [-16, 'good', 1.5, 0.2, -0.1, '11.43', 10, '5e10']
    rec = re.compile(r'^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$')
    print([i for i in s if rec.match(str(i))])


def regex_number():
    """
    案例：匹配浮点数和整数
        ? ：表示前一个字符匹配0或1次。
        .? ：表示匹配小数点(.)0次或1次。
    """
    s = '一共20行代码运行2次，每次时间13.59s'
    pat = r'\d+\.?\d+'
    r = re.findall(pat, s)
    print('"%s"中所有的数字（包括浮点数）：%s' % (s, str(r)))

    pat = r'\d+\.?\d*'
    r = re.findall(pat, s)
    print('"%s"中所有的数字（包括浮点数）：%s' % (s, str(r)))

    """
    匹配正整数：匹配所有正整数的正则表达式
        '^\\d*$'：会匹配到0，不准确
        '^[1-9]*'：会匹配 1. 串中的1，不是完全匹配，体会 $ 的作用。
        '^[1-9]\\d*$'：匹配正整数。
    """
    s = [-16, 1.5, 11.43, 10, 5]
    pat = '^[1-9]\\d*$'
    result = [i for i in s if re.match(pat, str(i))]
    print("%s 中的正整数：%s" % (str(s), str(result)))

    s = 'That'
    pat = r't'
    # re.I：是方法的可选参数，表示忽略大小写。
    r = re.finditer(pat, s, re.I)
    for i in r:
        print(i)


def regex_greedy_capture():
    """
    贪心捕获：
        (.*) 表示捕获任意多个字符，尽可能多地匹配字符，也被称为贪心捕获
        (.*) 的正则分解图如下所示，. 表示匹配除换行符外的任意字符。
    """
    content = '''<h>ddedadsad</h><div>graph</div><div>math</div>'''
    print("content = %s " % content)
    result = re.findall(r'<div>(.*)</div>', content)
    print(result)


def regex_not_greedy_capture():
    """
    非贪心捕获：
        (.*?)：非贪心捕获
    """
    content = ''' <h>ddedadsad</h><div>graph</div><div>math</div>'''
    print("content = %s " % content)
    result = re.findall(r'<div>(.*?)</div>', content)
    print(result)


if __name__ == '__main__':
    # 字符串基本操作
    # str_basic_operation()

    # 正则表达式
    # regex_expression()

    # 匹配浮点数和整数
    # regex_number()

    # 贪心捕获
    regex_greedy_capture()
    # 非贪心捕获
    regex_not_greedy_capture()
    pass
