#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：八进制转换为十进制

# 程序分析：无。
# 实例(Python 2.0+)
 
if __name__ == '__main__':
    n = 0
    p = raw_input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print n

# 以上实例输出结果为：

# input a octal number:
# 122
# 82