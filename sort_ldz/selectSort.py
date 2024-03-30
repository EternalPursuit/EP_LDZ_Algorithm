def selectSort(nums):
    '''
    选择排序的思想：就是从后面的所有元素中，通过比较选出最小的，然后加入到开头
    '''
    if not nums:
        return nums
    
    for i in range(len(nums)):
        minValue_ind = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[minValue_ind]:
                minValue_ind = j
        nums[minValue_ind],nums[i] = nums[i],nums[minValue_ind]
    return nums

if __name__ == "__main__":
    nums = [3,5,6,9,7,1,2,5,9,1,222,8,4]
    res = selectSort(nums)
    print(res)