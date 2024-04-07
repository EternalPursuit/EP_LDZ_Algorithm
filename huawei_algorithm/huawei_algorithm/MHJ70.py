

n = input()
mat = [list(map(int, input().split())) for _ in range(n)]

rule = input()

sum = 0
res = []
for val in rule:
    if val == "(":
        continue
    if val == ")":
        item1 = res.pop()
        item2 = res.pop()
        # 做计算
        sum += item2[0] * item2[1] * item1[1]
        res.append([item2[0], item1[1]])
    else:
        res.append(mat.pop(0))
print(sum)