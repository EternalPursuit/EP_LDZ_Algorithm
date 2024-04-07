'''
自己的解题方法,但是是有问题的，需要以后回看
'''
# def lengthOfLongestSubstring(s):
#     left, right = 0, 0
#     window = dict()
#     res = 0
#     while right < len(s):
#         r_char = s[right]
#
#         right += 1
#         if r_char in window:
#             while s[left] != r_char:
#                 left += 1
#             left += 1
#             window[r_char] = right -1
#             res = max(res, right - left)
#     return res

def lengthOfLongestSubstring(s):
    dic, res, i = {},0,-1
    for j in range(len(s)):
        if s[j] in dic:
            i = max(dic[s[j]],i)
        dic[s[j]] = j
        res = max(res,j-i)
    return res