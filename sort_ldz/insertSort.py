# 插入排序，是通过维护一个已经排序好的前缀，进行后面的元素插入。
'''
我的思路错误了，在注释的代码并不是真正的插入排序代码，而是变相的冒泡排序，
因此，虽然能够正确排序，但不是插入排序。

插入排序算法，是在已经拍好序的数列中，逐个判断，逐个移动，最后插入的。

在使用循环的时候，最好还是使用while循环，这种循环虽然需要额外定义变量，不是很省力，但是
比for循环有用太多了。
'''
# def insertSort(nums):
#     if not nums:
#         return nums
#
#     for i in range(1,len(nums)):
#         # for j in range(i):
#         #     if nums[i] < nums[j]:
#         #         nums[i],nums[j] = nums[j],nums[i]
#         cur_val = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > cur_val:
#             nums[j+1] = nums[j]
#             j -= 1
#
#         nums[j+1] = cur_val
#
#
#     return nums

def insertSort(arr):
    for i in range(1,len(arr)):
        val = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > val:
                arr[j+1],arr[j] = arr[j],arr[j+1]
            else:
                break
        arr[j+1] = val
    return  arr
                
if __name__ == "__main__":
    nums = [3,5,6,9,7,1,2,5,9,1,222,8,4]
    res = insertSort(nums)
    print(res)