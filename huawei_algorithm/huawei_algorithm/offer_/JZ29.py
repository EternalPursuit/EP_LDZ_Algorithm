'''
描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：

[[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]]

则依次打印出数字

[1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

数据范围:
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
'''


# -*- coding:utf-8 -*-
# class Solution:
#     # matrix类型为二维列表，需要返回列表
#     def printMatrix(self, matrix):
#         res = []#初始化返回列表
#         while matrix:
#             res += matrix.pop(0)#提取第一行
#             matrix = list(zip(*matrix))[::-1]#旋转90度
#         return res
#         # write code here
#
# a = 0
# if a is not None:
#     print(True)
# else:
#     print(False)


'''

描述
不分行从上往下打印出二叉树的每个节点，同层节点从左至右打印。例如输入{8,6,10,#,#,2,1}，如以下图中的示例二叉树，则依次打印8,6,10,2,1(空节点不打印，跳过)，请你将打印的结果存放到一个数组里面，返回。

数据范围:
0<=节点总数<=1000
-1000<=节点值<=1000
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PrintFromTopToBottom(self , root: TreeNode) -> List[int]:
        # write code here
        ori = [root]
        res = []
        while ori[0]:
            if root.val != "#":
                res.append(root.val)
            ori.append(root.left)
            ori.append(root.right)
            ori.pop(0)
        return res



描述
数字以 0123456789101112131415... 的格式作为一个字符序列，在这个序列中第 2 位（从下标 0 开始计算）是 2 ，第 10 位是 1 ，第 13 位是 1 ，以此类题，请你输出第 n 位对应的数字。

class Solution:
    def findNthDigit(self , n: int) -> int:
        # write code here
        # 长度是： n = 10*1 + 90*2 + 900*3 + 9000*4 +
        digit = 1
        start = 1
        sum = 10
        while n >= sum:
            n -= sum
            start *= 10
            digit += 1
            sum = 9*start*digit
        num = start + n//digit
        index = n%digit
        return int(str(num)[index])