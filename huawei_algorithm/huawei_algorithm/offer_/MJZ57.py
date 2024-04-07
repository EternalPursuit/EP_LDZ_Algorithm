
'''
描述
输入一个升序数组 array 和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，返回任意一组即可，如果无法找出这样的数字，返回一个空数组即可。
'''



def FindNumbersWithSum(array, sum):
    # write code here
    mid = len(array) // 2
    res = []
    l_largest = mid
    r_smallest = mid
    while l_largest >= 0:
        tar_add = sum - array[l_largest]
        while array[r_smallest] < tar_add:
            r_smallest += 1
        if array[r_smallest] == tar_add and r_smallest != l_largest:
            res.append(array[l_largest])
            res.append(array[r_smallest])
            break
        else:
            l_largest -= 1

    if array[l_largest] + array[r_smallest] != sum:
        return []
    else:
        return res

array = [1,4,4,9]
sum = 8
res = FindNumbersWithSum(array,sum)
print(res)