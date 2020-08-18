# _*_ coding: utf-8 _*_
"""
 #  @Time : 2020/8/18 8:38 
 #  @Author : yls 
 #  @Version：V 0.1
 #  @File : c_numpy_broadcast.py
 #  @desc : 广播，英文 broadcasting，有些读者是在使用 NumPy 时，
                从报错信息中第一次见到 broadcasting。
        广播规则：以上看到，不是任意 shape 的多个数组，操作时都能广播到一起，必须满足一定的约束条件。
            a、NumPy 首先会比较最靠右的维度，如果最靠右的维度相等或其中一个为 1，则认为此维度相等；
            b、那么，再继续向左比较，如果一直满足，则认为两者兼容；
            c、最后，分别在对应维度上发生广播，以此补齐直到维度一致。
 """

import numpy as np
import matplotlib.pyplot as plt


def numpy_test():
    """
    了解广播机制
    """
    v1 = np.arange(10).reshape(2, 5)
    print(v1)
    v2 = np.array([2])
    print(v2)
    v3 = v1 + v2
    print(v3)
    v2 = np.tile(2, (2, 5))
    print(v2)
    # ValueError: operands could not be broadcast together with shapes (2,5) (2,)
    v2 = np.array([1, 2])
    print(v2)
    v3 = v1 + v2
    print(v3)


def numpy_broadcast():
    """
    1、按照规则，从最右侧维度开始比较，数组 a, b 在此维度上的长度都为 3，相等；
    2、继续向左比较，a 在此维度上长度为 1，b 长度为 4，根据规则，也认为此维度是兼容的；
    3、继续比较，但是数组 b 已到维度终点，停止比较。
    结论，数组 a 和 b 兼容，通过广播能实现 shape 一致
    """
    a = np.arange(6).reshape(2, 1, 3)
    print("初始值a：")
    print(a)
    print()

    b = np.arange(12).reshape(4, 3)
    print("初始值b：")
    print(b)
    print()

    a = np.repeat(a, 4, axis=1)
    print("广播：")
    print(a)
    print()

    # 增加一个维度
    b = b[np.newaxis, :, :]
    # 在维度0上赋值2次
    b = np.repeat(b, 2, axis=0)
    print("广播后 a+b：")
    print(a + b)
    print()

    a = np.arange(6).reshape(2, 1, 3)
    b = np.arange(12).reshape(4, 3)
    print("原始值相加：")
    print(a + b)


