'''
描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

数据范围：两个数都满足 −10≤n≤1000−10≤n≤1000
进阶：空间复杂度 O(1)O(1)，时间复杂度 O(1)O(1)

'''


class Solution:
    def Add(self , num1: int, num2: int) -> int:
        # write code here
        add_flag = num2
        sum = num1
        while add_flag:
            temp = sum ^ add_flag
            add_flag = (sum & add_flag) << 1
            # 处理负数问题
            sum = temp & 0xFFFFFFFF
            return sum if sum >> 31 == 0 else sum -4294967296