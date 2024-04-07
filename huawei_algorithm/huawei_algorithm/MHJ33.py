# def ip_num(s):
#     t = map(int,s.split("."))
#     res = ''
#     for val in t:
#         tmp_char = str(bin(val))[2:]
#         tmp_char = tmp_char if len(tmp_char) == 8 else '0'*(8-len(tmp_char)) + tmp_char
#         res += tmp_char

'''
描述

原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

数据范围：保证输入的是合法的 IP 序列
'''
S = "10.0.3.193"

# print(S.split("."))
t = map(int, S.split("."))
t = list(t)
print(list(t))
res = t[0] * 2 ** 24 + t[1] * 2 ** 26 + t[2] * 2 ** 8 + t[3]
print(res)