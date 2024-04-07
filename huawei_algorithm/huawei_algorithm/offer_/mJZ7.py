
class TreeNode(object):
    def __init__(self,x):
        self.x = x
        self.left = None
        self.right = None

class Solution:
   def reConstructBinaryTree(self, preOrder, vinOrder) -> TreeNode:
        # write code here
        n = len(preOrder)
        m = len(vinOrder)
        if n == 0 or m == 0:
            return None
        root = TreeNode(preOrder[0])
        for i in range(len(vinOrder)):
            if preOrder[0] == vinOrder[i]:
                leftpre = preOrder[1:i + 1]
                leftvin = vinOrder[i]
                root.left = self.reConstructBinaryTree(leftpre, leftvin)
                rightpre = preOrder[i + 1:]
                rightvin = vinOrder[i + 1:]
                root.right = self.reConstructBinaryTree(rightpre, rightvin)
                break
        return root
pre = [1,2,4,7,3,5,6,8]
vin = [4,7,2,1,5,3,8,6]
sol = Solution()
res = sol.reConstructBinaryTree(pre,vin)
print(res)