'''
在这道题中，下面的区间长度刚好是left - right，不用+1,
需要记住：这种段的长度的时候，是不用加1的，否则就要自己去临时想。
'''
def maxArea(height):
    i,j,res = 0,len(height),0
    while i < j:
        if height[i] < height[j]:
            res = max(res,height[i]*(j-i))
            i += 1
        else:
            res = max(res,height[j]*(j-i))
            j -= 1
    return res
 

