#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：字符串日期转换为易读的日期格式。

# 程序分析：无。

# 程序源代码：

from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print dt

# 以上实例输出结果为：

# 2015-08-28 00:00:00