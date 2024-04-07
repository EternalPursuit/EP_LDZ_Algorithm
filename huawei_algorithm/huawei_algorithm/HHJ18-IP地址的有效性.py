

A = 0
B = 0
C = 0
D = 0
E = 0
I = 0
P = 0
def is_mask(s):
    return False

def is_private(s):
    return False

s = input()
tmp = s.split("~")
IP =tmp[0]
MASK = tmp[1]
ip_l = IP.split(".")
if len(ip_l)!= 4:
    I += 1
for i in range(1,4):
    if 0<=int(ip_l[i])<=255:
        continue
    else:
        I += 1
        break
first_add = int(ip_l[0])
if 1 <= first_add <= 126 and is_mask(MASK):
    A += 1
elif 128 <= first_add < 192 and is_mask(MASK):
    B += 1
elif 192 <= first_add < 224 and is_mask(MASK):
    C += 1
elif 224 <= first_add < 240 and is_mask(MASK):
    D += 1
elif 240 <= first_add < 256 and is_mask(MASK):
    E += 1
elif 127 <= first_add < 128 and is_mask(MASK):
    pass
elif 0 <= first_add < 1 and is_mask(MASK):
    pass
else:
    I += 1
if is_private(IP):
    P += 1


