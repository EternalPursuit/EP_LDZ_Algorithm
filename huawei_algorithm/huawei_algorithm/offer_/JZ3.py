'''
 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，那么对应的输出是2或者3。存在不合法的输入的话输出-1

数据范围：0≤n≤10000 0≤n≤10000
进阶：时间复杂度O(n) O(n) ，空间复杂度O(n) O(n)
'''
class Solution:
    def duplicate(self , numbers: List[int]) -> int:
        # write code here
        tmp = {}
        for val in numbers:
            if not val.isdigit():
                return -1
            tmp[val] = tmp.get(val,0) + 1
            if tmp[val] > 1:
                return val