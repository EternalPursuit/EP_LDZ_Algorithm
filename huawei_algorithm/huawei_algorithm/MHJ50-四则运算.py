# last_res = cal_no_kuo("-4/2+7")
# print(last_res)
# def cal_no_kuo(s):
#     import re
#     s = re.split(r"([+\-\*/])",s)
#     temp = []
#     # for i in range(len(s)):
#     i =0
#     while i < len(s):
#         if s[i] == '#':
#             tar_l = s[i+1]+s[i+2]
#             temp.append(tar_l)
#             i = i + 2
#         else:
#             temp.append(s[i])
#         i += 1
#     s = [item if item != '' else "0" for item in temp]
#
#
#     tmp_l = []
#     i = 0
#
#     while i < len(s):
#         if s[i] =="*":
#             mul_res = float(tmp_l.pop()) * float(s[i+1])
#             tmp_l.append(str(mul_res))
#             i += 1
#         elif s[i] == "/":
#             div_res = float(tmp_l.pop()) / float(s[i+1])
#             tmp_l.append(str(div_res))
#             i += 1
#         else:
#             tmp_l.append(s[i])
#         i += 1
#
#
#     res = float(tmp_l[0])
#     i = 0
#     while i < len(tmp_l):
#         if tmp_l[i] in "+-":
#             res = res + float(tmp_l[i+1]) if tmp_l[i] == "+" else res - float(tmp_l[i+1])
#             i = i + 2
#         else:
#             i += 1
#     return res

def cal_no_kuo(s_l):
    i = 0
    tmp_l = []
    while i < len(s_l):
        if (s_l[i]  == "-" and i==0) or (s_l[i] =="-" and not s_l[i-1].isdigit()):
            tmp_l.append(s_l[i] + s_l[i+1])
            i += 1
        if s_l[i] in "*/":
            mulDiv = float(tmp_l.pop()) * float(s_l[i+1]) if s_l[i] =="*" else float(tmp_l.pop()) / float(s_l[i+1])
            tmp_l.append(mulDiv)
            i += 1
        else:
            tmp_l.append(s_l[i])
        i += 1
    # 处理加法：
    res = float(tmp_l[0])
    i = 1
    while i < len(tmp_l):
        if tmp_l[i] in "+-":
            res = res + float(tmp_l[i+1]) if tmp_l[i] == "+" else res - float(tmp_l[i+1])
            i += 2
        else:
            i += 1
    return res

s = "-8+5-5*8/-4+5-3+4"
res = cal_no_kuo(s)
print(res)


#
#
# import re
# s = "3+2*{1+2*[-4/(8-6)+7]}"
# tmp_l = []
# left_m = ["(","[","{"]
# right_m = [")","]","}"]
#
# # map_m = {key:val for key,val in zip(right_m,left_m)}
# map_m = dict(zip(right_m,left_m))
# temp = re.split(r"([+\-\/*(){}[\]])",s)
# s = [item for item in temp if item]
#
#
# for chr in s:
#     if chr not in right_m:
#         tmp_l.append(chr)
#     else:
#         cal_char = tmp_l.pop()
#         cal_string = [cal_char]
#         while cal_char != map_m[chr]:
#             cal_char = tmp_l.pop()
#             if cal_char not in left_m:
#                 cal_string.insert(0,cal_char)
#         res_tmp_m = cal_no_kuo(cal_string)
#         res_tmp_m = "#" + str(res_tmp_m) if res_tmp_m < 0 else str(res_tmp_m)
#         tmp_l.append(res_tmp_m)



# if len(tmp_l)==1:
#     print(int(float(tmp_l[0])))
# else:
#     last_res = cal_no_kuo(''.join(tmp_l))
#     print(int(last_res))