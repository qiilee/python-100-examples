#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：创建一个链表。

# 程序分析：无。
# 实例(Python 2.0+)
 
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(raw_input('please input a number:\n'))
        ptr.append(num)
    print ptr

# 以上实例输出结果为：

# please input a number:
# 3
# please input a number:
# 5
# please input a number:
# 7
# please input a number:
# 8
# please input a number:
# 2
# [3, 5, 7, 8, 2]