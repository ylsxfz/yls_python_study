# _*_ coding: utf-8 _*_
"""
 @Time : 2020/7/23 12:33 
 @Author : yls 
 @Version：V 0.1
 @File : m_time_module.py
 @desc : Python 时间模块使用逻辑大盘点
        Python 与时间处理相关模块有：time 模块和 datetime 模块。
            time 模块， 提供 2 种时间表达方式：
                1、假定一个零点基准，偏移长度换算为按秒的数值型
                2、由 9 个整数组成的元组 struct_time 表示的时间

            datetime 模块，常用类有 4 个：
                1、date：日期类，包括属性年、月、日及相关方法
                2、time：时间类，包括属性时、分、秒等及相关方法
                3、datetime：日期时间，继承于 date，包括属性年、月、日、时、分、秒等及相关方法，其中年月日必须参数
                4、timedelta：两个 datetime 值的差，比如相差几天（days）、几小时（hours）、几分（minutes）等。

            除了以上 2 个时间模块外，calendar 模块还提供一些实用的功能，比如：
                1、年、月的日历图
                2、闰年判断
                3、月有几天等等
 """
import time

def time_module():
    print('a')

if __name__ == '__main__':
    pass
