'''
这道题关键的地方在于 不能是等号
'''
def isValidTree(root,left=float("-inf"),right=float("inf")):
    if root is None: return True
    return left < root.val<right and isValidTree(root.left,left,root.val) and isValidTree(root.right,root.val,right)



