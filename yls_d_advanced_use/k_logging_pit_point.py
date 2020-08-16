# _*_ coding: utf-8 _*_
"""
 #  @Time : 2020/8/14 15:33 
 #  @Author : yls 
 #  @Version：V 0.1
 #  @File : k_logging_pit_point.py
 #  @desc : python 常见的10个坑点合集和logging日志管理模块的使用总结。
        一：10个坑点合集：
            1、列表和 * 操作:
                原来 * 操作复制出的 a[0]、a[1]、...、a[5]，在内存中标识符是相等的，实现的仅仅是浅复制。
                不使用 *，使用列表生成式，复制出 5 个不同 id 的内嵌列表，这样就能避免赋值互不干扰的问题。

            2、列表内元素可重复出现，讨论如何删除列表中的某个元素:
                遍历 lst、remove 一次，移掉位置 i 后的所有元素索引都要减一。
                一旦删除的元素，重复出现在列表中，就总会漏掉一个该删除的元素。

            3、Python 函数的参数可设为默认值，如果一个默认参数类型为list，默认值为设置为[]
              为了避免这个隐藏的坑，函数的默认参数值切记不能设置为 []，而是为 None。这样即便按照默认值调用多次，也会规避此风险。

            4、{} 和 ()：
                初始创建的元组对象，若只有一个元素，只用一对括号是不够的，下面 single 对象不会被解释为元组，而是 float 型。
                还有创建集合与字典，它们都用一对 {}，但是默认返回字典，而不是集合。
                要想创建空集合，可使用内置函数 set()。

            5、解包：Python 中，支持多值赋值给多变量的操作。最常见的用法，一行代码交换两个变量。
                记住一点：多值赋值是先计算出等号右侧的所有变量值后，再赋值给等号左侧变量。
                这种多值赋值，是一种解包（unpack）操作。
                既然是解包，那么就得先有打包。的确，等号右侧的多个变量，会被打包（pack）为一个可迭代对象。
                赋值操作，就相当于解包。
                更为简洁、紧凑的做法：等号左侧定义两个我们想要的变量，其他不想要的项放到 others 变量中，并在前加一个 *，如下所示：
                sid, name, *others =  [1,'xiaoming','address','telephone',['','','...']]

            6、访问控制：
                a、Python 是一门动态语言，支持属性的动态添加和删除。
                而 Python 面向对象编程（OOP）中，提供很多双划线开头和结尾的函数，
                它们是系统内置方法，被称为魔法方法。
                如 __getattr__ 和 __setattr__ 是关于控制属性访问的方法。
                b、重写 __getattr__ 方法，会定义不存在属性时的行为。如下，访问类不存在属性时，程序默认会抛出 AttributeError 异常。
                c、只要涉及属性赋值，赋值前都会调用 __setattr__ 方法：
                    但是，使用它很容易掉进一个坑，__setattr__ 里再次涉及属性赋值，这样会无限递归下去。
                    为保险起见，不要在 __setattr__ 方法中再做属性赋值。

            7、中括号访问：
                某个对象具有 [index]，返回某个元素值。那么，它们是怎么实现这种中括号索引的呢？只要重写魔法方法 __getitem__，就能实现 [index] 功能。
                类 Table 是一个最精简的具备中括号索引的类。构造函数 __init__ 传入一个字典，__getitem__ 返回字典键为 column_name 的字典值。

            8、鸭子类型：
                Python 是动态语言，对函数参数的类型要求很宽松，函数体内使用此类型的方法或属性时，
                只要满足有它们就行，不强制要求必须为这个类或子类。
                但是，对静态类型语言，如 Java，参数类型就必须为此类型或子类。

            9、元类：
                元类，会被 Pythoner 经常提起，元类确实也有一些使用场合。但是，它又是很高深的、偏底层的抽象类型。
                Python 界的领袖 Tim Peters 说过：“元类就是深度的魔法，99% 的用户应该根本不必为此操心。”
                Python 中，将描述 Student 类的类被称为：元类

            10、对象序列化：
                对象序列化，是指将内存中的对象转化为可存储或传输的过程。很多场景，直接一个类对象，传输不方便。
                但是，当对象序列化后，就会更加方便，因为约定俗成的，接口间的调用或者发起的 Web 请求，一般使用 JSON 串传输。

        二：logging日志管理模块：
            日志写入不是我们想象的这般简单。如果一直向同一个文件里写，文件就会变得很大很大；也不方便分析。
            更糟糕的是，文件越来越大，当大小等于磁盘容量时，后面的日志信息就无法再写入。当然，还有更多问题会出现。
            Python 中，也有一个模块 logging，也能做到高效的日志管理。
            例如，logging 模块，能按照指定周期切分日志文件。这一切的规则，都是为了实现对日志的高效管理。
            这些需求背后，对应着一套解决方案，也就是 logging 库，和它的四大组件：记录器、处理器、过滤器和格式化器。

 """
