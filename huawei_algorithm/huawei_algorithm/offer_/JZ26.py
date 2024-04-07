

'''
描述
输入两棵二叉树A，B，判断B是不是A的子结构。（我们约定空树不是任意一个树的子结构）

'''

class Solution:
    def HasSubtree(self , pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        # write code here
        if not pRoot1:
            return False

        if not pRoot2:
            return False


        if self.is_node(pRoot1 ,pRoot2):
            return True
        return self.HasSubtree(pRoot1.left ,pRoot2) or self.HasSubtree(pRoot1.right ,pRoot2)



    def is_node(self ,pRoot1 ,pRoot2):
        if not pRoot2:
            return False

        if not pRoot1:
            return False

        if pRoot1.val != pRoot2.val:
            return False

        return self.is_node(pRoot1.left ,pRoot2.left) and self.is_node(pRoot1.right ,pRoot2.right)
