'''
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
'''

target_string = input("请输入字符串：")

length = 0
# for val in target_string[::-1]:
#     if val != ' ':
#         length += 1
#     else:
#         break
# print(length)

for val in target_string[::-1]:
    if val == " ":
        break
    length += 1
print(length)