'''
快排的思想：主要就是通过：1. 找基准点，并且返回分成两半的数组，2. 递归

思路正确，但是在操作方式上发生了错误。也就是说对于快排来说，最基本的参数是3个，nums,start,end

只有这样，才能保持原数组排序。

'''
# def quickSort(nums):
#     if len(nums) <= 1:
#         return  nums
    
#     pivot = partition(nums)

#     left_nums = quickSort(nums[:pivot])
#     right_nums = quickSort(nums[pivot:])
#     return left_nums + right_nums
'''
最原始的做法，但是这种做法是不对的，所以还是不要用了。
记录在语雀中的方法一中。
'''

# def partition(nums):
#     if len(nums) <= 1:
#         return nums
    
#     pivot_nums = nums[0]
#     i = 0
#     j = len(nums) - 1
#     while i < j:
#         while  i < j and nums[i] < pivot_nums:
#             i += 1
        
#         while i < j and nums[j] > pivot_nums:
#             j -= 1
        
#         if i < j:
#             nums[i],nums[j] = nums[j],nums[i]
#     return j


# def quickSort(nums, start=0, end=None):
#     if end is None:
#         end = len(nums) - 1
#
#     if start < end:
#         pivot_index = partition(nums, start, end)
#         quickSort(nums, start, pivot_index - 1)
#         quickSort(nums, pivot_index + 1, end)
#
#
# def partition(nums, start, end):
#     pivot = nums[end]
#     left = start
#     for i in range(start,end):
#         if nums[i] < pivot:
#             nums[i], nums[left] = nums[left], nums[i]
#             left += 1
#
#     if nums[left] > pivot:
#         nums[left], nums[end] = nums[end], nums[left]
#
#     return left
#
    # pivot = nums[(start + end)//2]
    # i = start
    # j = end
    # while i < j:
    #     if nums[i] < pivot:
    #         i += 1
    #     if nums[j] > pivot:
    #         j -= 1
    #     if i < j:
    #         nums[i],nums[j] = nums[j],nums[i]
    # return i
# def quickSort(nums,start=0,end=None):
#     if end is None:
#         end = len(nums) - 1
#     if len(nums) <= 1:
#         return  nums
#     if start < end:
#         pivot = partition(nums,start,end)
'''
思路一：完全正确的做法了，最主要的思路就是将pivot定在end
然后将left赋予开始索引,去除掉end，
紧接着开始遍历每个元素就行，将<pivot的数和left进行交换后，left+=1
left实际上就是当前小于pivot的最大索引，最后将left的数值和pivot比较一下
如果符合情况就调换，返回left就行了。
'''
# def partition(nums,start,end):
#     pivot = nums[end]
#     left = start
#     for i in range(start,end):
#         if nums[i] <= pivot:
#             nums[left],nums[i] = nums[i],nums[left]
#             left += 1
#
#     if nums[left] > pivot:
#         nums[left],nums[end] = nums[end],nums[left]
#     return left
###############################################################
# 思路二：完全正确的做法了，最主要的思路就是每当发现一个不符合情况的索引时，
# 立刻将其进行调换。这时候调换之后，双方的索引都没有变换，但值已经发生变化，
# 接着继续判断就行了
def partition(nums,low,high):
    pivot = nums[low]
    while low < high:
        while low < high and nums[high] >= pivot:
            high -= 1
        nums[low], nums[high] = nums[high], nums[low]
        while low < high and nums[low] <= pivot:
            low += 1
        nums[low], nums[high] = nums[high], nums[low]

    return low

def quickSort(nums,low,high=None):

    if high is None:
        high = len(nums)-1

    if low < high:
        mid = partition(nums,low,high)
        quickSort(nums,low,mid-1)
        quickSort(nums,mid+1,high)
    


# nums = [3,6,4,12,5,6,5,8,68,9,6,5]
nums = [16,0,100,1,9]
quickSort(nums,0)
print(nums)
