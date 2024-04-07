class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # size = len(nums)
        # if size == 0:
        #     return 0

        # dp = [0]*size
        # dp[0] = nums[0]

        # for i in range(1,size):
        #     if dp[i-1] >= 0:
        #         dp[i] = dp[i-1] + nums[i]
        #     else:
        #         dp[i] = nums[i]
        # return max(dp)
        # for i in range(1,len(nums)):
        #     nums[i] = max(nums[i],nums[i-1]+nums[i])
        # return max(nums)
        pre = 0
        res = nums[0]
        for i in range(len(nums)):
            pre = max(nums[i],pre+nums[i])
            res = max(res,pre)
        return res