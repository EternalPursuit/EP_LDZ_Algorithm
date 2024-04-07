'''
描述
输入一个正整数，计算它在二进制下的1的个数。
注意多组输入输出！！！！！！

数据范围： 1≤n≤231−1 1≤n≤231−1
输入描述：

输入一个整数
输出描述：

计算整数二进制中1的个数
示例1
输入：

5

输出：

2

说明：

5的二进制表示是101，有2个1

示例2
输入：

0

输出：

0


'''

N = int(input())

res = 0
while N > 0:
    if N%2 == 1:
        res += 1
        N >>= 1
print(res)