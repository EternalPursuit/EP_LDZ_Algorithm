
while True:
    try:
        flag = 0
        num1 = input()
        num2 = input()
        m = len(num1)
        n = len(num2)
        res = []
        while n>0 and m>0:
            tmp = int(num1[m-1]) + int(num2[n-1]) + flag
            if tmp >= 10:
                flag = 1
            else:
                flag = 0
            res.append(tmp%10)
            n -= 1
            m -= 1
        while m>0:
            tmp = int(num1[m-1]) + flag
            if tmp >= 10:
                flag = 1
            else:
                flag = 0
            res.append(tmp%10)
            m -= 1
        while n>0:
            tmp = int(num2[n-1]) + flag
            if tmp >= 10:
                flag = 1
            else:
                flag = 0
            res.append(tmp%10)
            n -= 1
        if flag == 1:
            res.append(1)

        for val in res[::-1]:
            print(val,end='')
    except:
        break