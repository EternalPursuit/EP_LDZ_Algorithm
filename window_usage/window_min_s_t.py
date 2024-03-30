'''
给定一个s,一个t，找到s中t的变为次的子串
返回这些自查你的其实索引，不考虑答案输出的顺序。
'''

def maxNoSameChar(s,t):
    left,right = 0,0
    window,need = {},{}
    valid = 0

    res = []

    for i in t:
        need[i] = need.get(i,0) + 1

    while right < len(s):
        val_r = s[right]
        right += 1

        if val_r in need:
            window[val_r] = window.get(val_r,0) + 1
            if window[val_r] == need[val_r]:
                valid += 1

        while right - left >= len(t):
            if valid == len(need):
                res.append(left)
            val_f = s[left]
            left += 1
            if val_f in need:
                if window[val_f] == need[val_f]:
                    valid -= 1
                window[val_f] -= 1
    return res
