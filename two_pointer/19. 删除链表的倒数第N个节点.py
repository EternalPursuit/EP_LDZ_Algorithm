class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
'''
对于链表的题来说，最重要的就是哨兵节点的初始化，这是非常重要的
因为它能够极大地改善递归的完整性，正如DP中的初始值一样。
'''
def removeNthNode(head,n):
    dummy = ListNode(0,head)
    pre = head
    second = dummy
    for i in range(n):
        pre = pre.next

    while pre:
        pre = pre.next
        second = second.next

    second.next = second.next.next
    return dummy.next

