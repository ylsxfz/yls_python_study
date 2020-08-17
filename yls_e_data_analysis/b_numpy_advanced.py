# _*_ coding: utf-8 _*_
"""
 #  @Time : 2020/8/17 14:11 
 #  @Author : yls 
 #  @Version：V 0.1
 #  @File : b_numpy_advanced.py
 #  @desc :
    ，你应该完全理解 reshape 操作后的魔法：
        1、buffer 是个一维数组，永远不变；
        2、变化的 shape 通过 view 传达；
        3、取值仅有 0 的轴为自由轴，它能变化出任意维度。
        4、reshape 后的数组，仅仅是原来数组的视图 view，并没有发生复制元素的行为，这样才能保证 reshape 操作更为高效。
 """
import numpy as np
from numpy import linalg


def numpy_base():
    """
    如果 v2 是 v1 的视图，那么 v1 也会改变，如下，
    v1 的第一个元素也发生相应改变，所以得证。
    """
    a = np.arange(0, 24, 2)
    print("原数组：")
    print(a)
    print()

    print("dtype：")
    print(a.dtype)
    print()

    print("flags：")
    print(a.flags)
    print()

    print("一维数组转二维：")
    b = a.reshape(2, 6)
    print(b)
    print()

    print("一维数组转三维：")
    c = a.reshape(2, 3, 2)
    print(c)
    print()


def numpy_high_frequency():
    """
    NumPy 中两个数组加减乘除等，默认都是对应元素的操作
    """
    # 创建一维数组
    v1 = np.arange(5)
    print("一维数组：")
    print(v1)
    print()

    print("执行 v1+2 操作，按照元素顺序逐个加 2：")
    v2 = v1 + 2
    print(v2)
    print()

    print("执行 v1 * v1，注意是按照元素逐个相乘：")
    v3 = v1 * v1
    print(v3)
    print()


def numpy_matrix_operation():
    """
    矩阵运算：
        乘法：使用 dot 函数，另一种是转化为 matrix 对象。

    """
    # 数值[1,10)内，生成shape为(5,2)的随机整数数组
    v1 = np.arange(5)
    v2 = np.random.randint(1, 10, (5, 2))
    v3 = np.dot(v1, v2)
    print("1.1、矩阵乘法==》dot函数")
    print(v3)
    print()

    print("1.2、矩阵乘法==》转化为 matrix 对象")
    v3 = np.matrix(v1) * np.matrix(v2)
    print(v3)
    print()

    print("行列式：")
    v1 = np.arange(12)
    v2 = v1.reshape(3, 2, 2)
    v3 = linalg.det(v2)
    print(v3)

    v3 = np.arange(9).reshape(3, 3)
    v3 = linalg.det(v3)
    print(v3)


def numpy_statistical_variables():
    """
    统计变量
    """
    m1 = np.random.randint(1, 10, (3, 4))
    print("原数组：")
    print(m1)
    print()

    print("mean()：求平均值：")
    print(m1.mean())
    print()

    print("m1.sum()/size：求平均值：")
    print(m1.sum() / 12)
    print()

    print("axis参数：求某一维度的平均值：")
    print(m1.mean(axis=1))
    print()

    print("m1.std()：标准差：")
    print(m1.std())
    print()

    print("m1.std(axis=1)：一维上的标准差：")
    print(m1.std(axis=1))
    print()

    print("m1.max()：最大值：")
    print(m1.max())
    print()

    print("m1.max(axis=1)：一维上的最大值：")
    print(m1.max(axis=1))
    print()

    print("m1.min()：最小值：")
    print(m1.min())
    print()

    print("m1.min(axis=1)：一维上的最小值：")
    print(m1.min(axis=1))
    print()

    print("m1.sum()：求和：")
    print(m1.sum())
    print()

    print("m1.sum(axis=1)：一维上的求和：")
    print(m1.sum(axis=1))
    print()

    print("m1.cumprod()：求所有维度上元素的累乘：")
    print(m1.cumprod())
    print()

    print("m1.cumprod(axis=1)：某一维度上的累乘：")
    print(m1.cumprod(axis=1))
    print()

    print("m1.cumsum()：求所有维度上元素的累加和：")
    print(m1.cumsum())
    print()

    print("m1.cumsum(axis=1)：某一维度上的累加和：")
    print(m1.cumsum(axis=1))
    print()

    print("m1.trace()：求迹（对角线上元素的和）：")
    print(m1.trace())
    print()


