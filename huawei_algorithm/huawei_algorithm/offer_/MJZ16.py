def Power(base: float, exponent: int) -> float:
    # write code here
    res = 1
    if exponent > 0:
        for _ in range(exponent):
            res *= base
        return res
    if exponent == 0:
        return 1.0

    if exponent < 0:
        for i in range(exponent, 0, -1):
            print(i)
            res /= base
        return res

res = Power(2,-3)