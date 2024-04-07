'''
描述

给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。
注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串。
数据范围：字符串长度：1≤s≤150 1≤s≤150
进阶：时间复杂度：O(n3) O(n3) ，空间复杂度：O(n) O(n)
输入描述：

输入两个只包含小写字母的字符串
输出描述：

输出一个整数，代表最大公共子串的长度
'''

'''
# 建立动态规划方程，dp[i][j]表示为到第一个字串i,第二个字串j处的最大公共子串的长度。
# 那么:  dp[i][j] = dp[i-1][j-1] + 1 if t[i] == h[j] else max(dp[i-1][j], dp[i][j-1])

这道题和最长公共子序列是有一点不同的，这道题是最大公共子串，要求的是连续，因此在写状态转移方程的时候是需要为0
并且记录最大长度的。

'''
def LongestCommonSubsequence(text1,text2):
    m, n = len(text1), len(text2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    max_length = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j-1]+1 if text1[i-1] == text2[j-1] else 0
            max_length = max(max_length,dp[i][j])

    return dp[m][n]

test1 = "asdfas"
text2 = "werasdfaswer"

res = LongestCommonSubsequence(test1,text2)
print(res)