'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表
'''


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree.left is None and pRootOfTree.right is None:
            return pRootOfTree

        pRootOfTree.left = self.Convert(pRootOfTree.left)
        pRootOfTree.right = self.Convert(pRootOfTree.right)
        return pRootOfTree.right