# fail because of undealt return (result) constraints: what to return when x^n is out of the constraints? LeetCode did not specify

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        # use recursion
        if n == 1:
            return x
        if x == 1:
            return 1
        elif n < 0:
            return 1/(self.myPow(x,abs(n)-1)*x)
        else:
            return self.myPow(x, n-1) * x
