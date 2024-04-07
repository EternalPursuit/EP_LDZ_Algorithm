def findAnagrams(s,p):
    left,right = 0,0
    window,need={},{}
    res = []
    valid = 0
    for val in p:
        need[val] = need.get(val,0) + 1

    while right < len(s):
        r_char = s[right]
        right += 1

        if r_char in need:
            window[r_char] = window.get(r_char,0) + 1
            if window[r_char] == need[r_char]:
                valid += 1

            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d,0) - 1
    return res

