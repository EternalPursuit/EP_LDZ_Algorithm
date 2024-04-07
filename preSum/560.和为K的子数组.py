'''
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
子数组是数组中元素的连续非空序列。
'''
'''
这道题的解法是：前缀和。
条件：题目中的要求是连续非空序列，并且是求和的。
所以才能使用： 前缀和。因为它是记录了连续多个数字的和。
'''
'''
这道题有两个要点：
1. 初始化一个前缀和 字典
2. 设置一个 当前前缀和的数
'''
from collections import defaultdict
def subarraySum(nums,k):
    ans = 0
    presum = defaultdict(int)
    presum[0] = 1
    cur_presum = 0
    for i in range(len(nums)):
        cur_presum += nums[i]
        ans += presum[cur_presum-k]
        presum[cur_presum] += 1
    return ans
