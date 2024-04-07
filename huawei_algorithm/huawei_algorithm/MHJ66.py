

key=["reset","reset board","board add","board delete","reboot backplane","backplane abort"]
value=["reset what","board fault","where to add","no board at all","impossible","install first"]
s = input().strip().split()


if len(s) < 0 or len(s) >2:
    print("unknown command")
elif len(s) == 1:
    # if s[0]==key[0][:len(s[0])]:
    if key[0].startswith(s[0]):
        print(value[0])
    else:
        print("unknown command")
else:
    res = []
    for i in range(len(key)):
        command = key[i].split()
        if len(command) == 2 and command[0].startswith(s[0]) and command[1].startswith(s[1]):
            res.append(value[i])
        else:
            continue
    if len(res) == 1:
        print(res[0])
    else:
        print("unknown command")