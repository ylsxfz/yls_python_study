# _*_ coding: utf-8 _*_
# """
#  @Time : 2020/7/21 8:42
#  @Author : yls
#  @Version：V 0.1
#  @File : i_math_operation.py
#  @desc :数学运算、逻辑运算和进制转化相关的16个内置函数
#         max(iterable,*[, key, default]):函数形参列表中符号 * 表示，
#                     后面的形参只能为关键字参数（keyword argument），
#                     不能为位置参数（positional argument）
#                     例如：max(a,key=lambda x: a.count(x), default=1)
#
#                     [] 表示里面的形参是可选项，max 函数可被如下几种形式调用：
#                         1、max(iterable)
#                         2、max(iterable,*, key)
#                         3、max(iterable,*,default)
#                         4、max(iterable,*, key, default)
#
#         sum(iterable, /, start=0)：看到形参列表中有一个 /，
#                     它表示 / 前的参数只能是位置参数，不能是关键字参数。
#  """


class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "id = " + self.id + ", name = " + self.name


def math_basic_operation():
    """
    数学运算：
        len(s):返回对象内元素个数。

         max(iterable,*[,key,default]):返回最大值,max、min 函数都有一个参数 key，
                它们也被称为 key 函数，key 函数一般结合更紧凑的 lambda 函数。
                max有一个default参数：
                    1、当传入的列表为空时，若参数default被赋值，则返回default。
                    2、否则、会抛出序列的异常(empty sequence)

        pow(x,y,z=None,/)：x为底的y次幂，如果z给出，取余。

        round(number[,ndigits])：四舍五入，ndigits代表小数点后保留几位。

        sum(iterable,/,start=0)：q求和,start代表求和的初始值。

        abs(x,/):求绝对值或复数的模。

        divmod(a,b)：分别取商和余数。

        complex([real[,iag]])：创建有一个复数。

        hash(object)：返回对象的哈希值。

        id(object)：返回对象的内存地址。

    """
    dic = {'a': 1, 'b': 223, 'c': 43, 'd': 1241, 'e': 124124124}
    print("dict:" + str(dic))
    print("dict的长度为：" + str(len(dic)))
    print("dic的最大值为：" + str(max(dic)))

    a = [{'name': 'xiaoming', 'age': 18, 'gender': 'male'},
         {'name': 'xiaohong', 'age': 20, 'gender': 'female'}]
    print("a:" + str(a))
    print("a按照年龄比较，年龄大的为：" + str(max(a, key=lambda x: x['age'])))

    print("max传入的列表为空，default赋值为10，将返回10：" + str(max((), default=10)))

    print("pow(3,2) = %d" % pow(3, 2))
    print("pow(3,2,4) = %d" % pow(3, 2, 4))
    print()

    print("round(10.0222222,3)= %s " % str(round(10.0222222, 3)))
    print()

    a = [1, 4, 2, 3, 1]
    print("a = %s" % str(a))
    print("sum(a) = %d" % sum(a))
    print("sum(a,10) = %d " % sum(a, 10))
    print()

    print("abs(-6) = %d" % abs(-6))
    print()

    print("complex(1,2) = %s" % str(complex(1, 2)))
    print()

    xiaoming = Student('001', 'xiaoming')
    print('hash(xiaoming) = %s' % str(hash(xiaoming)))
    print()

    print('id(xiaoming) = %s' % str(id(xiaoming)))


def logical_operation():
    """
    逻辑运算：
        all(iterable)：接受一个迭代器，如果迭代器的所有元素都为真，返回True，否则返回False。

        any(iterable)：接受一个迭代器，如果迭代器里有一个元素为真，返回 True，否则返回 False。
    """
    print("all([1,0,1,12,1,12]) = %s" % str(all([1, 0, 1, 12, 1, 12])))
    print("all([1,1,12,1,12]) = %s" % str(all([1, 1, 12, 1, 12])))

    print("any([1,0,1,12,1,12]) = %s" % str(any([1, 0, 1, 12, 1, 12])))
    print("any([1,1,12,1,12]) = %s" % str(any([1, 1, 12, 1, 12])))


def base_conversion():
    """
    进制转换：
        ascii(object)：调用对象的repr()方法，获取该方法的返回值。

        bin(x)：将十进制转换为二进制。

        oct(x)：将十进制转换为八进制。

        hex(x)：将十进制转换为十六进制。

    """
    xiaoming = Student('001', 'xiaoming')
    print("xiaoming：" + str(xiaoming))
    print("ascii(xiaoming)：" + str(ascii(xiaoming)))
    print()

    print("bin(10) = %s" % bin(10))
    print()

    print("oct(10) = %s" % oct(10))
    print()

    print("hex(10) = %s" % hex(10))
    print()


def lst_max_lenth(*lst):
    """
    已知多个列表，找出列表更长的，使用max方法
    Args:
        *lst: 多个list
    """
    return max(*lst, key=lambda v: len(v))


if __name__ == '__main__':
    # 数学运算、逻辑运算和进制转化
    # math_basic_operation()

    # max_lst = lst_max_lenth([1, 234, 23, 42, 42, 35, 25], [1, 41, 41, 4, 14], [124, 14, 124, 123])
    # print(max_lst)

    # 逻辑运算
    # logical_operation()

    # 进制装换
    base_conversion()
    pass
