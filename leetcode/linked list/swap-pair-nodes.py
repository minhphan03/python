# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        cur = head
        start = cur.next
        
        pre = ListNode(0)
        
        
        while cur and cur.next:
            third = cur.next.next
            prev = cur
            cur = cur.next
            cur.next = prev
            prev.next = third
            pre.next = cur
            
            pre = prev
            cur = third
        
        return start
            
            
