'''


'''

# class Solution:
#     def isNumberic(self, s):
#         # 需要判断这个字符串是否是一个数字的表示
#         # 需要判断是一个整数的时候
#         # 需要判断是带有小数的时候
#         # 需要判断是否是科学计数法
#         import re
#         s = s.strip()
#         if re.match(r'^[+-]?\d+$') or re.match(r'^[+-]?\d{0,}\.\d{0,}$') or re.match(r'^[+-]?\d+[Ee][+-]?\d+'):
#             return True
#         else:
#             return  False

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return bool布尔型
import re

class Solution:
    def isNumeric(self, str):
        match_Obj = re.match('^\s*[+-]{0,1}((\d)+((\.)(\d)+){0,1}|((\.)(\d)+)|((\d)+(\.)))([eE][+-]{0,1}[\d]+){0,1}\s*$',str)
        match_Obj = re.match('^{0,1}$',str)

#         if re.match(r'^[+-]?\d+$') or re.match(r'^[+-]?\d{0,}\.\d{0,}$') or re.match(r'^[+-]?\d+[Ee][+-]?\d+'):
        if match_Obj:
            return True
        else:
            return False
(\d)+((\.)(\d)+){0,1}|((\.)(\d)+)|((\d)+(\.))
([eE][+-]{0,1}[\d]+){0,1}\s*

((\d)+((\.)(\d)+){0,1}|((\.)(\d)+)|((\d)+(\.)))
([eE][+-]{0,1}[\d]+){0,1}\s*