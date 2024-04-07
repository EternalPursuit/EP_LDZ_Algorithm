n =1000

def is_wanqunshu(num):
    if num == 1:
        return False
    res = [1]
    i = 2
    while i*i <= num:
        if num % i == 0:
            res.append(i)
            res.append(num//i)
        i += 1
    total = sum(res)
    if total == num:
        return True
    else:
        return False
res = 0
for i in range(1,n+1):
    if is_wanqunshu(i):
        res += 1

print(res)
