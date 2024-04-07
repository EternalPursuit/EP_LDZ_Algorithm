
'''
描述

密码要求:

1.长度超过8位

2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

数据范围：输入的字符串长度满足 1≤n≤100 1≤n≤100
输入描述：

一组字符串。
输出描述：

如果符合要求输出：OK，否则输出NG
'''

import sys
import re

def check(s):
    if len(s) <= 8:
        return 0


    kinds = 0
    # 判断应该包含 大小写 字母， 数字， 其他符号
    if re.search('[a-z]',s):
        kinds += 1
    if re.search('[A-Z]',s):
        kinds += 1
    if re.search('[0-9]',s):
        kinds += 1
    if re.search('\W',s) and re.search(r'[^ \r]',s):
        kinds += 1
    if kinds < 3:
        return 0
    # 判断不能有长度大于2的包含公共元素的子串重复
    for i in range(len(s)-3):
        if len(s.split(s[i:i+3]))>=3:
            return 0
    return 1

while True:
    try:
        s = input()
        res = check(s)
        print("OK" if res else "NG")

    except:
        break