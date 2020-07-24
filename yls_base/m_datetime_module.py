# -*- coding: UTF-8 -*-
"""
 @Time: 2020/07/23 20:23 
 @Author: yls 
 @Version: V 0.1
 @File: m_datetime_module.py
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
from datetime import date, time, datetime, timedelta


def datetime_fun():
    """
    date
    """
    # 打印当前日期
    tod = date.today()
    print(tod)

    # 打印日期字符串
    str_date = date.strftime(tod, '%Y-%m-%d')
    print(str_date)

    # 字符日期转日期
    str_to_date = datetime.strptime('2020-02-22', '%Y-%m-%d')
    print(str_to_date)

    """
    datetime
    """
    # 打印当前时间
    right = datetime.now()
    print(right)

    # 当前时间转字符串显示
    str_time = datetime.strftime(right, '%Y-%m-%d %H:%M:%S')
    print(str_time)

    # 字符串时间转时间类型
    str_to_time = datetime.strptime('2020-02-02 15:12:13', '%Y-%m-%d %H:%M:%S')
    print(str_to_time)


if __name__ == '__main__':
    datetime_fun()
    pass
