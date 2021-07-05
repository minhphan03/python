class Solution:
    def isPalindrome(self, x: int) -> bool:
        #not transferring to a string
        
        if x < 0 or (x % 10 == 0 and x !=0):
            return False
        
        revertedNumber = 0
        #find half the number
        
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = int(x/10)
        
        return x == revertedNumber or x == int(revertedNumber/10)
