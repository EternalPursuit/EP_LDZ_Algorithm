'''
描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

数据范围：字符串长度满足 1≤n≤2500 1≤n≤2500
输入描述：

输入一个字符串（字符串的长度不超过2500）
输出描述：

返回有效密码串的最大长度
'''

# str_= input()
# n = len(str_)
#
# lis = []
#
# for i in range(n-1):
#     for j in range(1,n):
#         # if str_[j] == str_[i] and str_[i+1:j] == str_[j-1:i:-1]:
#         if str_[i:j+1] == str_[j:i-1:-1]:
#             lis.append(len(str_[i:j+1]))
#
# print(max(lis))


def manacher(s):
    t = "#".join('^{}$'.format(s))
    # t = "#".join(s)
    print("ori string is : ",t)
    n = len(t)

    P = [0]*n
    C = R = 0

    for i in range(1,n-1):
        P[i] = (R > i) and min(R - i, P[2*C - i])

        while t[i + P[i] + 1] == t[i - P[i] - 1]:
            P[i] += 1

        if i + P[i] > R:
            C, R = i , i + P[i]
    return max(P)

s = input()
print(manacher(s))


