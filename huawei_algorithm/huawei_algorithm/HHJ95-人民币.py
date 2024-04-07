map_gewei = ["零", "壹", "贰", "叁", "肆","伍", "陆", "柒", "捌", "玖", "拾"]
map_danwei = ['元', '万','亿']
map_shuzi = ["", '拾', "佰", "仟"]


def ZhengShu(s):
    if s == "0":
        return "零元"
    res = ''
    len_s = len(s)
    #分段处理每4位
    for i in range(len_s,0,-4):
        start = max(i-4,0)
        section = s[start:i]
        fourth = ''
        last_was_zero = False
        for j,ch in enumerate(section[::-1]):
            num = int(ch)
            if num == 0:
                if not last_was_zero and j<len(section)-1:
                    fourth = map_gewei[num]+fourth
                last_was_zero = True
            else:
                fourth = map_gewei[num] + map_shuzi[j] + fourth
                last_was_zero = False
        if fourth:
            unit_index = (len_s-start)//4 - 1
            fourth += map_danwei[unit_index] if unit_index<len(map_gewei) else ""
        res = fourth + res
    return res + "元"    
    # i = 0
    # fourth_ = ''
    # while i < len(s):
    #     # 当前位上的数字
    #     num = int(s[i])
    #     # 找到对应的转换
    #     zhuan_num = map_gewei[num]
    #     # 找到对应的数位
    #     shu_num = map_shuzi[i % 4]
    #     # 当前位的表示组合起来：
    #     tmp = zhuan_num + shu_num
    #
    #     fourth_ = tmp + fourth_
    #     i += 1
    #     # 满4个就加到res上
    #     if i % 4 == 0 or (i >= len(s)):
    #         res = fourth_ + map_danwei[i // 4] + res