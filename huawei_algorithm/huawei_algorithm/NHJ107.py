while True:
    try:
        a = float(input().strip())
        epsilon = 0.00001
        low = min(-1.0,a)
        high = max(1.0,a)
        i = 0
        ans = (low+high)/2.0
        while abs(ans**3-a) > epsilon:
            i+=1
            print(f"这是第{i}次")
            if ans**3 < a:
                low = ans
            else:
                high = ans
            ans = (low+high)/2.0
        print(f"{ans:.1f}")


    except:
        break