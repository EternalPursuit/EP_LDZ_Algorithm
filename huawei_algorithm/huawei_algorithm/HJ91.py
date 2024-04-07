'''
描述
请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）从棋盘左上角出发沿着边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。

注：沿棋盘格之间的边缘线行走

数据范围： 1≤n,m≤8 1≤n,m≤8


输入描述：

输入两个正整数n和m，用空格隔开。(1≤n,m≤8)
输出描述：

输出一行结果
示例1
输入：

2 2

输出：

6

'''

M,N = map(int,input().split())

dp = [[0]*N for _ in range(M)]

for i in range(N):
    dp[0][i] = 1
for i in range(M):
    dp[i][0] = 1


for i in range(1,M):
    for j in range(1,N):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[M-1][N-1])