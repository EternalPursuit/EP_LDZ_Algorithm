
'''
描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。

数据范围： 1≤n≤108 1≤n≤108
输入描述：

输入一个int型整数
输出描述：

按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
示例1
输入：

9876673

输出：

37689
'''

'''
需要注意的是，必须用dict.fromkeys函数，这个会默认以list中的数字作为键，None为值。
这样由于键是唯一的，那么就自然去重了。
之后再用list转换为列表

需要注意的是格式的要求。
'''
target_list = [int(item) for item in input()][::-1]

tmp_dict = dict.fromkeys(target_list)
res_list = list(tmp_dict)
for val in res_list:
    print(val,end='')