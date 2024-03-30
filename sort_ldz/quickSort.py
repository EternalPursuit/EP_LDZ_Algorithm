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
def quickSort(nums,start=0,end=None):
    if end is None:
        end = len(nums) - 1
    if len(nums) <= 1:
        return  nums
    if start < end:
        pivot = partition(nums,start,end)
        quickSort(nums,start,pivot-1)
        quickSort(nums,pivot+1,end)

def partition(nums,start,end):
    pivot = nums[end]
    left = start
    for i in range(start,end):
        if nums[i] <= pivot:
            nums[left],nums[i] = nums[i],nums[left]
            left += 1

    if nums[left] > pivot:
        nums[left],nums[end] = nums[end],nums[left]
    return left




nums = [3,4,5,6,5,8,68,9,6,5]
quickSort(nums)
print(nums)
