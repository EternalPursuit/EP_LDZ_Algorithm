'''
描述
输入一个字符串，返回其最长的数字子串，以及其长度。若有多个最长的数字子串，则将它们全部输出（按原字符串的相对位置）
本题含有多组样例输入。

数据范围：字符串长度 1≤n≤200 1≤n≤200  ， 保证每组输入都至少含有一个数字
输入描述：

输入一个字符串。1<=len(字符串)<=200
输出描述：

输出字符串中最长的数字字符串和它的长度，中间用逗号间隔。如果有相同长度的串，则要一块儿输出（中间不要输出空格）。
'''
s = "a8a72a6a5yy98y65ee1r2"
import re

t = re.findall("\d+",s)
t.sort(key=len)
res = ''
for val in t:
    if len(val) == len(t[-1]):
        res += str(val)
print(res)
print(f"{res},{len(t[-1])}")