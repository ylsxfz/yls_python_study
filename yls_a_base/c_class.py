# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/7/19  15:43
#  @Author: yls
#  @Version: V 0.1
#  @File: c_class.py
#  @Desc:
"""


class Dog(object):
    """
    Python 使用关键字 class 定制自己的类，self 表示类实例对象本身。
    一个自定义类内包括属性、方法，其中有些方法是自带的。
    __init__：方法能定义一个带参数的类；
    __new__：方法自定义实例化类的行为；
    __getattribute__：方法自定义读取属性的行为；
    __setattr__：自定义赋值与修改属性时的行为。
    """

    def __init__(self, name, dtype):
        """
        类的属性：通过 __init__，定义 Dog 对象的两个属性：name、dtype。
        方法前加 2 个 _ 后，方法变为“私有方法”，只能在 Dog 类内被共享使用。
        Args:
            name: 属性姓名
            dtype: 属性类型
        """
        self.__name = name
        self.__dtype = dtype

    def get_name(self):
        """
        属性 name 不能被访问了，
        也就无法得知 wangwang 的名字叫啥。不
        过，这个问题有一种简单的解决方法，直接新定义一个方法就行：
        """
        return self.__name

    @property
    def name(self):
        """
        使用 @property 装饰后 name 变为属性，意味着 .
        name 就会返回这本书的名字，而不是通过 .name() 这种函数调用的方法。
        这样变为真正的属性后，可读性更好。
        """
        return self.__name

    @name.setter
    def name(self,new_name):
        """
        如果使 name 既可读又可写，就再增加一个装饰器 @name.setter。
        Args:
            new_name: 修改的值
        """
        self.__name = new_name

    def shout(self):
        print("You're %s,type: %s" % (self.name, self.dtype))


if __name__ == '__main__':
    # wangwang是Dog类的实例
    wangwang = Dog("dog", "二哈")

    # Dog 类现在没有定义任何方法，但是刚才说了，
    # 它会有自带的方法，使用 __dir__() 查看这些自带方法：
    print(wangwang.__dir__())
    wangwang.shout()
    pass
