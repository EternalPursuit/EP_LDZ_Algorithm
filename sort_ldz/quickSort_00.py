class Solution:
    def sortedSquares(self, nums):
        new_squared_nums = []
        for val in nums:
            new_squared_nums.append(val**2)
        print("开始排序")
        self.quickSort(new_squared_nums,0,len(new_squared_nums)-1)
        print("结束排序")
        return new_squared_nums
        
    # def quickSort(self,nums,low,high=None):
    #     if len(nums) <= 1:
    #         return nums
    #     if high is None:
    #         high = len(nums) - 1
        
    #     mid = self.partition(nums,low,high)
    #     self.quickSort(nums,low,mid-1)
    #     self.quickSort(nums,mid+1,high)
    
    # def partition(self,nums,low,high):
    #     pivot = nums[high]

    #     left = low
    #     for i in range(low,high):
    #         if nums[i] < pivot:
    #             nums[i],nums[left] = nums[left],nums[i]

    #     if nums[left] > pivot:
    #         nums[left],nums[high] = nums[high],nums[left]
    #     return left       
# 下面是正确的代码，不过当pivot的取值发生变化时，就不正确了。
    # def partition(self,nums,low,high):
    #     pivot = nums[low]
    #     while low < high:
    #         while low < high and nums[high] >= pivot:
    #             high -= 1
    #         nums[low], nums[high]  = nums[high], nums[low]
    #         while low < high and nums[low] <= pivot:
    #             low += 1
    #         nums[low], nums[high] = nums[high], nums[low]
    #     return low

    # def quickSort(self,nums,low,high=None):
    #     if high is None:
    #         high = len(nums)-1
    #     if low < high:
    #         mid = self.partition(nums,low,high)
    #         self.quickSort(nums,low,mid-1)
    #         self.quickSort(nums,mid+1,high)

    def partition(self,nums,low,high):
        pivot = nums[high]
        left = low
        for j in range(low,high):
            if nums[j] < pivot:
                nums[j],nums[left] = nums[left],nums[j]
                left += 1
        if nums[left] > pivot:
            nums[left],nums[high] = nums[high],nums[left]
        return left

    def quickSort(self,nums,low,high):
        if low < high:
            pi = self.partition(nums,low,high)
            self.quickSort(nums,low,pi-1)
            self.quickSort(nums,pi+1,high)

s = Solution()
nums = [-4,-1,0,3,10]
res = s.sortedSquares(nums)
print(res)