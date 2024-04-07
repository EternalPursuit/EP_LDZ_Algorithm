'''
写出一个程序，
接受一个由字母、数字和空格组成的字符串，
和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母
'''

import  sys

res= []
for line in sys.stdin:
    res.append(line)

print(res)

input_string = res[0]
target_char = res[1]

input_string =  input_string.lower()
target_char = target_char.lower()

res = dict()
for val in input_string:
    res[val] = res.get(val,0) + 1

if target_char in res:
    print(res[target_char])
else:
    print("0")