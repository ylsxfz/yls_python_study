# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/09 16:20 
#  @Author: yls 
#  @Version: V 0.1
#  @File: i_collection.py
#  @Desc: Python 最被低估的模块 collections 3 个常用类总结及案例解读
        1、NamedTuple：对于数据分析或机器学习领域，用好 NamedTuples 会写出可读性更强、更易于维护的代码。
               注意： NamedTuple 优点明显，但是同样缺点也较为明显，一个 NamedTuple 创建后，
                    它的属性取值不允许被修改，也就是属性只能是可读的。

        2、Counter：主要功能就是计数。我们在分析数据时，基本都会涉及计数，真的家常便饭。

        3、DefaultDict：DefaultDict 能自动创建一个被初始化的字典，也就是每个键都已经被访问过一次。
"""
from collections import namedtuple, Counter, defaultdict


def namedtuple_example():
    Person = namedtuple('Person', ['id', 'age', 'height', 'name', 'address',
                                   'province', 'city', 'town', 'country', 'birth_address',
                                   'father_name', 'monther_name', 'telephone', 'emergency_telephone'])
    a = [''] * 11
    b = Person(3, 19, 'xiaoming', *a)
    print(b)

    def update_persons_info(old_data, new_data):
        changed_list = []
        for line in new_data:
            new_props = line.split()
            new_person = Person(new_props)
            for old in old_data:
                old_props = old.split()
                old_person = Person(old_props)
                if old_person.id != new_person.id:
                    changed_list.append(old_person.id)
                elif old_person.address != new_person.address:
                    changed_list.append(old_person.address)
                elif old_person.birth_address != new_person.birth_address:
                    changed_list.append(old_person.birth_address)
        return changed_list

    # 改行会报错：AttributeError: can't set attribute
    # b.age = 20


def counter_example():
    sku_purchase = [3, 8, 3, 10, 3, 3, 1, 3, 7, 6, 1, 2, 7, 0, 7, 9, 1, 5, 1, 0]
    count = Counter(sku_purchase).most_common()
    print(count)

    count = Counter('i love python so much').most_common()
    print(count)


def defaultDict_example():
    d = defaultdict(int)
    print(d)
    d = defaultdict(list)
    print(d)
    d = defaultdict(list, {})
    print(d)

    d = defaultdict(list)
    s = 'from collections import defaultdict'
    for index, i in enumerate(s):
        d[i].append(index)
    print(d)

    """
    排序词（permutation）：两个字符串含有相同字符，但字符顺序不同。
    """
    def is_permutation(str1,str2):
        if str1 is None or str2 is None:
            return False
        if len(str1) != len(str2):
            return False
        unq_s1 = defaultdict(int)
        unq_s2 = defaultdict(int)
        for c1 in str1:
            unq_s1[c1] += 1
        for c2 in str2:
            unq_s2[c2] += 1
        return unq_s1 == unq_s2

    r = is_permutation('nice','cine')
    print(r)

    r = is_permutation('','')
    print(r)

    r = is_permutation('',None)
    print(r)

    r = is_permutation('work','woo')
    print(r)


if __name__ == '__main__':
    # namedtuple_example()
    # counter_example()
    defaultDict_example()
    pass
