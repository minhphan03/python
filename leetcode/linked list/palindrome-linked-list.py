# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        #solution by anitej123
        #slow to reach the middle, fast to reach the end
        slow = fast = head
        
        #put fast before fast.next
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        #reverse the second half
        cur = slow
        prev = None
        
        #read reversed-linked-list.py for more info
        while cur:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third 
            
        #since third = cur.next and cur = third = cur.next is null
        #the node at the start that has value is prev
        
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True
