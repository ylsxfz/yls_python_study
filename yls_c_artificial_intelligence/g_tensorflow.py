# _*_ coding: utf-8 _*_
# -------------------------------------------------------------------------------
#  @Time : 2020/7/24 13:07
#  @Author : yls
#  @Version：V 0.1
#  @File : g_tensorflow.py
#  @desc :TensorFlow 由 Google 与 Brain Team 合作开发，
#         是一个采用数据流图（data flow graphs），用于数值计算的开源软件库。
#         节点（Nodes）在图中表示数学操作，
#         图中的线（edges）则表示在节点间相互联系的多维数据数组，即张量（tensor）。
#         详情参考：
#             http://www.tensorfly.cn/
# -------------------------------------------------------------------------------
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def test_tensorflow():
    sess = tf.Session()

    a = tf.constant(10)

    b = tf.constant(12)

    c = sess.run(a + b)

    print(c)


if __name__ == '__main__':
    test_tensorflow()
    pass
