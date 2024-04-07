'''
描述
密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。

一、密码长度:
5 分: 小于等于4 个字符
10 分: 5 到7 字符
25 分: 大于等于8 个字符

二、字母:
0 分: 没有字母
10 分: 密码里的字母全都是小（大）写字母
20 分: 密码里的字母符合”大小写混合“

三、数字:
0 分: 没有数字
10 分: 1 个数字
20 分: 大于1 个数字

四、符号:
0 分: 没有符号
10 分: 1 个符号
25 分: 大于1 个符号

五、奖励（只能选符合最多的那一种奖励）:
2 分: 字母和数字
3 分: 字母、数字和符号
5 分: 大小写字母、数字和符号

最后的评分标准:
>= 90: 非常安全
>= 80: 安全（Secure）
>= 70: 非常强
>= 60: 强（Strong）
>= 50: 一般（Average）
>= 25: 弱（Weak）
>= 0:  非常弱（Very_Weak）

对应输出为：

VERY_SECURE
SECURE
VERY_STRONG
STRONG
AVERAGE
WEAK
VERY_WEAK

请根据输入的密码字符串，进行安全评定。

注：
字母：a-z, A-Z
数字：0-9
符号包含如下： (ASCII码表可以在UltraEdit的菜单view->ASCII Table查看)
!"#$%&'()*+,-./     (ASCII码：0x21~0x2F)
:;<=>?@             (ASCII码：0x3A~0x40)
[\]^_`              (ASCII码：0x5B~0x60)
{|}~                (ASCII码：0x7B~0x7E)

提示:
1 <= 字符串的长度<= 300
输入描述：

输入一个string的密码
输出描述：

输出密码等级
示例1
输入：

38$@NoNoN

输出：

VERY_SECURE

说明：

样例的密码长度大于等于8个字符，得25分；大小写字母都有所以得20分；有两个数字，所以得20分；包含大于1符号，所以得25分；由于该密码包含大小写字母、数字和符号，所以奖励部分得5分，经统计得该密码的密码强度为25+20+20+25+5=95分。


示例2
输入：

Jl)M:+

输出：

AVERAGE

说明：

示例2的密码强度为10+20+0+25+0=55分。        
'''


# tar_s = input()

# score = 0

# import re

# if len(tar_s) <= 4:
#     score += 5
# elif len(tar_s) <= 7:
#     score += 10
# else:
#     score += 25

# # 字母
# if re.findall(r"[a-zA-Z]", tar_s) == []:
#     score += 0
# elif re.match(r"^[a-z]+$", tar_s) or re.match(r"^[A-Z]+$"):
#     score += 10
# elif re.match(r"^[a-zA-Z]+$", tar_s):
#     score += 20

# # 数字
# if re.findall(r"[0-9]", tar_s) == []:
#     score += 0
# elif len(re.findall(r"^[0-9]+$", tar_s)) == 1:
#     score += 10
# else:
#     score += 20

# # 符号
# if re.findall(r"[\W]",tar_s) == []:
#     score += 0
# elif len(re.findall(r"[\W]")) == 1:
#     score += 10
# else:
#     score += 25

# # 奖励
# if re.search(r"[\d]",tar_s) and re.search(r"[a-z]",tar_s) and re.search(r"[\W]",tar_s) and re.search(r"[A-Z]",tar_s):
#     score += 5

# elif re.search(r"[\W]",tar_s) and re.search(r"[a-z]")


import re

def calculate_score(password):
    length_score = 0
    letter_score = 0
    digit_score = 0
    symbol_score = 0
    bonus_score = 0
    
    length = len(password)
    # 一、密码长度评分
    if length <= 4:
        length_score = 5
    elif 5 <= length <= 7:
        length_score = 10
    else:
        length_score = 25

    # 二、字母评分
    if re.search('[a-zA-Z]', password):
        if re.search('[a-z]', password) and re.search('[A-Z]', password):
            letter_score = 20
        else:
            letter_score = 10

    # 三、数字评分
    digits = re.findall('\d', password)
    if len(digits) == 1:
        digit_score = 10
    elif len(digits) > 1:
        digit_score = 20

    # 四、符号评分
    symbols = re.findall('[\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]', password)
    if len(symbols) == 1:
        symbol_score = 10
    elif len(symbols) > 1:
        symbol_score = 25

    # 五、奖励评分
    if letter_score and digit_score:
        bonus_score += 2
    if letter_score and digit_score and symbol_score:
        bonus_score += 1
    if letter_score == 20 and digit_score and symbol_score:
        bonus_score += 2

    # 总分
    total_score = length_score + letter_score + digit_score + symbol_score + bonus_score
    
    # 根据总分评定安全级别
    if total_score >= 90:
        return 'VERY_SECURE'
    elif total_score >= 80:
        return 'SECURE'
    elif total_score >= 70:
        return 'VERY_STRONG'
    elif total_score >= 60:
        return 'STRONG'
    elif total_score >= 50:
        return 'AVERAGE'
    elif total_score >= 25:
        return 'WEAK'
    else:
        return 'VERY_WEAK'

# 输入密码并评定安全级别
password = input()
print(calculate_score(password))

# 奖励
if letter_score and digit_score:
    bonus_score += 2
elif letter_score and digit_score and symbol_score:
    bonus_score += 1
elif letter_score == 20 and digit_score and symbol_score:
    bonus_score += 2