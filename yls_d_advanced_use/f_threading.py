# _*_ coding: utf-8 _*_
"""
 #  @Time : 2020/8/3 16:25 
 #  @Author : yls 
 #  @Version：V 0.1
 #  @File : f_threading.py
 #  @desc : python多线程和协程6个方面使用逻辑
        高效的协程：
            在同一个线程中，如果发生以下事情：
                A 函数执行时被中断，传递一些数据给 B 函数；
                B 函数拿到这些数据后开始执行，执行一段时间后，发送一些数据到 A 函数；
                就这样交替执行……
                这种执行调用模式，被称为协程
 """

import threading
import time
import threading


def threading_test():
    t = threading.current_thread()
    print(t)
    # 获取线程名字
    print(t.getName())
    # 线程id
    print(t.ident)
    # 判断线程是否存活
    print(t.isAlive())

    # 创建一个线程
    my_thread = threading.Thread()
    # 创建一个名称为my_thread的线程
    my_thread = threading.Thread(name="my_thread")


def print_i(i):
    print('打印i：%d' % (i,))


def print_time():
    """
    交替获得CPU时间片
    """
    # 在每个线程中打印5次
    for _ in range(5):
        # 模拟打印前的相关处理逻辑
        time.sleep(0.1)
        print('当前线程%s，打印结束时间为：%s'
              % (threading.current_thread().getName(), time.time()))


a = 0


def add1():
    """
    线程不安全，抢夺全局变量
    不推荐该方式
    """
    global a
    temp = a + 1
    time.sleep(0.2)
    a = temp
    print('%s adds a to 1: %d' % (threading.current_thread().getName(), a))


locka = threading.Lock()


def add2():
    """
    当程序中只有一把锁，通过 try...finally 还能确保不发生死锁。但是，当程序中启用多把锁，很容易发生死锁。
    不推荐该方式
    """
    global a
    try:
        # 获得锁
        locka.acquire()
        tmp = a + 1
        time.sleep(6)
        a = tmp
    finally:
        # 解放锁
        locka.release()
        print('%s adds a to 1: %d' % (threading.current_thread().getName(), a))



def A():
    a_list = ['1','2','3']
    for to_b in a_list:
        from_b = yield to_b
        print('receive %s from B'%(from_b,))
        print('do some complex process for A during 200ms ')

def B(a):
    from_a = a.send(None)
    print('response %s from A '%(from_a,))
    print('B is analysising data from A')
    b_list = ['x','y','z']
    try:
        for to_a in b_list:
            from_a = a.send(to_a)
            print('response %s from A ' % (from_a,))
            print('B is analysising data from A')
    except StopIteration:
        print('----from a done----')
    finally:
        a.close()

if __name__ == '__main__':
    # threading_test()
    # my_thread = threading.Thread(target=print_i, args=(1,))
    # my_thread.start()

    # threads = [threading.Thread(name='t%d' % (i,), target=print_time) for i in range(3)]
    # [t.start() for t in threads]

    # threads = [threading.Thread(name='t%d'%(i,),target=add1) for i in range(10)]
    # [t.start() for t in threads]

    # threads = [threading.Thread(name='t%d'%(i,),target=add2) for i in range(3)]
    # [t.start() for t in threads]
    
    a = A()
    B(a)

    pass
