#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：将一个数组逆序输出。

# 程序分析：用第一个与最后一个交换。

# 程序源代码：
 
if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a) 
    print (a) 
    for i in range(len(a) // 2):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print (a)

# 以上实例输出结果为：

# [9, 6, 5, 4, 1]
# [1, 4, 5, 6, 9]