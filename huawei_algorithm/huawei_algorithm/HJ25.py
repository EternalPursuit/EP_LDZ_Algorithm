# Tar_ = input()
#
# res = []
# tmp_least = []
#
# mapldz = dict()
# for val in Tar_:
#     mapldz[val] = mapldz.get(val,0) + 1
#
#
#
# sorted_items = list(mapldz.items())
#
# sorted_items.sort(key= lambda x:x[1])
#
# flag = sorted_items[0][1]
#
# need_char = []
# for item in sorted_items:
#     if item[1] > flag:
#         need_char.append(item[0])
#
#
# if need_char:
#     res = [key*value for key,value in mapldz.items() if value != flag]
# else:
#     res = [key*value for key,value in mapldz]
#
# print(''.join(res))

Tar_ = input()
mapldz = {}
for val in Tar_:
    mapldz[val] = mapldz.get(val,0) + 1

Minvalue = min(mapldz.values())

res = ''
for i  in Tar_:
    if mapldz[i] > Minvalue:
        res += i
if res:
    print(res)
else:
    print(Tar_)
