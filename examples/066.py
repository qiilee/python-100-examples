#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：输入3个数a,b,c，按大小顺序输出。　　　

# 程序分析：无。

# 程序源代码：

 
if __name__ == '__main__':
    n1 = int(raw_input('n1 = :\n'))
    n2 = int(raw_input('n2 = :\n'))
    n3 = int(raw_input('n3 = :\n'))
 
    def swap(p1,p2):
        return p2,p1
 
    if n1 > n2 : n1,n2 = swap(n1,n2)
    if n1 > n3 : n1,n3 = swap(n1,n3)
    if n2 > n3 : n2,n3 = swap(n2,n3)
 
    print n1,n2,n3

# 以上实例输出结果为：

# n1 = :
# 123
# n2 = :
# 456
# n3 = :
# 789
# 123 456 789