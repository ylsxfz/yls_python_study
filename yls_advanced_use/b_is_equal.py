# _*_ coding: utf-8 _*_
# -------------------------------------------------------------------------------
#  @Time : 2020/7/27 10:26
#  @Author : yls
#  @Version：V 0.1
#  @File : b_is_equal.py
#  @desc : Python 中，对象相等性比较相关关键字包括 is、in，比较运算符有 ==:
#             1、is：判断两个对象的标识号是否相等。
#             2、in：用于成员检测。
#             3、==：用于判断值或内容是否相等，默认是基于两个对象的标识号比较。
# -------------------------------------------------------------------------------


def is_equal():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(id(a))
    print(id(b))
    print(a is b)

    a, b = [], []
    print(a is b)

    a, b = 123, 123
    print(a is b)

    c = 123456
    d = 123456
    print('c == d:')
    print(id(c) == id(d))
    print(c is d)

    a = None
    b = None
    print(a is b)


def in_fun():
    print('ab' in 'abc')
    print('abc'.find('ab'))

    print('ac' in 'abc')
    print('abc'.find('ac'))

    print([1, 2] in [[1, 2], 'str'])
    print('apple' in {'orange': 1., 'banana': 2.3, 'apple': 5.2})


class Student():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        self._age = val

    def __eq__(self, val):
        print(self.__dict__)
        return self.__dict__ == val.__dict__


class Students(list):
    def __contains__(self, stu):
        for s in self:
            if s.name == stu.name:
                return True
            return False


def val_equarl():
    str1 = "alg_channel"
    str2 = "alg_channel"
    print(str1 == str2)

    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)

    c = [1, 3, 2]
    print(a == c)

    a = {'a': 1.0, 'b': 2.0}
    b = {'a': 1.0, 'b': 2.0}
    print(a == b)

    c = (1, 2)
    d = (1, 2)
    print(c == d)


if __name__ == '__main__':
    # is_equal()

    # in_fun()

    # s1 = Student('xiaoming')
    # s2 = Student('xiaohong')

    # a = Students()
    # a.extend([s1,s2])

    # s3 = Student('xiaoming')
    # print(s3 in a)

    # s4 = Student('xiaoli')
    # print(s4 in a)

    val_equarl()

    a = []
    xiaoming = Student('xiaoming',29)
    if xiaoming not in a:
        a.append(xiaoming)

    xiaohong = Student('xiaohong',30)
    if xiaohong not in a:
        a.append(xiaohong)

    xiaoming2 = Student('xiaoming',29)
    if xiaoming2 == xiaoming:
        print("对象完全一致，相等")

    if xiaoming2 not in a:
        a.append(xiaoming2)

    print(len(a))

    pass
