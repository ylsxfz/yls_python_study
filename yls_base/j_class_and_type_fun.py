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
from collections.abc import Iterable

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


class Student():
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        self._age = None
        self._sortname = None

    def instance_method(self):
        print("这是实例方法")
        return self

    @classmethod
    def __annotations__(cls):
        return "学生类"

    def __toString__(self):
        return "id: %d " % self.id + "，name：%s " % self.name

    @classmethod
    def print_type_name(cls):
        print("这是类上的方法，类名为 %s,注解为 %s " % (cls.__name__, cls.__annotations__()))

    def get_age(self):
        return self._age

    def set_age(self, val):
        self._age = val

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age, 'name property')

    @property
    def sortname(self):
        return self._sortname

    @sortname.setter
    def sortname(self, val):
        self._sortname = val

    @sortname.deleter
    def sortname(self):
        del self._sortname


class Undergraduate(Student):
    def studyClass(self):
        pass

    def attendActivity(self):
        pass

class Parent():
    def __init__(self,x):
        self.v = x

    def add(self,x):
        return self.v + x

class Son(Parent):
    def add(self,y):
        # 直接调用父类的add方法
        r = super().add(y)
        # 子类的add与父类相比，能实现对结果的打印功能
        print(r)


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

        list([iterable])：返回可变序列类型：列表。

        range(stop)：生成不可变序列
        range(start,stop[,step])：生成不可变序列

        set([iterable])：返回一个集合对象，并允许创建后再增加、删除元素。

        slice(stop)：返回一个由range(start,stop,step)所指定索引集的slice对象。
        slice(start,stop[,step])：返回一个由range(start,stop,step)所指定索引集的slice对象。

        tuple([iterable])：创建一个不可修改的元组对象。

        type(object)：查看对象类型
        type(name,bases,dict)：查看对象类型

        zip(*iterables)：创建一个迭代器，聚合每个可以迭代对象的元素。
                参数前带 *，意味着是可变序列参数，可传入 1 个，2 个或多个参数。

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
    print()

    print("frozenset([1, 1, 1, 23, 4, 55, 2]) = %s " % str(frozenset([1, 1, 1, 23, 4, 55, 2])))
    print()

    print("list({1,2,3,4,5}) = %s " % str(list({1, 2, 3, 4, 5})))
    lst = list(map(lambda i: str(i), [186, 1243, 3201]))
    print(lst)
    lst = list(map(lambda x: x % 2 == 1, [1, 34, 23, 25, 235]))
    print(lst)
    print()

    #  只有一个参数，默认初始值为 0，步长为 1
    print("range(11) = %s" % str(range(11)))
    # 三个参数都提供，分别是开始、终止、步长值
    print("range(0,11,1) = %s" % str(range(0, 11, 1)))
    print()

    print("set([1, 23, 24, 234, 2, 52, 52, 52, 23]) = %s" % str(set([1, 23, 24, 234, 2, 52, 52, 52, 23])))
    print()

    a = [1, 4, 2, 3, 1]
    print("a = %s " % str(a))
    # 等价于a[0:5:2]
    print("a[slice(0, 5, 2)] = %s " % str(a[slice(0, 5, 2)]))
    print("a[slice(2)] = %s " % str(a[slice(2)]))
    print()

    print("tuple(range(10)) = %s" % str(tuple(range(10))))
    print()

    xiaoming = Student()
    print("type(xiaoming) = %s" % str(type(xiaoming)))
    print("type([1, 4, 2, 3, 1]) = %s" % str(type([1, 4, 2, 3, 1])))
    print()

    for i in zip([1, 2]):
        print(i)
    a = range(5)
    print("a = %s " % str(a))
    b = list('abcde')
    print("b = %s " % str(b))
    print("[str(y) + str(x) for x,y in zip(a,b)] = %s " % str([str(y) + str(x) for x, y in zip(a, b)]))



def calss_object_properties():
    """
    类对象及属性：
        classmethod：该修饰符对应的函数不需要实例化，不需要self参数。
            第一个参数需要表示自身类的cls参数，能调用类的属性、方法、实例等。

        delattr(object,name)：删除对象的属性，在不需要某个或某些属性是，这个方法就会很有用。

        dir([object])：不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时返回参数的属性、方法列表

        getattr(object,name[,default])：获取对象的属性。

        hasattr(object, name)；判断对象是否包含某个属性。

        isinstance(object,classinfo)：判断object是否为类classinfo的实例，若是，返回true。

        issubclass(class,classinfo)：如果class时classinfo的子类，返回True。
                classinfo取值也可能为元组，若class时元组内某个元素类型的子类，也会返回True。

        property(fget=None,fset=None,fdel=None,doc=None)：返回property属性。不适用装饰器，定义类上的属性。

        supper([type,[,object-or-type]])：返回一个代理对象，它会将方法调用委托给type的父类或者兄弟类。

        callable(object)：判断对象是否可被调用，能被调用的对象就是一个callable对象，比如函数str、int等都可被调用的。

    """

    Student().print_type_name()
    Student().instance_method()

    xiaoming = Student(1, 'xiaoming')
    print(xiaoming.__toString__())
    print(hasattr(xiaoming, 'id'))
    delattr(xiaoming, 'id')
    print(hasattr(xiaoming, 'id'))
    print()

    print(dir())
    print(dir(xiaoming))
    print()

    print(getattr(xiaoming, 'name'))
    print()

    print("isinstance(xiaoming,Student) = %s " % str(isinstance(xiaoming, Student)))
    print()

    print("isinstance([1,2,3],Iterable) = %s" % str(isinstance([1, 2, 3], Iterable)))
    print()

    print("issubclass(Undergraduate,Student) = %s" % str(issubclass(Undergraduate, Student)))
    print("issubclass(object,Student) = %s" % str(issubclass(object, Student)))
    print("issubclass(Student,object) = %s" % str(issubclass(Student, object)))

    print("issubclass(int,(int,float)= %s " % str(issubclass(int, (int, float))))

    xiaoming.age = 12
    print(xiaoming.age)

    Son(1).add(2)

    print("callable(int) = %s " % str(callable(int)))
    print("callable(str) = %s" % str(callable(str)))
    print("callable(xiaoming) = %s " % str(callable(xiaoming)))

if __name__ == '__main__':
    # 作用域示例
    # parent()

    # 类型函数
    # type_function()

    # 类对象和属性
    calss_object_properties()
    pass