def numpy_parctice():
    """
    1、返回有规律的数组：
        数组前半部分 1, 1, 1, 2, 2, 2, 3, 3, 3 通过 repeat 函数复制 3 次，后面部分通过 tile 函数复制 3 次
    """
    print("************************》1《*****************************")
    a = np.array([1, 2, 3])
    print("转换前：%s" % str(a))
    a = np.hstack((np.repeat(a, 3), np.tile(a, 3)))
    print("转换后：%s" % str(a))
    print()

    """
    2、Python 实现向量化：借助 NumPy 的 vectorize 实现操作向量化。
    原生的 Python 列表不支持向量化操作，两个列表相加默认不是逐个元素相加，
    借助 vectorize 能实现矢量相加。
    """
    print("************************》2《*****************************")
    a = [1, 2, 3, 4, 5, 6]
    b = [4, 5, 6, 7, 8, 9]
    print("原始值：a = %s" % str(a))
    print("原始值：a = %s" % str(a))
    print("默认相加：%s " % str(a + b))

    def add(x, y):
        return x + y

    addv = np.vectorize(add)
    print("利用vectorize实现矢量相加：%s " % str(addv(a, b)))
    print()

    """
    3、限制打印元素的个数：使用 set_printoptions 限制打印元素的个数：
    """
    print("************************》3《*****************************")
    np.set_printoptions(threshold=5)
    print(addv(a, b))

    """
    4、求中位数：使用 median 方法，因为 axis 为 1 的数组元素长度为 4，
            所以中位数为中间两个数的平均数。
    """
    print("************************》4《*****************************")
    a = np.array([[[4, 2, 4],
                   [8, 2, 7],
                   [5, 3, 6],
                   [3, 2, 3]],

                  [[2, 6, 1],
                   [5, 9, 8],
                   [9, 7, 1],
                   [2, 1, 1]]])
    ma = np.median(a, axis=1)
    print("沿 axis = 1 的中位数：\n %s " % str(ma))
    print()

    """
    5、计算 softmax 得分值：
        调用 softmax，得到每个元素的得分，因为 softmax 单调递增函数，所以输入值越大，得分值越高。
        sum(sm) 等于 1。
    """
    print("************************》5《*****************************")
    a = np.array([0.07810512, 0.12083313, 0.23554504, 0.62057901, 0.3437597,
                  0.10876455, 0.08338525, 0.28873765, 0.54033942, 0.71941148])

    def softmax(a):
        e_a = np.exp(a - np.max(a))
        return e_a / e_a.sum(axis=0)

    sm = softmax(a)
    print("计算 softmax 得分值：\nsm = %s " % str(sm))
    print("sm求和：sum(sm) = %s " % str(sum(sm)))
    print()

    """
    6、求任意分位数：使用 percentile 函数，q 为分位数列表
    """
    a = np.arange(11)
    print("原始值：a = %s " % str(a))
    print("求a的20分位数、80分位数：%s" % str(np.percentile(a, q=[20, 80])))
    print()

    """
    7、找到 NumPy 中缺失值：NumPy 使用 np.nan 标记缺失值，给定如下数组 a，求出缺失值的索引。
    """
    print("找到 NumPy 中缺失值：")
    a = np.array([0., 1., np.nan, 3., np.nan, np.nan, 6., 7., 8., 9.])
    b = np.where(np.isnan(a))
    print(b)
    print()

    """
    8、返回无缺失值的行：给定数组，找出没有任何缺失值的行
    """
    print("返回无缺失值的行：")
    a = np.array([[0., np.nan, 2., 3.],
                  [4., 5., np.nan, 7.],
                  [8., 9., 10., 11.],
                  [12., 13., np.nan, 15.],
                  [16., 17., np.nan, 19.],
                  [20., 21., 22., 23.]])
    m = np.sum(np.isnan(a), axis=1) == 0
    print(m)
    print(a[m])
    print()

    """
    9、求相关系数：
    """
    a = np.array([[2, 12, 21, 10],
                  [1, 20, 8, 22],
                  [7, 1, 5, 1],
                  [7, 10, 14, 14],
                  [12, 13, 13, 14],
                  [0, 12, 21, 2]])
    cor = np.corrcoef(a[:, 1], a[:, 2])
    print("相关系数：%s " % str(cor))

    """
    10、缺失值默认填充为 0
    """
    a = np.array([[0., np.nan, 2., 3.],
                  [4., 5., np.nan, 7.],
                  [8., 9., 10., 11.],
                  [12., 13., np.nan, 15.],
                  [16., 17., np.nan, 19.],
                  [20., 21., 22., 23.]])
    a[np.isnan(a)] = 0
    print(a)
    print()


# def numpy_fashion_mnist():
#     train_data = fashion_mnist_train.to_numpy()  # Pandas DataFrame 转 numpy 对象
#     row0 = train_data[0, :784].reshape(28, -1)
#     plt.imshow(row0)
#     plt.show()
#     for i in range(10):
#         print('图%d' % (i,))
#         plt.imshow(train_data[i, :784].reshape(28, -1))
#         plt.colorbar()
#         plt.show()


if __name__ == '__main__':
    # 了解广播机制
    # numpy_test()

    # 练习广播m
    # numpy_broadcast()

    # numpy 练习题
    # numpy_parctice()

    pass
