'''
这道题最巧妙的地方在于对于起始点-1在数据集中的，不去考虑
而对于起始点-1的采取考虑
这是因为我们只需要考虑起始点就行，至于那些不是起始点的
只需要跳过就行了，因为必然会被考虑到。
'''
# def longestConsecutive(nums):
#     res = 0
#     num_set = set(nums)
#     for num in num_set:
#         if num - 1 not in num_set:
#             seq_len = 1
#             while (num+1) in num_set:
#                 seq_len += 1
#                 num += 1
#             res = max(res, seq_len)
#     return res

def longestConsecutive2(nums):
    res = 0
    nums_set = set(nums)
    for num in nums_set:
        if num - 1 not in nums_set:
            seq_len = 1
            while num + 1 in nums_set:
                seq_len += 1
                num += 1
            res = max(res, seq_len)
    return res

