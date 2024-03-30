def bubbleSort(nums):
    if nums is None:
        return nums
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums


if __name__ == "__main__":
    nums = [3,5,6,9,7,1,2,5,9,1,222,8,4]
    res = bubbleSort(nums)
    print(res)