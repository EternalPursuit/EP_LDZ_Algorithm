'''
描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回 true ,否则返回 false 。假设输入的数组的任意两个数字都互不相同。

数据范围： 节点数量 0≤n≤10000≤n≤1000 ，节点上的值满足 1≤val≤1051≤val≤105 ，保证节点上的值各不相同
'''


class Solution:
    def VerifySquenceOfBST(self, sequence: List[int]) -> bool:
        # write code here
        if not sequence:
            return False
        s, root = [] , 999999
        for i in range(len(sequence)-1,-1,-1):
            if sequence[i] > root:
                return False
            while s and sequence[i] < s[-1]:
                root = s.pop()
            s.append(sequence[i])
        return True  