# _*_ coding: utf-8 _*_
# -------------------------------------------------------------------------------
#  @Time : 2020/7/24 9:15
#  @Author : yls
#  @Version：V 0.1
#  @File : m_timedelta_module.py
#  @desc : 时间相关的案例
# -------------------------------------------------------------------------------
import re
from datetime import datetime, date, time, timedelta
import calendar


def get_days_girlfriend(birthday: str) -> int:
    """
    计算还有几天是你生日
    Args:
        birthday: 生日日期

    Returns:
        返回还剩多少天到生日
    """
    splits = re.split(r'[-.\s+/]', birthday)
    # 去掉空格符
    splits = [s for s in splits if s]
    if len(splits) < 3:
        raise ValueError('输入格式不正确，至少包括年月日')
    # 只截取年月日
    splits = splits[:3]

    birthday = datetime.strptime('-'.join(splits), '%Y-%m-%d')
    tod = date.today()
    dalta = birthday.date() - tod
    return dalta.days


def get_year_calendar():
    """
    绘制年的日历图
    Returns:
        打印指定2019年的年日历图
    """
    mydate = date.today()
    year_calendar_str = calendar.calendar(2019)
    print(f"{mydate.year}年的日历图：{year_calendar_str}\n")


def get_month_calendar():
    """
    绘制月的日历图
    Returns:
        打印月份的日历图
    """
    mydate = date.today()
    month_calendat_str = calendar.month(mydate.year, mydate.month)
    print(f"{mydate.year}年-{mydate.month}月的日历图：{month_calendat_str}\n")


def is_a_leep_year():
    """
    判断是否为闰年
    Returns:
        打印是否为闰年
    """
    mydate = date.today()
    is_leap = calendar.isleap(mydate.year)
    print_leap_str = "%s年是闰年" if is_leap else "%s年不是闰年\n"
    print(print_leap_str % mydate.year)


def month_has_days():
    """
    判断月有几天
    Returns:
        打印月有多少天
    """
    mydate = date.today()
    weekday, days = calendar.monthrange(mydate.year, mydate.month)
    print(f"{mydate.year}年-{mydate.month}月的第一天是那一周的第{weekday}天\n")
    print(f"{mydate.year}年-{mydate.month}月共有{days}天\n")

    month_first_day = date(mydate.year,mydate.month,1)
    print(f"当月第一天：{month_first_day}\n")

    _,days = calendar.monthrange(mydate.year,mydate.month)
    month_last_day = date(mydate.year,mydate.month,days)
    print(f"当月最后一天:{month_last_day}\n")


if __name__ == '__main__':
    # days = get_days_girlfriend('2020-08-20')
    # print(days)
    # days = get_days_girlfriend('2020/8/20')
    # print(days)
    # days = get_days_girlfriend('2020 8 20')
    # print(days)
    # days = get_days_girlfriend('2020/8/20 19:00')
    # print(days)

    # 年日历图
    # get_year_calendar()
    # 月日历图
    # get_month_calendar()

    # 判断当前是否为闰年
    # is_a_leep_year()

    # 判断月有几天
    month_has_days()
    pass
