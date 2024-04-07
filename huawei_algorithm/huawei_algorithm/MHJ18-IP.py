ipClass2num = {
    'A':0,
    'B':0,
    'C':0,
    'D':0,
    'E':0,
    'ERROR':0,
    'PRIVATE':0,
}

def check_ip(ip):
    # ip_bit = ip.split('.')
    if len(ip) != 4 or '' in ip:  #ip 的长度为4 且每一位不为空
        return False
    for i in ip:
        if int(i)<0 or int(i) >255:   #检查Ip每一个10位的值范围为0~255
            return False
    return True

def check_mask(mask):
    if len(mask)!=4:
        return False
    res = ''
    for val in mask:
        val = int(val)
        tmp = bin(val)[2:]
        res += (8-len(tmp))*'0'+str(tmp)
    if "01" in res or "1" not in res or "0" not in res:
        return False
    else:
        return True


def check_private_ip(ip):
    ip = [int(item) for item in ip]
    if (ip[0]==10) or (ip[0]==172 and 16 <= ip[1] <= 31) or (ip[0]==192 and 168 == ip[1]):
        return True
    return False

while True:
    try:
        s = input().split("~")
        ip = s[0].split(".")
        mask = s[1].split(".")
        if check_mask(mask) and check_ip(ip):
            if check_private_ip(ip):
                ipClass2num["PRIVATE"] += 1
            if   0   < int(ip[0]) <= 126:
                ipClass2num['A'] += 1
            elif 126 < int(ip[0]) <= 127 or int(ip[0]) == 0:
                pass
            elif 127 < int(ip[0]) <= 191:
                ipClass2num['B'] += 1
            elif 191 < int(ip[0]) <= 223:
                ipClass2num["C"] += 1
            elif 223 < int(ip[0]) <= 239:
                ipClass2num["D"] += 1
            elif 239 < int(ip[0]) <= 255:
                ipClass2num["E"] += 1

        else:
            print(f"{ip}~{mask}")
            ipClass2num["ERROR"] += 1

    except:
        break


for v in ipClass2num.values():
    print(v,end=" ")