def numpy_change_arr():
    """
    flatten：NumPy 的 flatten 函数也有改变 shape 的能力，它将高维数组变为向量。但是，它会发生数组复制行为。
    newaxis： 增加一个维度，维度的索引只有 0。
    repeat：实现某一维上的元素复制操作。
    tile：实现按块复制元素。
    vstack，vertical stack：沿竖直方向合并多个数组。
    hstack：沿水平方向合并多个数组。
    concatenate：指定在哪个维度上合作数组.
    NumPy 还有一些小 track，比如 r_ 类、c_ 类，也能实现合并操作。
    值得注意，不管是 vstack，还是 hstack，沿着合并方向的维度，其元素的长度要一致。

    argmax 返回数组中某个维度的最大值索引，当未指明维度时，返回 buffer 中最大值索引.
    argmin 返回数组中某个维度的最小值索引，当未指明维度时，返回 buffer 中最小值索引.
    """
    v1 = np.random.randint(1, 10, (2, 3))
    print("原数组：")
    print(v1)
    print()

    print("flatten()函数：")
    v2 = v1.flatten()
    print(v2)
    print()

    print("newaxis 增加一个维度，维度的索引只有 0，本篇的开头已经详细解释过，不再赘述。")
    v1 = np.arange(10)
    print(v1)
    v2 = v1[:, np.newaxis]
    print(v2)
    print()

    v1 = np.array([[1, 2], [3, 4]])
    print("源数组：")
    print(v1)
    print("repeat 操作，实现某一维上的元素复制操作：")
    print("axis=0：")
    v2 = np.repeat(v1, 2, axis=0)
    print(v2)
    print("axis=1：")
    v2 = np.repeat(v1, 2, axis=1)
    print(v2)
    print()

    print("tile 实现按块复制元素：np.tile(v1,3)")
    print(np.tile(v1, 3))
    print()
    print("tile 实现按块复制元素：np.tile(v1,(2,3))")
    print(np.tile(v1, (2, 3)))
    print()

    print("vstack，vertical stack，沿竖直方向合并多个数组：")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[-1, -2]])
    print(np.vstack((a, b)))
    print()

    print("hstack 沿水平方向合并多个数组：")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6, 7], [8, 9, 10]])
    c = np.hstack((a, b))
    print(c)
    print()

    print("concatenate 指定在哪个维度上合作数组：axis=0")
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[-1, -2]])
    print(np.concatenate((a, b), axis=0))
    print()
    print("concatenate 指定在哪个维度上合作数组：axis=1")
    c = np.array([[5, 6, 7], [8, 9, 10]])
    print(np.concatenate((a, c), axis=1))

    print("NumPy 还有一些小 track，比如 r_ 类、c_ 类，也能实现合并操作：")
    print("c_：")
    print(np.c_[a, c])
    print("r_：")
    print(np.r_[a, c[:, :2]])
    print()

    a = np.random.randint(1,10,(2,3))
    print("a：")
    print(a)
    print("a.argmax()：")
    print(a.argmax())
    print(a.argmax(axis=0))
    print(a.argmax(axis=1))
    print()

    print("a.argmin()：")
    print(a.argmin())
    print(a.argmin(axis=0))
    print(a.argmin(axis=1))
    print()


if __name__ == '__main__':
    # 揭秘 Shape
    # numpy_base()

    # 熟悉NumPy中高频使用的方法
    # numpy_high_frequency()

    # 矩阵运算
    # numpy_matrix_operation()

    # 统计变量
    # numpy_statistical_variables()

    # 改变数组
    numpy_change_arr()
    pass
