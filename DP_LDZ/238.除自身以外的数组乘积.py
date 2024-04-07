'''
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        L, R, answer = [0] * length, [0] * length, [0] * length

        L[0] = 1
        for i in range(1, length):
            L[i] = L[i - 1] * nums[i - 1]

        R[length - 1] = 1
        for i in range(length - 2, -1, -1):
            R[i] = R[i + 1] * nums[i + 1]

        for i in range(length):
            answer[i] = L[i] * R[i]
        return answer