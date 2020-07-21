# _*_ coding: utf-8 _*_
"""
 @Time : 2020/7/21 12:50 
 @Author : yls 
 @Version：V 0.1
 @File : j_class_and_type_fun.py
 @desc : Python 查找变量的顺序遵守 LEGB 规则，即遇到某个变量时：
            1、优先从它所属的函数（local）内查找；
            2、若找不到，并且它位于一个内嵌函数中，就再到它的父函数（enclosing）中查找；
            3、如果还是找不到，再去全局作用域（global）查找；
            4、再找不到，最后去内置作用域（build-in）查找。
            5、若还是找不到，报错。
 """
# 全局作用域
a = 10


def parent():
    """
    作用域
    """
    # enclosing作用域
    b = 20

    def son():
        # c：局部作用域(local)
        c = 20
        # b：son位于一个内嵌函数中，b在son的父函数中(enclosing)
        print(b + c)
        # a：位于全局作用域(global)
        print(a + b + c)
        # min：位于内置作用域(build-in)
        print(min(a, b, c))

    son()


def type_function():
    """
    类型函数：
        bool([x])：测试一个对象是True，还是False。

        bytes([source[,encoding[,errors]]])：将一个字符串转换成字节类型。

        str(object='')：将字符类型、数值类型等转换为字符串类型。

        chr(i)：查看十进制整数对应的ASCII字符。

        ord(c)：查看某个ASCII字符对应的十进制数。

        dict()：class dict(**kwarg)
                class dict(mapping, **kwarg)
                class dict(iterable, **kwarg)
                创建数据字典。

        object()：返回一个根对象，它是所有类的基类。

        int(x)：int(x,base = 10),x可能为字符串或数值，将x转换为一个整数。
                base为转换的进制，十进制、十六进制等
                如果x不能转化为整数，则抛出ValueError异常。

        float(x)：将一个字符串或者整数转换为浮点数。

        frozenset([iterable])：创建一个不可修改的冻结集合，一旦创建不予许增删元素。

    Returns:

    """

    print("bool([0,0,0]) = %s" % str(bool([0, 0, 0])))
    print("bool([]) = %s " % str(bool([])))
    print("bool([0,1,1]) = %s " % str(bool([0, 1, 1])))
    print()

    print("bytes('apple',encoding='utf-8') = %s" % str(bytes("apple", encoding='utf-8')))
    print()

    print("str(100) = %s " % str(100))
    print()

    print("chr(65) = %s " % str(chr(65)))
    print()

    print("ord('A') = %d " % ord('A'))
    print()

    print("dict() = %s " % str(dict()))
    print("dict(a = 'a',b = 'b') = %s " % str(dict(a='a', b='b')))
    print("dict(zip(['a','b'],[1,2])) = %s " % str(dict(zip(['a', 'b'], [1, 2]))))
    print("dict([('a',1),('b',2)]) = %s " % str(dict([('a', 1), ('b', 2)])))
    print()

    o = object()
    print(o)
    print("type(o) = %s " % str(type(o)))
    print()

    print("int('12') = %d " % int('12'))
    print("int('12',16) = %d " % int('12', 16))
    try:
        print(int('we'))
    except Exception as e:
        print(e)
    print()

    print("float('30) = %f " % float('30'))


if __name__ == '__main__':
    # 作用域示例
    # parent()

    # 类型函数
    type_function()
    pass
