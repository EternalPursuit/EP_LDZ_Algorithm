while True:
    try:
        y, m, d = map(int, input().split())
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y%4 == 0 and y%100 != 0) or y%400 == 0:
            month[1] = 29
        print(sum(month[:m-1])+d)
    except:
        break