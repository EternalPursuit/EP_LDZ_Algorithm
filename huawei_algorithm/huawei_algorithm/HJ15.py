'''

描述
输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。

数据范围：保证在 32 位整型数字范围内
输入描述：

 输入一个整数（int类型）
输出描述：

 这个数转换成2进制后，输出1的个数
'''


res = 0

a = int(input())

while a//2 > 1:
    if a%2:
        res += 1
    a //= 2

if a == 1:
    res += 1

print(res)


'''
这段代码试图计算一个整数转换为二进制后包含的1的个数。虽然逻辑上基本正确，但是有几个问题需要修正以确保它能够正确地对所有的输入值进行处理：

循环条件：代码中的 while 循环条件设置为 a//2 > 1，这意味着当 a 降到 2 或 3 时，循环就会停止。这导致如果最后 a 变为 2（二进制为 10）或 3（二进制为 11），这时候的 1 的个数将不会被正确统计。循环应该继续直到 a 为 0。

最后一位的处理：原代码在循环结束后，通过检查 a == 1 来决定是否增加 res 的值。这种处理方法忽略了 a 最后为 2 的情况，因为 2 转为二进制也包含一个 1。

更优的实现：可以更简洁地实现相同的功能，例如使用 Python 的内置函数 bin() 来转换整数为二进制字符串，然后数字符串中 1 的个数。

修正后的代码：
python
Copy code
res = 0
a = int(input())

# 修改循环条件，确保能够正确处理所有数字
while a:
    if a % 2:
        res += 1
    a //= 2

print(res)
或者使用 Python 的内置方法：

python
Copy code
a = int(input())
# 使用 bin() 函数转换为二进制字符串，然后计算 '1' 的个数
res = bin(a).count('1')
print(res)
这两种方法都能正确处理所有的32位整型数，并且能够准确计算出二进制表示中 1 的个
'''