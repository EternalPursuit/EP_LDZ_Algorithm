class Solution(object):
    def LowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.LowestCommonAncestor(root.left,p,q)
        right = self.LowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return  root

print(-float("inf"))