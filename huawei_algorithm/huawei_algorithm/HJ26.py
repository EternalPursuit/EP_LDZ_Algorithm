while True:
    try:
        s = input()
        a = ''
        for i in s:
            if i.isalpha():
                a += i
        b = sorted(a, key=str.upper)
        index = 0
        d = ''
        for i in range(len(s)):
            if s[i].isalpha():
                d += b[index]
                index += 1
            else:
                d += s[i]
        print(d)
    except:
        break


'''
我的实现：

'''

ta = input()
need = ''
for val in ta:
    if val.isalpha():
        need += val

B = sorted(need,key=str.upper)

index = 0
res = ''
for i in ta:
    if i.isalpha():
        print(B[index],end='')
        index += 1
    else:
        print(i,end='')
