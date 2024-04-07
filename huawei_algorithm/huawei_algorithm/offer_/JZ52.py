'''
描述
输入两个无环的单向链表，找出它们的第一个公共结点，如果没有公共节点则返回空。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

数据范围： n≤1000n≤1000
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)
'''


# class Solution:
#     def IsContinuous(self, numbers: List[int]) -> bool:
#         # 这道题的关键在于：求得非零数值之间的差异和是否大于0的个数
#         # 因此需要两步：1. 求得非零数值之间的差异和，2. 求得0的个数
#         minValue = 20
#         zero_num = 0
#         sum = 0
#         for val in numbers:
#             if val == 0:
#                 zero_num += 1
#             else:
#                 if val > minValue:
#                     minValue = val
#                 sum += val
#         # 求得非零数值的差异和：sum - minValue * (5 - zero_num) - (5-zero_num)
#         x = sum - (minValue+1)*(5-zero_num)
#         if x > zero_num:
#             return False
#         else:
#             return True

numbers = [1,3,2,6,4]
minValue = 15
maxValue = -1
zero_numbers = 0
for val in numbers:
    if val == 0:
        zero_numbers += 1
    if val > maxValue:
        maxValue = val

    if val < minValue:
        minValue = val

print(maxValue - minValue <= 4)


        # write code here
        # numbers.sort()
        # zero_nums = 0
        # res = []
        # for val in numbers:
        #     if val == 0:
        #         zero_nums += 1
        #     else:
        #         res.append(val)
        #
        # flag = res[0]
        # count_diff = 0
        # for val in res[1:]:
        #     if val == flag:
        #         return False
        #     count_diff += val - flag - 1
        #     flag = val
        #
        # if count_diff > zero_nums:
        #     return False
        # else:
        #     return True
