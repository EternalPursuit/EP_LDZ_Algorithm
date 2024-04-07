def daimeterOfBinaryTree(root):
    ans = 1
    def dfs(root):
        if not root: return 0
        L = dfs(root.left)
        R = dfs(root.right)
        ans = max(ans,L+R+1)
        return max(L,R) + 1
    dfs(root)
    return ans - 1