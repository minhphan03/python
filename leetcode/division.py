class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isNeg = (dividend > 0) ^ (divisor > 0)
        q = 0
        
        de = abs(dividend)
        do = abs(divisor)
        while de >= do:
            #use bit shift operator based on the fact that leftshift multiplies the answer by 2
            #to minimize subtracting amap to prevent time limit exceed
            
            k = 0
            while de>= (do << k+1):
                k +=1
            
            #decrease divident and add to quotient
            de -= (do << k)
            q += (1 << k)
            
        MAX_INT = 1 << 31
        
        if q >= MAX_INT:
            if isNeg:
                return -MAX_INT
            else:
                return MAX_INT - 1
        elif isNeg:
            return -q
        else:
            return q
