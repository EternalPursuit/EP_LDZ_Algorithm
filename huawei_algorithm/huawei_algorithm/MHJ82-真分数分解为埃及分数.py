'''
描述
分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。
注：真分数指分子小于分母的分数，分子和分母有可能gcd不为1！
如有多个解，请输出任意一个。



输入描述：

输入一个真分数，String型
输出描述：

输出分解后的string
'''

ori = input()
def func(ori):
    s = ori.split("/")
    a = int(s[0])
    b = int(s[1])
    if a==1:
        return ori
    if b%a==0:
        return "1/"+str(b//a)

    res = [ ]
    while abs(a)!=1:
        p = b//a
        r = b%a
        ans = "1/"+str(p+1)
        res.append(ans)
        b = b*(p+1)
        a = a-r
        if abs(a)!=1 and b%a == 0:
            res.append("1/"+str(b//a))
            return "+".join(res)
        elif abs(a) == 1:
            res.append("1/"+str(b))
            return '+'.join(res)
print(func(ori))