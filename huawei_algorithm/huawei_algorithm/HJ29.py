
# '''
# 描述

# 对输入的字符串进行加解密，并输出。

# 加密方法为：

# 当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；

# 当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；

# 其他字符不做变化。
# 解密方法为加密的逆过程。
# 数据范围：输入的两个字符串长度满足 1≤n≤1000 1≤n≤1000  ，保证输入的字符串都是只由大小写字母或者数字组成
# 输入描述：

# 第一行输入一串要加密的密码
# 第二行输入一串加过密的密码
# 输出描述：

# 第一行输出加密后的字符
# 第二行输出解密后的字符
# '''

# import re
# def Add_password(s):
#     s = re.sub('[a-y]',lambda x:chr(ord(x.group().upper())+1),s)
#     s = re.sub("z","A",s)
#     s = re.sub('[A-Y]',lambda x:chr(ord(x.group().lower())+1),s)
#     s = re.sub("Z","a",s)
#     s = re.sub('[0-8]',lambda x : str(int(x.group())+1),s)
#     s = re.sub('9','0',s)
#     return s

# def detach_password(s):
#     s = re.sub('[b-z]',lambda x:chr(ord(x.group().upper())-1),s)
#     s = re.sub("a","Z",s)
#     s = re.sub('[B-Z]',lambda x:chr(ord(x.group().lower())-1),s)
#     s = re.sub("A","z",s)
#     s = re.sub('[1-9]',lambda x : str(int(x.group())-1),s)
#     s = re.sub('0','9',s)
#     return s

# while True:
#     try:
#         target_word = input()
#         detach_word = input()
#         a_s = Add_password(target_word)
#         print(a_s)
#         b_s = detach_password(detach_password)
#         print(b_s)
#     except:
#         break


# 您的代码用于加密和解密字符串，看起来已经很接近正确的解决方案了，但似乎在调用 detach_password 函数时出现了一个小错误：您应该将 detach_word 变量传递给 detach_password 函数，而不是函数名 detach_password 本身。这里是修改后的代码段：
#
# python
# Copy code
# import re
#
# def Add_password(s):
#     s = re.sub('[a-yA-Y]', lambda x: chr(ord(x.group().upper()) + 1) if x.group().islower() else chr(ord(x.group().lower()) + 1), s)
#     s = re.sub("zZ", lambda x: "A" if x.group() == "z" else "a", s)
#
#     s = re.sub('[0-8]', lambda x: str(int(x.group()) + 1), s)
#     s = re.sub('9', '0', s)
#     return s
#
# def detach_password(s):
#     s = re.sub('[b-z]', lambda x: chr(ord(x.group().upper()) - 1), s)
#     s = re.sub("a", "Z", s)
#     s = re.sub('[B-Z]', lambda x: chr(ord(x.group().lower()) - 1), s)
#     s = re.sub("A", "z", s)
#     s = re.sub('[1-9]', lambda x: str(int(x.group()) - 1), s)
#     s = re.sub('0', '9', s)
#     return s
#
# while True:
#     try:
#         target_word = input()
#         detach_word = input()
#         a_s = Add_password(target_word)
#         print(a_s)
#         b_s = detach_password(detach_word)  # 修正了这里
#         print(b_s)
#     except EOFError:  # 使用 EOFError 更合适，因为它是 input() 遇到文件结束标记时抛出的异常
#         break

# s = "abcdefg"
# def encrypt_(input,operation="enc"):
#     res = []
#     shift = 1 if operation=="enc" else -1
#     for char in input:
#         if char.isalpha():
#             offset = ord(char)-ord('A') if char.isupper() else ord(char)-ord('a')
#             base = ord('a') if char.isupper() else ord("A")
#             new_char = chr(base+(shift+offset)%26)
#             res.append(new_char)
#         elif char.isdigit():
#             new_char = str((int(char) + shift)%10)
#             res.append(new_char)
#         else:
#             res.append(char)
#
#     return "".join(res)
#
# enc = encrypt_(s,"enc")
# print(enc)
# dec = encrypt_(enc,"dec")
# print(dec)def encrypt_(input,operation="enc"):
#     res = []
#     shift = 1 if operation=="enc" else -1
#     for char in input:
#         if char.isalpha():
#             offset = ord(char)-ord('A') if char.isupper() else ord(char)-ord('a')
#             base = ord('a') if char.isupper() else ord("A")
#             new_char = chr(base+(shift+offset)%26)
#             res.append(new_char)
#         elif char.isdigit():
#             new_char = str((int(char) + shift)%10)
#             res.append(new_char)
#         else:
#             res.append(char)
#
#     return "".join(res)
#
# enc = encrypt_(s,"enc")
# print(enc)
# dec = encrypt_(enc,"dec")
# print(dec)
#
#
#
# def encrypt_decrypt(input_str, operation="encrypt"):
#     result = []
#     for char in input_str:
#         if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
#             # 对字母进行加密或解密
#             shift = 1 if operation == "encrypt" else -1
#             base = ord('A') if char.isupper() else ord('a')
#             offset = (ord(char.upper()) - base + shift) % 26
#             new_char = chr(base + offset).lower() if char.islower() else chr(base + offset).upper()
#             result.append(new_char)
#         elif '0' <= char <= '9':
#             # 对数字进行加密或解密
#             new_char = str((int(char) + (1 if operation == "encrypt" else -1)) % 10)
#             result.append(new_char)
#         else:
#             # 其他字符不变
#             result.append(char)
#     return ''.join(result)
#
# # 测试加密和解密
# encrypted = encrypt_decrypt("zZaA9", operation="encrypt")
# print("Encrypted:", encrypted)
# decrypted = encrypt_decrypt(encrypted, operation="decrypt")
# print("Decrypted:", decrypted)

def check(a,b):
    enc_= "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dec_= "BCDEFGHIJKLMNOPQRSTUVWXYZA1234567890bcdefghijklmnopqrstuvwxyza"
    res = ''
    if b == 1:
        for i in a:
            res += dec_[enc_.index(i)]
    elif b == -1:
        for i in a:
            res += enc_[dec_.index(i)]
    return res

while True:
    try:
        print(check(input(),1))
        print(check(input(),-1))
    except:
        break
s = "2OA92AptLq5G1lW8564qC4nKMjv8C"
print(check(s,1))