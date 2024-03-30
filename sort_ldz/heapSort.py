'''
对于堆排序的理解：
    1. 首先要建立一个大顶堆或者小顶堆。
    2. 通过不断地将上面元素和下面元素替换，然后修改恢复大顶堆，或者小顶堆。
    3. 通过递归调用的方法完成。
    4. 大顶堆的建立需要借用到维护所需函数。
    5. 维护所需函数，实现非常简单，就是将
'''
# def heapSort(nums):
#     length = len(nums)
#     for i in range(length//2-1,-1,-1):
#         heapify(nums,length,i)
#
#     while length > 0:
#         nums[0],nums[length-1] = nums[length-1],nums[0]
#         length -= 1
#         heapify(nums,length,0)
#
#     return nums
#
#
#
#
# def heapify(nums,n,i):
#     left = 2*i + 1
#     right = 2*i +2
#     largest = i
#     if left < n and nums[left] > nums[largest]:
#         largest = left
#     if right < n and nums[right] > nums[largest]:
#         largest = right
#
#     if largest != i:
#         nums[largest],nums[i] = nums[i],nums[largest]
#         heapify(nums,n,largest)
    


nums = [3,4,5,6,5,8,68,9,6,5]
heapSort(nums)
print(nums) 
    