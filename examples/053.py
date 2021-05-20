#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：学习使用按位异或 ^ 。

# 程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0

# 程序源代码：

if __name__ == '__main__':
    a = 0o77
    b = a ^ 3
    print ('The a ^ 3 = %d' % b)
    b ^= 7
    print ('The a ^ b = %d' % b)

# 以上实例输出结果为：

# The a ^ 3 = 60
# The a ^ b = 59