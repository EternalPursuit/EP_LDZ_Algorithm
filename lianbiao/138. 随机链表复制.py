class Node:
    def __init__(self,val=0,next=None,random=None):
        self.val = val
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        myDict = {}
        cur = head
        while cur:
            myDict[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            myDict[cur].next = myDict.get(cur.next)
            myDict[cur].random = myDict.get(cur.random)
            cur = cur.next

        if not head:
            return head
        else:
            return myDict[head]

