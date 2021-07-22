# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        no = 1
        while cur.next != None:
            no +=1
            cur = cur.next
        
        if n == no:
            return head.next
        steps = no - n -1
        
        prev = head
        while steps !=0:
            prev=prev.next
            steps -=1
        
        prev.next = prev.next.next
        
        return head
        
