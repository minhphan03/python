# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    #no need for recursion
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        current = ListNode(0)
        
        #don't return the head (the dummy result) because it does not point to the next
        #element in list. Use head.next instead
        result = current
        
        while (l1 or l2):
            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next
            
            current.next = ListNode(sum%10)
            
            #equivalence of ? : ternary expression 
            sum = 1 if sum > 9 else 0
            
            current = current.next
        
        # if sum after return is declared (sum>0)
        if sum>0:
            current.next = ListNode(sum)
        
        return result.next
