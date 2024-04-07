class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self) -> None:
        self.s = ""
        self.index = 0

    def Serialize(self, root):
        if root is None:
            return ''
        s = ''
        queue_root = [root]
        while queue_root:
            tmp_root = queue_root.pop(0)
            if tmp_root:
                s += str(tmp_root.val) + ","
                queue_root.append(tmp_root.left)
                queue_root.append(tmp_root.right)
            else:
                s += "#,"
        return s

    def Deserialize(self, s):
        if s == '':
            return None
        s_val = s.split(",")
        ind = 0
        root = TreeNode(int(s_val[ind]))
        queue_nodes = [root]
        while queue_nodes:

            root_node = queue_nodes.pop(0)

            ind += 1
            if s[ind]:
                tmp_node = TreeNode(int(s[ind]))
                root_node.left = tmp_node
                queue_nodes.append(tmp_node)
            ind += 1
            if s[ind]:
                tmp_node = TreeNode(int(s[ind]))
                root_node.right = tmp_node
                queue_nodes.append(tmp_node)
        return root