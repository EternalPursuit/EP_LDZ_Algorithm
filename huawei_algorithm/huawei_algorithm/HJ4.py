'''
描述

•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

'''

'''
这道题我错在以下几点：
1. if , else 这个没有写完整，导致if里面执行了一遍之后，因为没有else，
所以又执行了一遍打印。 以至于出错
2. 在if判断中，对于最后的索引没有处理好。 必须是相对索引，或者绝度索引。
'''
TargetString = input()


length_string = len(TargetString)

if length_string == 0:
    print(TargetString)

index_now = 0
while index_now < length_string:
    if length_string -  index_now < 8:
        print(TargetString[index_now:] + '0'*(8-length_string + index_now))
    else:
        print(TargetString[index_now:index_now+8])

    index_now += 8