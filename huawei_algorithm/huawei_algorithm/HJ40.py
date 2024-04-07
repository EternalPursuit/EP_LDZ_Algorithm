# import sys

# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))


import re

ta = input()


char_l = re.findall(r"[a-zA-Z]",ta)
print(char_l)
print(len(char_l))
spa_l = re.findall(r"[\s]",ta)
print(spa_l)
print(len(spa_l))
digi = re.findall(r"[0-9]",ta)
print(digi)
print(len(digi))
print(len(ta)-len(char_l)-len(spa_l)-len(digi))