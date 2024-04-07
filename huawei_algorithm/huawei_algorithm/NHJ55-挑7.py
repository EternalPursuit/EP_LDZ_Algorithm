n = int(input())
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 0
for i in range(2, n+1):
    if (i >= 7 and i % 7 == 0) or str(i).find("7") != -1:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i-1]

print(dp[n])