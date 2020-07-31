# _*_ coding: utf-8 _*_
"""
#  @Time : 2020/7/20 10:09
#  @Author : yls
#  @Version：V 0.1
#  @File : f_list_tuple.py
#  @desc : list(列表) 和 tuple(元组) 的常用实例
"""

from random import randint, sample, shuffle, uniform
from pyecharts.charts import Scatter
import pyecharts.options as opts


def list_is_duplicated(lst):
    """
    判断list内有无重复元素
    Args:
        lst: lst列表数据

    Returns:
        is_duplicated，使用 list 封装的 count 方法，
        依次判断每个元素 x 在 list 内的出现次数。
        如果大于 1，则立即返回 True，表示有重复。
        如果完成遍历后，函数没返回，表明 list 内没有重复元素，返回 False。
    """
    for x in lst:
        # 判断 x 元素在 lst 中出现的次数
        if lst.count(x) > 1:
            return True
    return False


def list_reverse(lst):
    """
    列表反转： 一行代码实现列表反转
        1：[::-1]，这是切片的操作。
        2：[::-1] 生成逆向索引（负号表示逆向），步长为 1 的切片。
    Args:
        lst: 列表

    Returns:
        反转后的列表数据
    """
    return lst[::-1]


def list_find_duplicate(lst):
    """
    找出列表中的所有重复的元素
    Args:
        lst: 列表

    Returns:
        ret: 返回重复元素的列表
    """
    ret = []
    for x in lst:
        if lst.count(x) > 1:
            ret.append(x)
    return ret


def list_fibonacci_sequence(n):
    """
    斐波那契数列：第一、二个元素的值都为1，第三个元素等于前两个元素和，依次类推
    Returns:
        fib: 返回数列
    """
    if n <= 1:
        return [1]
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    return fib


def list_fibonacci_sequence_yield(n):
    """
    遇到 yield 返回，下次再进入函数体时，从 yield 的下一句开始执行。
    Args:
        n: 需要生成多少个数列
    """
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def list_mode_one(lst):
    """
    max 函数是 Python 的内置函数，所以使用它无需 import。
    max 有一个 key 参数，指定如何进行值得比较。
    该方法只能返回一个元素。
    Args:
        lst: 列表

    Returns:
        返回出现频次最多的元素
    """
    if not lst:
        return None
    # v 在 lst 的出现次数作为大小比较的依据
    return max(lst, key=lambda v: lst.count(v))


def list_mode_two(lst):
    """
    max 函数是 Python 的内置函数，所以使用它无需 import。
    max 有一个 key 参数，指定如何进行值得比较。
    该方法可以将出现频次最多的元素全部返回
    Args:
        lst: 列表

    Returns:
        返回所有出现频次最多的元素
    """
    if not lst:
        return None
    max_freq_elem = max(lst, key=lambda v: lst.count(v))
    max_freq = lst.count(max_freq_elem)
    # 统计出现频次最多的元素
    ret = []
    for i in lst:
        if i not in ret and lst.count(i) == max_freq:
            ret.append(i)
    return ret


def list_max_len(*lists):
    """
    带有一个 * 的参数为可变的位置参数，意味着能传入任意多个位置参数。
    key 函数定义怎么比较大小：lambda 的参数 v 是 lists 中的一个元素。
    Args:
        *lists:

    Returns:
        返回长度最长的列表
    """
    # v 代表一个 list，其长度作为大小比较的依据
    max_len_list = max(*lists, key=lambda v: len(v))
    max_len = len(max_len_list)
    # 获取等于最长长度的所有列表
    ret = []
    for i in lists:
        if len(i) == max_len:
            ret.append(i)
    return ret


def list_head(lst):
    """
    列表的表头
    Args:
        lst: 列表

    Returns:
        返回列表的表头
    """
    return lst[0] if len(lst) > 0 else None


def list_tail(lst):
    """
    列表的表尾
    Args:
        lst: 列表

    Returns:
        返回列表的表尾
    """
    return lst[-1] if len(lst) > 0 else None;


def list_mul_table():
    """
    九九乘法表
    """
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(str(j) + str("*") + str(i) + "=" + str(i * j), end="\t")
        print()


def list_pair(lst):
    """
    t[:-1]：原列表切掉最后一个元素；
    t[1:]：原列表切掉第一个元素；
    zip(iter1, iter2)：实现 iter1 和 iter2 的对应索引处的元素拼接。
    Args:
        lst: 列表

    Returns:
        返回生成的元素对
    """
    # 生成相邻元素对
    return list(zip(lst[:-1], lst[1:]))


def list_random_sample():
    """
    样本抽样：
        首先，使用列表生成式，创建长度为 100 的列表 lst；
        然后，sample 抽样 10 个样本
    """
    lst = [randint(0, 50) for _ in range(100)]
    print("抽取前5个元素：" + str(lst[:5]))
    lst_sample = sample(lst, 10)
    print("样本抽样：" + str(lst_sample))


def list_shuffle():
    """
    内置random中的shuffle函数,能够重洗数据。
    值得注意：shuffle是对输入列表就地（in place）洗牌，节省存储空间
    Returns:

    """
    lst = [randint(0, 50) for _ in range(100)]
    print("抽取前5个元素：" + str(lst[:5]))
    # 重洗数据
    shuffle(lst)
    print("重洗数据集后，抽取前5个元素：" + str(lst[:5]))


def list_uniform():
    """
    random模块，uniform(a,b)生成[a,b]内的一个随机数
    round(x,n)：方法返回浮点数x的四舍五入值。
            x -- 数值表达式。
            n -- 数值表达式，表示从小数点位数。
    Returns:

    """
    x, y = [i for i in range(100)], \
           [round(uniform(0, 10), 2) for _ in range(100)]
    c = (
        Scatter()
            .add_xaxis(x)
            .add_yaxis('y', y)
    )
    c.render()


if __name__ == '__main__':
    a = [1, -2, 3, 4, 1, 2, 1, 2, 3, 3, 2]
    print(str(a) + "内有无重复元素：" + str(list_is_duplicated(a)))

    lst3 = list_reverse(a)
    print(str(a) + "反转后：" + str(lst3))

    lst4 = list_find_duplicate(a)
    print(str(a) + "重复元素：" + str(lst4))

    lst5 = list_fibonacci_sequence(10)
    print("斐波那数列：" + str(lst5))

    lst6 = list(list_fibonacci_sequence_yield(10))
    print("斐波那数列（yield生成器）：" + str(lst6))

    print(str(a) + "中出现频次最多的元素是(只能输出一个元素)：" + str(list_mode_one(a)))
    print(str(a) + "中出现频次最多的元素是：" + str(list_mode_two(a)))

    r = list_max_len([1, 2, 3], [1, 2], [1, 2, 3, 4], [4, 5, 6, 7])
    print("更长的列表：" + str(r))

    print(str(a) + "的表头：" + str(list_head(a)))
    print(str(a) + "的表头：" + str(list_tail(a)))

    print("九九乘法表：")
    list_mul_table()

    print(str(a) + "的相邻元素对：" + str(list_pair(a)))

    # 样本抽样
    list_random_sample()

    # 重洗数据集
    list_shuffle()

    # 均匀生成坐标点
    list_uniform()
    pass
