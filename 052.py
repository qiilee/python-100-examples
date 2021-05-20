#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：学习使用按位或 | 。

# 程序分析：0|0=0; 0|1=1; 1|0=1; 1|1=1
# 实例(Python 2.0+)
 
if __name__ == '__main__':
    a = 0o77
    b = a | 3
    print ('a | b is %d' % b)
    b |= 7
    print ('a | b is %d' % b)

# 以上实例输出结果为：

# a | b is 63
# a | b is 63