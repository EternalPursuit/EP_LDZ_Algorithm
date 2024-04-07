class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            # 当遍历的时候，并不会修改对应位置的绝对值大小，而只是
            # 将其标记为负数而已，这样并不影响它取值，因为负数的绝对值还是一样的。
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

s = Solution()
nums = [3,4,-1,1,9,-5]
res = s.firstMissingPositive(nums)
print(res)