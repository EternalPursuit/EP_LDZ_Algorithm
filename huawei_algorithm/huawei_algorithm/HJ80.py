

args=['3','11 2 5','4','-1 0 3 2']

N1 = int(args[0])
N2 = int(args[2])

N1_list = args[1].split()
N2_list = args[3].split()
N1_list.extend(N2_list)
tmp_d =dict.fromkeys(N1_list)
N1_list = list(tmp_d)
print(N1_list)
N1_list.sort(key=int)
print("".join(N1_list))
