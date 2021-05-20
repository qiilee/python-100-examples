#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：计算字符串中子串出现的次数。

# 程序分析：无。
# 实例(Python 2.0+)
 
if __name__ == '__main__':
    str1 = raw_input('请输入一个字符串:\n')
    str2 = raw_input('请输入一个子字符串:\n')
    ncount = str1.count(str2)
    print ncount

# 以上实例输出结果为：

# 请输入一个字符串:
# www.runoob.com
# 请输入一个子字符串:
# runoob
# 1