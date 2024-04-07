n = int(input())
s = input()

window = [1,2,3,4]
ind = 0

for val in s:
    if val == "U" and ind == 0 and window[ind]==1:
        window = [n-3,n-2,n-1,n]
        ind = 3
        continue
    elif val == "D" and ind == 3 and  window[ind]==n:
        window = [1,2,3,4]
        ind = 0
        continue
    elif val == "U" and ind == 0:
        window = [item-1 for item in window]
        continue
    elif val == "D" and ind == 3:
        window = [item+1 for item in window]
        continue

    elif val == "U" and ind !=0:
        ind -= 1
        continue
    elif val == "D" and ind != 3:
        ind += 1
        continue


for val in window:
    print(val,end=" ")
print()
print(window[ind])