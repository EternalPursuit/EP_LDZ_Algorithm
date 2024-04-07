# class Solution:
#     def nextPermutation(self, nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i = len(nums) - 1
#         while i > 0 and nums[i] <= nums[i-1]:
#             i -= 1
#         if i > 0:
#             nums[i],nums[i-1] = nums[i-1],nums[i]
#         nums[i:].sort()
#         return nums
'''
这道题的思路是：从后面向前找，第一个降序的数，就是我们要处理的边界
我们需要将i -1处的值换成i:后面值中的最小值，这就是交换
然后将i:后面的 值升序排列，这样就是紧邻值
但是需要注意的是，我们在找i的时候，已经确定i：后的是降序排列了
所以升序只不过是一个对调的过程。
'''
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i > 0:
            j = len(nums) - 1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[j],nums[i-1] = nums[i-1],nums[j]
        left,right = i,len(nums)-1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left,right = left + 1,right-1
        return nums

nums = [3,2,1]
s = Solution()
res = s.nextPermutation(nums)
print("origin nums : ",nums)

print("fasd",nums.sort())