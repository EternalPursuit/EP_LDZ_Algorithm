import re

target = input()

pattern = re.compile(r'[^a-zA-Z]')

res_ = pattern.split(target)

res_.reverse()
for val in res_:
    if val:
        print(val,end=" ")