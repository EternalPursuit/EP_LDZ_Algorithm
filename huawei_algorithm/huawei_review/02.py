from math import inf
arr = list(map(int, input().split()))
# 最小差值, 全部人员总实力， 人员总数
min_difference, tot, n = inf, sum(arr), len(arr)
def solve(idx: int, select_cnt: int, select_sum: int):
    global min_difference
    if select_cnt == n // 2:
    # 当全部人员选择了一半时，计算两组实力差值是否更小
        min_difference = min(min_difference, abs(tot - 2 * select_sum))
        return
    for i in range(idx, n):
    # 不选择时
        solve(i + 1, select_cnt, select_sum)
        solve(i + 1, select_cnt + 1, select_sum + arr[i])
        solve(0, 0, 0)

print(min_difference)
