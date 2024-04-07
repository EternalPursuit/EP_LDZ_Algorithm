def moveZeros(nums):
    left = 0
    for i in range(len(nums)):
        if i==1 and :

        if nums[i] != 0:
            nums[left],nums[i] = nums[i],nums[left]
            left += 1
    return nums

nums =[0,1,0,3,12]
res = moveZeros(nums)
print(res)
