'''
描述

功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

数据范围： 1≤n≤2×109+14 1≤n≤2×109+14
输入描述：

输入一个整数
输出描述：

按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
示例1
输入：

180

输出：

2 2 3 3 5

'''

Target_Num = int(input())

factor_list = []
factor_num = 2

while Target_Num >= 1 and factor_num*factor_num < Target_Num:
    while (Target_Num%factor_num) == 0:
        factor_list.append(factor_num)
        Target_Num //= factor_num
        print("Target_num is : ",Target_Num)
    factor_num += 1

if Target_Num > 1:
    factor_list.append(Target_Num)

for val in factor_list:
    print(val,end=" ")