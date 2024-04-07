'''
描述
Redraiment是走梅花桩的高手。Redraiment可以选择任意一个起点，从前到后，但只能从低处往高处的桩子走。他希望走的步数最多，你能替Redraiment研究他最多走的步数吗？

数据范围：每组数据长度满足 1≤n≤200 1≤n≤200  ， 数据大小满足 1≤val≤350 1≤val≤350



输入描述：

数据共2行，第1行先输入数组的个数，第2行再输入梅花桩的高度
输出描述：

输出一个结果
'''

n = int(input())
m = map(int, input().split())

dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if m[j] < m[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

