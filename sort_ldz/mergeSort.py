'''
归并排序：主要就是将nums分成两个部分，然后递归合并。

我在这段代码的理解中，思路是正确的，代码也是正确的，唯一的不足是
在mergeSort的初始化问题上，有一点小问题，那就是len(nums) <= 1，就要返回nums了

而我只是单纯地判断了是否为空，这是一种不负责的心态和思想，需要改正。
'''

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums)//2
    return merge(mergeSort(nums[:mid]),mergeSort(nums[mid:]))


def merge(nums1,nums2):
    if not nums1:
        return nums2
    if not nums2:
        return nums1
    res = [ ]
    i = 0
    j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    
    if j >= len(nums2):
        res.extend(nums1[i:])
        
    if i >= len(nums1):
        res.extend(nums2[j:])
    return res

if __name__ == "__main__":
    nums = [3,1,66,8,4,5,1,2,9]
    res = mergeSort(nums)
    print(res)
    