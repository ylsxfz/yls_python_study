# -*- coding: UTF-8 -*-
"""
#  @Time: 2020/08/08 09:27 
#  @Author: yls 
#  @Version: V 0.1
#  @File: g_iter_yield.py
#  @Desc: python应用迭代器和生成器的9个案例
        1、迭代器：遍历迭代器，表头位置相应改变；next函数执行一次，迭代对象指向就前进一次；
                StopIteration触发时，意味着已到迭代器的尾部。
        2、生成器：带yield的函数是生成器，而生成器也是一种迭代器。所以生成器也有上面那些迭代器的特点。

        案例使用：
            （1）拼接迭代器 ==》chain(*iterables)：
                a：chain 函数实现元素拼接，原型如下，参数 * 表示可变的参数
                b：它有些 join 串联字符串的感觉，join 只是一次串联一个序列对象。而 chain 能串联多个可迭代对象，形成一个更大的可迭代对象。
                c：chain 是一个生成器函数，在迭代时，每次吐出一个元素，所以做到最高效的节省内存。

            （2）累积迭代器 ==》accumulate(iterable[, func, *, initial=None])：
                注意：1、如果 func 不提供，默认求累积和。
                     2、如果 func 提供，func 的参数个数要求为 2，根据 func 的行为返回结果。
                a：包装 iterable 为迭代器；
                b：初始值 initial 很重要；
                . 如果它的初始值为 None，迭代器向前移动求出下一个元素，并赋值给 total，然后 yield；
                . 如果初始值被赋值，直接 yield。
                a：此时迭代器 it 已经指向 iterable 的第二个元素，遍历迭代器 it，func(total, element) 后，
                    求出 total 的第二个取值，yield 后，得到返回结果的第二个元素。
                b：直到 it 迭代结束。

            （3）漏斗迭代器==》compress(data,selectors):
                    功能类似漏斗，经过selectors过滤后，返回一个更小的迭代器。

            （4）drop迭代器==》dropwhile(predicate,iterable):
                    扫描可迭代对象 iterable，从不满足条件处往后全部保留，返回一个更小的迭代器。
                    .iterable 包装为迭代器
                    .迭代 iterable
                        （1）如果不满足条件 predicate，yield x，然后跳出迭代，迭代完 iterable 剩余所有元素。
                        （2）如果满足条件 predicate，就继续迭代，如果所有都满足，则返回空的迭代器。

            （5）take迭代器==》takewhile(predicate,iterable):
                     扫描列表，只要满足条件就从可迭代对象中返回元素，直到不满足条件为止。
                     .遍历 iterable
                        a、符合条件 predicate，yield x
                        b、否则跳出循环

            （6）克隆迭代器==》tee(iterable,n=2):
                    实现对原迭代器的复制。

            （7）复制元素==》repeat(object[,times]):
                    repeat实现复制元素n次。

            （8）笛卡尔积==》product(A,B): ((x,y) for x in A for y in B)

            （9）加强版zip==》zip_longest(A,B,fillvalue):
                    若可迭代对象的长度未对齐，将根据fillvalue填充缺失值，返回结果的长度等于更长的序列长度。




"""
from collections.abc import Iterator
from itertools import *


def iter_example():
    """
    1、列表不论遍历多少次，表头的位置始终是第一个元素；
    2、迭代器遍历结束后，不再指向原来的表头位置，而是为最后元素的下一个位置。
    3、只有迭代器对象才能与内置函数next结合使用，next一次，迭代器就前进一次，指向一个新的元素。
    4、我们不可以用len来获取迭代器的长度，只能迭代到最后一个末尾元素时，才知道其长度。
    """

    a = [1, 2, 34, 34, 335]
    a_iter = iter(a)
    print(a_iter)
    print(a_iter.__next__())
    print(next(a_iter))

    flag = isinstance(a_iter, Iterator)
    print(flag)

    print("***********************")
    for i in a:
        print(i)
    print("***********************")
    for i in a_iter:
        print(i)
    print("***********************")
    b_iter = iter(a)
    iter_len = 0
    try:
        while True:
            i = next(b_iter)
            print(i)
            iter_len += 1
    except StopIteration:
        print('iterator stops')
    print('length of iterator is %d' % (iter_len,))


def not_yield_accumulate_div(a):
    """
    不使用生成器
    Args:
        a: 列表
    """
    if a is None or len(a) == 0:
        return []
    rtn = [a[0]]
    for i in a[1:]:
        rtn.append(i * rtn[-1])
    return rtn


def yield_accumulate_div(a):
    """
    使用生成器
    Args:
        a: 列表
    """
    if a is None or len(a) == 0:
        return []
    it = iter(a)
    total = next(it)
    yield total
    for i in it:
        total = total * i
        yield total


def itertools_example():
    """
    拼接迭代器
    """
    print("******************拼接迭代器**********************")
    chain_iterator = chain(['I', 'love'], ['python'], ['very', 'much'])
    for i in chain_iterator:
        print(i)
    print(isinstance(chain_iterator, Iterator))
    print()

    """
    累积迭代器
    """
    print("******************累积迭代器**********************")
    acc_iterator = accumulate([1, 2, 3, 4, 5, 6])
    for i in acc_iterator:
        print(i)
    print()

    print("func提供，参数个数为2，根据func的行为返回结果：")
    acc_iterator = accumulate([1, 2, 3, 4, 5, 6], lambda x, y: x * y)
    for i in acc_iterator:
        print(i)
    print()

    """
    漏斗迭代器
    """
    print("******************漏斗迭代器**********************")
    compress_itor = compress('abcdef', [1, 1, 0, 1])
    for i in compress_itor:
        print(i)
    print()

    """
    drop迭代器
    """
    print("******************drop迭代器**********************")
    drop_itor = dropwhile(lambda x: x < 3, [1, 0, 2, 41, 23, 23, 5, 5, 67, -3])
    for i in drop_itor:
        print(i)
    print()

    """
    take迭代器
    """
    print("******************take迭代器**********************")
    take_itor = takewhile(lambda x: x < 3, [1, 0, 2, 41, 23, 23, 5, 5, 67, -3])
    for i in take_itor:
        print(i)
    print()

    """
    tee迭代器
    """
    print("******************tee迭代器**********************")
    a = tee([1, 2, 3, 4, 2, 4, 5], 2)
    for i in a[0]:
        print(i)
    print("克隆的迭代器：")
    for i in a[1]:
        print(i)
    print()

    """
    repeat复制元素
    """
    print("******************repeat复制元素**********************")
    lst = list(repeat(6, 3))
    print(lst)

    lst = list(repeat([12, 321, 4, 11], 3))
    print(lst)
    print()

    """
    笛卡尔积：product
    """
    print("******************笛卡尔积：product**********************")
    lst = list(product('ABCD','xy'))
    print(lst)
    print()

    """
    加强版zip
    """
    print("******************加强版zip**********************")
    lst = list(zip_longest('ABCD','xy',fillvalue='-'))
    print(lst)


if __name__ == '__main__':
    # 迭代器
    # iter_example()

    # 生成器
    # rtn = not_yield_accumulate_div([1, 2, 3, 4, 5, 6])
    # print(rtn)
    # rtn = list(yield_accumulate_div([1, 2, 3, 4, 5, 6]))
    # print(rtn)

    # 拼接迭代器
    itertools_example()

    pass
