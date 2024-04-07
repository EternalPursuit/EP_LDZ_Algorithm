'''
描述
给定一个单链表的头结点pHead(该头节点是有值的，比如在下图，它的val是1)，长度为n，反转该链表后，返回新链表的表头。

数据范围： 0≤n≤10000≤n≤1000
要求：空间复杂度 O(1)O(1) ，时间复杂度 O(n)O(n) 。

如当输入链表{1,2,3}时，
经反转后，原链表变为{3,2,1}，所以对应的输出为{3,2,1}。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        # write code here
        cur = head
        pre = None

        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre