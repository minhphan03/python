## Demonstration of the Reversed Linked List Algorithm

We use interative method to traverse through the linked list, marking down the first index to begin the reversion, and decrement the right index until it reaches 0 to mark the end of the the reversion

We use a local variable to swap pointers in this algorithm
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None
        
        cur = head
        prev = None
        
        #left and right are "indices" in the linked list
        #move to the beginning of the reverse part
        while left > 1:
            prev = cur
            cur = cur.next
            left = left-1
            right = right-1
        
        #name the role of the pointers
        
        #tail is the next pointer (the beginning of the part that is altered)
        #con is the previous index of the reversed part (unchanged) that is needed to connect later
        tail = cur
        con = prev
  ```
  ![algorithm demonstration 1](https://leetcode.com/problems/reverse-linked-list-ii/Figures/92/iterative-4.png)
  ```python
        #reverse the node by the algorithm
        
        while right>0:
            
            #the third pointer points to the next position of the tail pointer
            
            #third is a local variable in the while loop
            
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            right -=1
 ```
 
![algorithm demonstration 2](https://leetcode.com/problems/reverse-linked-list-ii/Figures/92/iterative-5.png)
 ```python
        #when the rightmost index is done reversed,
        
        #the prev node is at the end of the reversed part
        #the cur node is at the next unchanged part 
        
        #connect the reversed part to the original linked list
        
        # if con is not null
        if con:
            con.next = prev
        else:
            head = prev
        
        
        #in the first while loop, we can still see that the the tail.next (cur.next) points to prev (which is the con node). 
        
        #Break this connection and pull the tail.next to the end of the linked list
        tail.next = cur
        
        return head
            
 ```

