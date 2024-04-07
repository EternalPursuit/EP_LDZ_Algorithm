# 处理输入
Array_N = int(input())
input_list = [0]*500

res_list = []
for _ in range(Array_N):
    input_char = int(input())
    input_list[input_char] = 1

for index, val in enumerate(input_list):
    if val == 1:
        print(index)