'''
描述

蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

例如，当输入5时，应该输出的三角形为：

1 3 6 10 15

2 5 9 14

4 8 13

7 12
11 
'''
rows = int(input())

i = 0
start = 1
j = 2
for _ in range(rows):
    start += i
    res = start
    print(res,end=" ")
    for s in range(j,rows+1):
        res += s
        print(res,end=" ")
    print("\n")
    i += 1
    j += 1