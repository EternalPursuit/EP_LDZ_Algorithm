'''
描述

给定一个字符串描述的算术表达式，计算出结果值。
输入字符串长度不超过 100 ，合法的字符包括 ”+, -, *, /, (, )” ， ”0-9” 。

数据范围：运算过程中和最终结果均满足 ∣val∣≤231−1 ∣val∣≤231−1  ，即只进行整型运算，确保输入的表达式合法
输入描述：

输入算术表达式
输出描述：

计算出结果值
示例1
输入：

400+5

输出：

405
'''
import re

def compute_mul_div(numbers, operators):
    # 处理所有乘法和除法
    i = 0
    while i < len(operators):
        if operators[i] == '*' or operators[i] == '/':
            if operators[i] == '*':
                numbers[i] = numbers[i] * numbers[i+1]
            else:
                numbers[i] = numbers[i] // numbers[i+1]
            del numbers[i+1]
            del operators[i]
        else:
            i += 1

def compute_add_sub(numbers, operators):
    # 处理所有加法和减法
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i+1]
        else:
            result -= numbers[i+1]
    return result

def calculate_expression(expression):
    # 移除空格
    expression = expression.replace(' ', '')
    # 使用正则表达式找到所有的数字和运算符
    numbers = list(map(int, re.findall(r'\d+', expression)))
    operators = re.findall(r'[+\-*/]', expression)
    print("numbers is :",numbers)
    print("operators is :",operators)
    
    # 首先处理乘法和除法
    compute_mul_div(numbers, operators)
    # 然后处理加法和减法
    result = compute_add_sub(numbers, operators)
    
    return result

# 示例
expression = "5+5/5*6-8"
print(calculate_expression(expression))