import json
import logging
from logging import handlers


def list_more():
    """
    列表和 * 操作:
        原来 * 操作复制出的 a[0]、a[1]、...、a[5]，在内存中标识符是相等的，实现的仅仅是浅复制。
        不使用 *，使用列表生成式，复制出 5 个不同 id 的内嵌列表，这样就能避免赋值互不干扰的问题。
    """
    print(['|'] * 10)
    print([[]] * 5)
    a = []
    a = [[]] * 5
    a[0].extend([1, 3, 5])
    a[1].extend([2, 4, 6])
    print(a)

    b = [[] for _ in range(5)]
    b[0].extend([1, 3, 5])
    b[1].extend([2, 4, 6])
    print(b)


def list_del(lst, e):
    """
    列表内元素可重复出现，讨论如何删除列表中的某个元素:
        遍历 lst、remove 一次，移掉位置 i 后的所有元素索引都要减一。
        一旦删除的元素，重复出现在列表中，就总会漏掉一个该删除的元素。
    """
    i = 0
    while i < len(lst):
        if lst[i] == e:
            lst.remove(lst[i])
        else:
            i += 1
    return lst


# def delta_val(val, volume=[]):
def delta_val(val, volume=None):
    """
    Python 函数的参数可设为默认值，如果一个默认参数类型为list，默认值为设置为[]

    为了避免这个隐藏的坑，函数的默认参数值切记不能设置为 []，而是为 None。这样即便按照默认值调用多次，也会规避此风险。
    Args:
        val: 参数
        volume: 默认为空的参数
    """
    print(id(volume))
    if volume is None:
        volume = []
    size = len(volume)
    for i in range(size):
        volume[i] = i + val
    return volume


def dict_tuple():
    point = (1.0, 3.0)
    # 初始创建的元组对象，若只有一个元素，只用一对括号是不够的，
    # 下面 single 对象不会被解释为元组，而是 float 型。
    single = (1.0)
    print(type(single))
    # 要想被解释为元组，在后面必须要加一个逗号：
    single = (1.0,)
    print(type(single))


def fix_points(pts):
    for i in range(len(pts)):
        t = pts[i]
        if isinstance(t, tuple):
            t = t if len(t) == 2 else (t[0], 0.0)
            pts[i] = t
        else:
            raise TypeError('pts 的元素类型要求为元组')
    return pts


def set_dict():
    """
    还有创建集合与字典，它们都用一对 {}，但是默认返回字典，而不是集合。
    要想创建空集合，可使用内置函数 set()。
    """
    d = {}
    print(type(d))

    s = set()
    print(type(s))


def unpack():
    """
    支持多值赋值给多变量的操作:
        多值赋值是先计算出等号右侧的所有变量值后，再赋值给等号左侧变量。
        这种多值赋值，是一种解包（unpack）操作。
        既然是解包，那么就得先有打包。的确，等号右侧的多个变量，会被打包（pack）为一个可迭代对象。
        赋值操作，就相当于解包。
    """
    a, b = 1, 2
    a, b = b + 1, a + b
    print(a, b)

    def foo():
        result = [1, 'xiaoming', 'address', 'telephone', ['', '', '...']]
        return result

    sid, name, *others = foo()
    print(sid)
    print(name)
    print(others)


