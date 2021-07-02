#if out of 32 bit integer, return 0
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        
        isNeg = False
        if x < 0:
            isNeg = True
            x = x*(-1)
        

        while x > 0:
            res = res*10 + x%10
            x = int(x/10)
        
        if res > (2**31-1):
            return 0
        if isNeg:
            return res*(-1)
        else:
            return res
