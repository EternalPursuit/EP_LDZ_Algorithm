class ListNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
    

class Solution: 
    def reverseBetween(self, head, m):
        pass
    
    def reverseK(self,head,k):
        cur = head
        for _ in range(k):
            tmp = cur.next.next
            cur.next.next = cur
            
        
            
            
            
        