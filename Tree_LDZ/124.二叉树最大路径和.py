class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.max_sum = float("-inf")
    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node: return 0
            leftGain = max(maxGain(node.left),0)
            rightGain = max(maxGain(node.right),0)
            priceNewPath = node.val + leftGain + rightGain
            self.max_sum = max(self.max_sum,priceNewPath)
            return node.val + max(leftGain,rightGain)
        maxGain(root)
        return self.max_sum
