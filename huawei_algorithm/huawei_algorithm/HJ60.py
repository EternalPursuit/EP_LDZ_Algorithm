'''
描述
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。

数据范围：输入的数据满足 4≤n≤1000 4≤n≤1000
输入描述：

输入一个大于2的偶数
输出描述：

从小到大输出两个素数
示例1
输入：

20

输出：

7
13

示例2
输入：

4

输出：

2
2

'''
N = int(input())

def is_su_shu(nums):
    i = 2
    while i * i < nums:
        if (nums%i) == 0:
            print(i)
            return False
        else:
            return True

for i in range(N//2+1,1,-1):
    print(i)
    if is_su_shu(i) and is_su_shu(N-i):
        print(i)
        print(N-i)
        break