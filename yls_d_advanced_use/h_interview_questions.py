# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/08 18:02 
#  @Author: yls 
#  @Version: V 0.1
#  @File: h_interview_questions.py
#  @Desc: 30道面试题：
"""
from functools import reduce
import random
from datetime import datetime
import os
import pandas as pd
import re
from collections import Counter, defaultdict
from collections.abc import Iterator
import threading
import time

a = 0


def interview_question_0_10():
    print("*********************************》1《******************************************")
    print("==》1、一行代码生成[1,3,5,7,9,11,13,15,17,19]：")
    a = [i * 2 + 1 for i in range(10)]
    print(a)
    print()

    print("*********************************》2《******************************************")
    print("==》2、写一个等差数列：首项为10，公差为12，末项不大于100的列表："
          "")
    a = list(range(10, 100, 12))
    print(a)
    print()

    print("*********************************》3《******************************************")
    print("==》3、一行代码求和1到10000内整数和：sum函数或者reduce函数：")
    a = sum(range(10000))
    print(a)

    a = reduce(lambda x, y: x + y, range(10000))
    print(a)
    print()

    print("*********************************》4《******************************************")
    print("==》4、打乱一个列表：")
    b = list(range(10))
    print(b)
    random.shuffle(b)
    print("打乱后：%s" % str(b))
    print()

    print("*********************************》5《******************************************")
    print("==》5、字典按value排序并返回新字典：")
    d = {'a': 12, 'b': 3, 'c': 50, 'd': 1}
    d = dict(sorted(d.items(), key=lambda item: item[1]))
    print(d)
    print()

    print("*********************************》6《******************************************")
    print("==》6、如何删除list中重复的元素，并保证元素顺序不变：")
    a = [3, 2, 2, 2, 1, 3]
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
    print()

    print("*********************************》7《******************************************")
    print("==》7、怎么找出两个列表的相同元素和不同元素：")
    a = [3, 2, 2, 2, 1, 3]
    b = [1, 4, 3, 4, 5]
    aset, bset = set(a), set(b)
    same = aset.intersection(bset)
    differ = aset.difference(bset).union(bset.difference(aset))
    print("same:" + str(same))
    print("differ:" + str(differ))

    print("*********************************》8《******************************************")
    print("==》8、字符串处理成字典：")
    a = "k0:10|k1:2|k2:11|k3:5"
    m = map(lambda x: x.split(":"), a.split("|"))
    ma = {mi[0]: int(mi[1]) for mi in m}
    print(ma)
    print()

    print("*********************************》9《******************************************")
    print("==》9、输入日期，判断这一天是这一年的第几天：")

    def get_day_of_year(y, m, d):
        return datetime(y, m, d).date().timetuple().tm_yday

    print(get_day_of_year(2020, 2, 1))
    print(get_day_of_year(2019, 12, 31))
    print()

    print("*********************************》10《******************************************")
    print("==》10、遍历目录和子目录，抓取.py文件")

    def get_files(directory, ext):
        res = []
        for root, dirs, files in os.walk(directory):
            for filename in files:
                name, suf = os.path.splitext(filename)
                if suf == ext:
                    res.append(os.path.join(root, filename))
        return res

    print(get_files("../yls_b_web", '.py'))
    print()


def interview_question_10_20():
    print("*********************************》11《******************************************")
    print("==》11、单机4G内存，处理10G文件的方法：")

    def python_read(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                yield line

    def pandas_read(filename, sep=',', chunksize=5):
        """
        Args:
            filename: 文件名称
            sep: 分隔符
            chunksize: 每次读取5行
        """
        reader = pd.read_csv(filename, sep=sep, chunksize=chunksize)
        while True:
            try:
                yield reader.get_chunk()
            except StopIteration:
                print('---Done---')
                break

    # a = python_read('files/a.csv')
    # print(a.__next__())
    # b = pandas_read('files/a.csv')
    # print(b.__next__())
    print()

    print("*********************************》12《******************************************")
    print("==》12、统计一个文本中单词频次出现最高的10个单词：")
    d = defaultdict(int)

    def process(line):
        for word in re.sub('\W+', " ", line).split():
            d[word] += 1

    for line in python_read('files/a.txt'):
        process(line)
    most10 = Counter(d).most_common(10)
    print(most10)
    print()

    print("*********************************》13《******************************************")
    print("==》13、反转一个整数：例如 -12345 --> -54321:")

    def reverse_int(x: int):
        if -10 < x < 10:
            return x
        sx = str(x)

        def rever_str(sx):
            return sx[::-1]

        if sx[0] == '-':
            sx = rever_str(sx[1:])
            x = int(sx)
            return - x
        sx = rever_str(sx)
        return int(sx)

    print(reverse_int(-1234556))
    print()

    print("*********************************》14《******************************************")
    print("==》14、代码输出的结果:")

    def f():
        i = 0

        def foo(x):
            return i * x

        rtn = []
        while i < 3:
            rtn.append(foo)
            i += 1
        return rtn

    # 调用函数 f
    for fs in f():
        print(fs(10))
    print()

    print("*********************************》15《******************************************")
    print("==》15、函数调用是否正确:")
    """
    A foo('.', 10) 错误
    B foo('.', 0,1,10) 正常
    C foo('.',0,1,c=10) 正确
    D foo('.',a=0,1,10) 错误
    E foo(filename='.', c=10) 正确
    F foo('.', c=10) 正确
    
    A 错误，a 被赋值为 10
    B 正确，c 是位置参数
    C 正确，c 是关键字参数
    D 错误，位置参数不能位于关键字参数后面
    E 正确，filename 和 c 都是关键字参数
    F 正确，filename 位置参数，c 是关键字参数
    """

    def foo(filename, a=0, b=1, c=2):
        print('filename: %s \n c: %d' % (filename, c))

    print()

    print("*********************************》16《******************************************")
    print("==》16、key 值为 lambda 函数，说说 lambda 函数的形参和返回值。:")
    """
    lambda 函数的形参：s 解包后的元素值，可能取值为：{1,3,5,7}、{1,5,7}、{2,4,6,7,8} 三种
    lambda 函数的返回值为：元素的长度，可能取值为：{1,3,5,7}、{1,5,7}、{2,4,6,7,8} 的长度 4,3,5。
    """

    def longer(*s):
        return max(*s, key=lambda x: len(x))

    a = longer({1, 3, 5, 7}, {1, 5, 7}, {2, 4, 6, 7, 8})
    print(a)
    print()

    print("*********************************》17《******************************************")
    print("==》17、正则匹配负整数:")
    """
    匹配所有负整数，不包括 0。正则表达式：^-[1-9]\d*$
        1、 ^- 表示字符串以 -开头
        2、[1-9] 表示数字 1 到 9，注意不要写成 \d，因为负整数没有以 -0 开头的
        3、\d* 表示数字 0 到 9 出现 0 次、1 次或多次
        4、$ 表示字符串以数字结尾
    """
    s = ['-1', '-15756', '9', '-01', '10', '-']
    pat = r'^-[1-9]\d*$'
    rec = re.compile(pat)
    rs = [i for i in s if rec.match(i)]
    print(rs)
    print()

    print("*********************************》18《******************************************")
    print("==》18、正则匹配负浮点数:")
    """
    正确写出匹配负浮点数的正则表达式，要先思考分析。
        1、考虑到两个实例：-0.12、-111.234，就必须要分为两种情况。
        2、适应实例 -0.12 的正则表达式：^-0.\d*[1-9]\d*$，注意要考虑到 -0.0000 这种非浮点数，因此正则表达式必须这样写。
        3、不要想当然地写为：^-0.\d*$，或者 ^-0.\d*[1-9]*$，或者 ^-0.\d*[0-9]*$，这些都是错误的！
        4、适应实例 -111.234 的正则表达式：^-[1-9]\d*.\d*$，使用 |，综合两种情况，故正则表达式为：
            ^-[1-9]\d*\.\d*|-0\.\d*[1-9]\d*$
    """
    s = ['-1', '-1.5756', '9', '-0.0001', '10', '-0000.1', '-', '-0.00000']
    pat = r'^-[1-9]\d*\.\d*|-0\.\d*[1-9]\d*$'
    rec = re.compile(pat)
    rs = [i for i in s if rec.match(i)]
    print(rs)
    print()

    print("*********************************》19《******************************************")
    print("==》19、使用filter()求出列表中大于10的元素:")
    a = [15, 2, 7, 20, 400, 10, 9, -15, 107]
    a = list(filter(lambda x: x > 10, a))
    print(a)
    print()

    print("*********************************》20《******************************************")
    print("==》20、说说下面 map 函数的输出结果:")
    m = map(lambda x, y: min(x, y), [5, 1, 3, 4], [3, 4, 3, 2, 1])
    print(list(m))
    print()


def interview_question_20_30():
    print("*********************************》21《******************************************")
    print("==》20、说说 reduce 函数的输出结果:")
    """
    reduce 实现对列表的归约化简，规则如下：
        f(x,y) = x*y + 1
    因此，下面归约的过程为：
        f(1,2) = 3
        f(3,3) = 3*3 + 1 = 10
        f(10,4) = 10*4 + 1 = 41
        f(41,5) = 41*5 + 1 = 206
    """
    res = reduce(lambda x, y: x * y + 1, [1, 2, 3, 4, 5])
    print(res)
    print()

    print("*********************************》22《******************************************")
    print("==》22、x = (i for i in range(5))，x 是什么类型:")
    """
    x 是生成器类型，与 for 等迭代，输出迭代结果
    """
    x = (i for i in range(5))
    for i in x:
        print(i)
    print()

    print("*********************************》23《******************************************")
    print("==》23、可变类型和不可变类型分别列举 3 个:")
    print("可变类型,mutable type：list,dict,set,deque等")
    print("不可变类型,immutable type：int,float,str,tuple,frozenset等")
    print()

    print("*********************************》24《******************************************")
    print("==》24、is 和 == 有什么区别？:")

    print("is：用来判断两个对象的标识好是否相等")
    print("==：用于判断值或内容是否相等，默认是基于两个对象的标识号比较。")
    print("也就是说，如果 a is b 为 True 且如果按照默认行为，意味着 a==b 也为 True。")
    print()

    print("*********************************》25《******************************************")
    print("==》25、写一个学生类 Student:")

    class Student:
        def __init__(self, id, name):
            self.id = id
            self.name = name

        def __eq__(self, other):
            return self.id == other.id

    s1 = Student(10, 'xiaoming')
    s2 = Student(20, 'xiaohong')
    s3 = Student(10, 'xiaoming2')
    print("s1==s2：%s " % str(s1 == s2))
    print("s1==s3：%s " % str(s1 == s3))
    print()

    print("*********************************》26《******************************************")
    print("==》26、 有什么方法获取类的所有属性和方法？:")

    print("获取类上的所有属性和方法:")
    print(dir(Student))
    print("获取实例上的属性和方法:")
    print(dir(s1))
    print()

    print("*********************************》27《******************************************")
    print("==》27、Python 中如何动态获取和设置对象的属性？:")
    print("hasattr(s1,'id')：%s" % str(hasattr(s1, 'id')))
    print("hasattr(s1,'address')：%s" % str(hasattr(s1, 'address')))
    print()

    print("*********************************》28《******************************************")
    print("==》28、:实现一个按照 2*i+1 自增的迭代器")

    class AutoIncrease(Iterator):
        def __init__(self, init, n):
            self.init = init
            self.n = n
            self.__cal = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.__cal == 0:
                self.__cal += 1
                return self.init
            while self.__cal < self.n:
                self.init *= 2
                self.init += 1
                self.__cal += 1
                return self.init
            raise StopIteration

    iter = AutoIncrease(1, 10)
    for i in iter:
        print(i)
    print()

    print("*********************************》29《******************************************")
    print("==》29、实现文件按行读取和操作数据分离功能:")

    def read_line(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                yield line

    def process_line(line: str):
        print(line)
        pass

    for line in read_line('files/a.csv'):
        process_line(line)
    print()

    print("*********************************》30《******************************************")
    print("==》30、使用 Python 锁避免脏数据出现的例子:")
    """
    使用多线程编程，会出现同时修改一个全局变量的情况，创建一把锁 locka：
    多线程的代码，由于避免脏数据的出现，基本退化为单线程代码，执行效率被拖累。
    """
    locka = threading.Lock()

    def add1():
        global a
        try:
            # 获得锁
            locka.acquire()
            tmp = a + 1
            time.sleep(0.2)
            a = tmp
        finally:
            locka.release()
        print('%s adds a to 1: %d' % (threading.current_thread().getName(), a))

    threads = [threading.Thread(name='t%d' % (i,), target=add1()) for i in range(10)]
    [t.start() for t in threads]
    print()
    print()

    print("*********************************》31《******************************************")
    print("==》31、说说死锁、GIL 锁、协程:")
    """
    多个子线程在系统资源竞争时，都在等待对方解除占用状态。
    1、比如，线程 A 等待着线程 B 释放锁 b，同时，线程 B 等待着线程 A 释放锁 a。在这种局面下，
    
    2、线程 A 和线程 B 都相互等待着，无法执行下去，这就是死锁。
        为了避免死锁发生，Cython 使用 GIL 锁，确保同一时刻只有一个线程在执行，所以其实是伪多线程。
        
    3、所以，Python 里常常使用协程技术来代替多线程。多进程、多线程的切换是由系统决定，
        而协程由我们自己决定。协程无需使用锁，也就不会发生死锁。同时，利用协程的协作特点，
        高效的完成了原编程模型只能通过多个线程才能完成的任务。
    """
    print()
    print()


if __name__ == '__main__':
    print("*********************************》《******************************************")
    print("==》、:")

    print()
    print()
    # interview_question_0_10()
    # interview_question_10_20()
    interview_question_20_30()
    pass
