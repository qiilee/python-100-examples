#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：时间函数举例1。

# 程序分析：无。

# 程序源代码：

if __name__ == '__main__':
    import time
    print time.ctime(time.time())
    print time.asctime(time.localtime(time.time()))
    print time.asctime(time.gmtime(time.time()))

# 以上实例输出结果为：

# Wed Oct 21 17:08:51 2015
# Wed Oct 21 17:08:51 2015
# Wed Oct 21 09:08:51 2015