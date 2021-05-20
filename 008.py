#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目：输出 9*9 乘法口诀表。

# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

# 程序源代码：

# 9*9 乘法口诀(Python 2.x)
for i in range(1, 10):
    print 
    for j in range(1, i+1):
        print "%d*%d=%d" % (i, j, i*j),



# 9*9 乘法口诀(Python 3.x)
#!/usr/bin/python3
 
for i in range(1, 10):
    print() 
    for j in range(1, i+1):
        print ("%d*%d=%d" % (i, j, i*j), end=" " )
