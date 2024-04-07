def power_(a,n):
    i = 0
    res = 1
    while n:
        if n%2:
            res = res*a
        a *= a
        n //= 2
        i += 1
        print(f"第i次：{i}")
    return res

base = 3
n = 64
res = power_(base,n)
print(res)