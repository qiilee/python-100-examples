#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：时间函数举例3。

# 程序分析：无。

# 程序源代码：

if __name__ == '__main__':
    import time
    start = time.clock()
    for i in range(10000):
        print i
    end = time.clock()
    print 'different is %6.3f' % (end - start)

# 以上实例输出结果为：

# 0
# 1
# 2
# 3
# 4
# ……
# different is  0.015