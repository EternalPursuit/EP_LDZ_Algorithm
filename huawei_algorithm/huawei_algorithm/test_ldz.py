
def check_ip(ip):
    if len(ip) != 4:
        return False
    for val in ip:
        if val<0 or val>255:
            return False
        else:
            continue
    return True 

def check_mask(mask):
    if not check_ip(mask):
        return False
    res = ''
    for val in mask:
        tmp = bin(val)[2:]
        res += (8-len(tmp))*'0'+str(tmp)
    if "01" in res:
        return False
    else:
        return True




while True:
    try:
        mask_addr =  list(map(int,input().split(".")))
        first_addr = list(map(int,input().split(".")))
        second_addr = list(map(int,input().split(".")))
        if check_ip(first_addr) and check_ip(second_addr) and check_mask(mask_addr):
            for i in range(4):
                # print(first_addr[i])
                # print(mask_addr[i])
                # print(second_addr[i])
                if not (first_addr[i]&mask_addr[i])^(second_addr[i]&mask_addr[i]):
                    continue
                else:
                    print("2")
                    break
            else:
                print("0")
        else:
            print("1")

    except:
        break