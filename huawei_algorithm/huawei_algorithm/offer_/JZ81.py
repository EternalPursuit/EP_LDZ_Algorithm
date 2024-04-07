# class Solution:

'''
描述
输入一个长度为 n 整数数组，数组里面可能含有相同的元素，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，对奇数和奇数，偶数和偶数之间的相对位置不做要求，但是时间复杂度和空间复杂度必须如下要求。

数据范围：0≤n≤500000≤n≤50000，数组中每个数的值 0≤val≤100000≤val≤10000
要求：时间复杂度 O(n)O(n)，空间复杂度 O(1)O(1)



'''

def reOrderArraOyTwo(array):
    # write code here
    ori = 0
    end = len(array) - 1
    while ori <= end:
        while array[ori] %2 != 0:
            ori += 1
        while array[end] %2 == 0:
            end -= 1
        if ori < end:
            array[ori],array[end] = array[end],array[ori]
    return array

a = [1,2,3,4,5]
b = reOrderArrayTwo(a)
print(b)

left, right = 0, len(array) - 1
while left < right:
    # 找到左边的偶数
    while left < right and array[left] % 2 != 0:
        left += 1
    # 找到右边的奇数
    while left < right and array[right] % 2 == 0:
        right -= 1
    # 交换偶数和奇数
    if left < right:
        array[left], array[right] = array[right], array[left]
return array