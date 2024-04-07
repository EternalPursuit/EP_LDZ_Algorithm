
tar_ = input()

a = {key:tar_.count(key) for key in tar_}

b = [(key,val) for key,val in a.items()]

b.sort(key= lambda x: x[1]*10000-ord(x[0]),reverse=True)



"""
描述

自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n(包括n)以内的自守数的个数

数据范围： 1≤n≤10000 1≤n≤10000 



输入描述：

int型整数
输出描述：

n以内自守数的数量。
"""

tmp_list = [0,1,5,6]
N = int(input())

def is_zss(nums):
    if nums%10 in tmp_list:
        return True

res = 0
for i in range(1,N+1):
    if is_zss(i):
        res += 1
    else:
        continue
print(res)