basketsball_index = input().split(",")
target_valid_index = input().split(",")

stack = []
res = ""
i = 0
while i < len(target_valid_index):
    val = target_valid_index[i]
    if (not stack) or (stack[0] != val and stack[-1]!=val):
        if basketsball_index:
            stack.append(basketsball_index.pop(0))
        else:
            print("NO")
            break

    if len(stack) > 1:
        if stack[-1] == val:
            res += "R"
            i += 1
            stack.pop()
        elif stack[0] == val:
            res += "L"
            i += 1
            stack.pop(0)

    if len(stack)==1 and stack[-1] == val:
        res += "L"
        i += 1
        stack.pop(0)
print(res)