class Student():
    def __init__(self, idt, name):
        self.idt = idt;
        self.name = name

    def __getattr__(self, prop_name):
        print('property %s not existed, would be set to None automatically' %
              (prop_name,))
        self.prop_name = None

    def __setattr__(self, prop_name, val):
        print('%s would be set to %s' % (prop_name, str(val)))


class Table(object):
    def __init__(self, dt: dict):
        self.dt = dt

    def __getitem__(self, item):
        return self.dt[item]


class Plane():
    def run(self):
        return 'plane is flying...'


class Clock():
    def run(self):
        return 'clock is flying...'


def using_rnn(duck):
    print(duck.run())


class Stu():
    def __init__(self, **args):
        self.ids = args['ids']
        self.name = args['name']
        self.address = args['address']


class Logger(object):
    """
    一个基本的日志类，同时将日志显示在控制台和写入文件中，同时按照天为周期切分日志文件。
    """
    kv = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s-%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.kv.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(
            filename=filename, when=when, backupCount=backCount, encoding='utf-8')
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到 logger 里
        self.logger.addHandler(th)


# 创建 log 对象，日志级别为 debug 及以上的写入日志文件：
log = Logger('files/all.log', level='debug').logger


class NewStudent:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        log.info('学生 id: %s, name: %s' % (str(id), str(name)))

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if isinstance(score, int):
            self.__score = score
            log.info('%s得分：%d' % (self.name, self.score))
        else:
            log.error('学生分数类型为 %s，不是整型' % (str(type(score))))
            raise TypeError('学生分数类型为 %s，不是整型' % (str(type(score))))


if __name__ == '__main__':
    # list和 * 操作
    # list_more()

    # list删除元素
    # reult = list_del([1, 2, 4, 53, 2, 2, 23, 2, 523, 5], 2)
    # print(reult)

    # 函数的默认参数为空
    # result = delta_val(10)
    # print(result)
    # result.append(1)
    # result.append(2)
    # print(result)
    # result = delta_val(10)
    # print(result)

    # {} 和 ()
    # dict_tuple()
    # 下面这行调用会报错：TypeError: pts 的元素类型要求为元组
    # fix_points([(1.0,3.0),(2.0),(5.0,4.0)])
    # result = fix_points([(1.0, 3.0), (2.0,), (5.0, 4.0)])
    # print(result)

    # 集合和字典
    # set_dict()

    # 解包
    # unpack()

    # 访问控制
    # xiaoming = Student(1, 'xiaoming')
    # print(xiaoming.address)  # 读取
    # xiaoming.address = 'beijing'
    # print(xiaoming.address)

    # 中括号访问
    # t = Table({'ids':list(range(5)),'name':'li zhang liu guo song'.split()})
    # print(t['name'])
    # print(t['ids'])

    # 鸭子类型
    # Plane 对象和 Clock 对象，因都有 run 方法，Python 认为它们看起来就是 duck 类型，
    # 因此，Plane 对象和 Clock 对象就被看作 duck 类型。
    # using_rnn(Plane())
    # using_rnn(Clock())

    # 对象序列化
    # xiaoming = Stu(ids=1, name='xiaoming', address='北京')
    # xiaohong = Stu(ids=2, name='xiaohong', address='南京')
    # with open('files/json.txt', 'w', encoding='utf-8') as f:
    #     json.dump([xiaoming, xiaohong], f, default=lambda obj: obj.__dict__, ensure_ascii=False, indent=2,
    #               sort_keys=True)

    # xiaoming = NewStudent(10010, 'xiaoming')
    # xiaoming.score = 88
    # xiaohong = NewStudent('001', 'xiaohong')
    # xiaohong.score = 90.6
    pass
