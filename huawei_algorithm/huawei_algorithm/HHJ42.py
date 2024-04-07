num1 = ['zero','one','two','three','four','five','six',
       'seven','eight','nine','ten','eleven','twelve',
       'thirteen','fourteen','fifteen','sixteen',
       'seventeen','eighteen','nineteen']
num2 = [0,0,'twenty','thirty','forty','fifty','sixty',
       'seventy','eighty','ninety']

while True:
    s = input()[::-1]

    danwei_ind = 0
    danwei = ["","thousand","million","billion"]

    res = []
    for i in range(0,len(s),3):
        tmp = []
        target = int(s[i:i+3][::-1])
        if target >= 100:
            tmp.append(num1[target//100])
            tmp.append("hundred")
            if target % 100 != 0:
                tmp.append("and")
        target %= 100
        if target >= 20:
            tmp.append(num2[target//10])
            if target % 10 != 0:
                tmp.append(num1[target%10])
        elif target > 0:
            tmp.append(num1[target])

        print(tmp)
        tmp = " ".join(tmp) + ' '+danwei[danwei_ind]
        res.append(tmp)
        danwei_ind += 1

    print("res is : ",' '.join(res[::-1]))