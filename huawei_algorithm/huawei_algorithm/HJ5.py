'''
 写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在 1≤n≤231−1 1≤n≤231−1
输入描述：

输入一个十六进制的数值字符串。
输出描述：

输出该数值的十进制字符串。不同组的测试用例用\n隔开。
'''

'''
这道题我错的地方：
1. 变换表不完整：需要把所有的数字都加上去，居然忽略了0，最好也是把大写字母一起加上去。
2. 16进制，但是习惯的写成了2进制
'''

Target_num_string = input()
transformer = {"1":1,"2":2,"3":3,"4":4,
                "5":5,"6":6,"7":7,"8":8,
                "9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,
                "A":10,"B":11,"C":12,"D":13,"E":14,"F":15,
                }

if not (Target_num_string.startswith("0x") or Target_num_string.startswith("0X")):
    print("")
else:
    tmp_string = Target_num_string[::-1]
    i = 1
    sum_res = 0
    for char_num in tmp_string[:-2]:
        print(f"char_num is {char_num}")
        if char_num in transformer:
            sum_res += transformer[char_num] * i
        else:
            break
        i *= 16

    print(sum_res)