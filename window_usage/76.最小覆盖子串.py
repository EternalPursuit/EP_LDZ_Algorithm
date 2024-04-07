'''
给你一个字符串 s 、一个字符串 t 。
返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
'''
def minWindow(s, t):
    left,right = 0,0
    window,need = {},{}
    valid = 0
    min_len = float('inf')
    start = 0
    for val in t:
        need[val] = need.get(val, 0) + 1

    while right < len(s):
        c = s[right]
        right += 1

        if c in need:
            window[c] = window.get(c,0) + 1
            if window[c] == need[c]:
                valid += 1

        while valid == len(need):
            if (right - left) < min_len:
                start = left
                min_len = right - left
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return "" if min_len == float('inf') else s[start:start+min_len]


def minWindow2(s, t):
    left,right = 0,0
    window,need = {},{}
    valid = 0
    start = 0
    min_len = float('inf')

    for val in t:
        need[val] = need.get(val, 0)+1

    while right < len(s):

        # 延伸右边界
        c = s[right]
        right += 1

        # 对延伸后的右边界进行处理
        if c in need:
            window[c] = window.get(c,0) + 1
            if window[c] == need[c]:
                valid += 1

        # 窗口符合条件了，就要开始处理了，在while循环中不断收缩左边界，
        # 不过需要知道的是滑动窗口收缩左边界的方法并不止下面这一种，还可以
        # 跳跃处理的，这都是依据题目进行判断的。比如不重复字符中就是直接跳转，高效又正确。
        while valid == len(need):
            # 判断一下是否需要更新，如果需要，就更新start，和min_len
            if (right - left) < min_len:
                start = left
                min_len = right - left

            # 开始收缩left边界
            d = s[left]
            left += 1
            # 处理一下左边界
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return "" if min_len == float('inf') else s[start:start+min_len]