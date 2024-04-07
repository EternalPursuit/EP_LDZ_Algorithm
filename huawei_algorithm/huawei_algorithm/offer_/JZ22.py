'''

描述
输入一个长度为 n 的链表，设链表中的元素的值为 ai ，返回该链表中倒数第k个节点。
如果该链表长度小于k，请返回一个长度为 0 的链表。


数据范围：0≤n≤1050≤n≤105，0≤ai≤1090≤ai​≤109，0≤k≤1090≤k≤109
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
进阶：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n) 
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        # write code here
        fast_p = pHead
        slow_p = pHead
        for _ in range(k):
            if fast_p.next:
                fast_p = fast_p.next
            else:
                break
        else:
            while fast_p.next:
                fast_p = fast_p.next
                slow_p = slow_p.next
            return slow_p.val
        return ListNode(0)