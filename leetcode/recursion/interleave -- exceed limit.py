#brute force
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #use recursion
        #for every recursion, we find combinations with the next thingy, and make combinations until find we run out of combinations. Check every combinations (brute-force)
        if (len(s1)+len(s2)!=len(s3)):
            return False
        return self.is_Interleave(s1,0,s2,0,"",s3)
    
    def is_Interleave(self, s1: str, n1: int, s2:str, n2:int, res:str, s3:str) ->bool:
        if (res == s3 and n1==len(s1) and n2==len(s2)):
            return True
        ans = False
        if (n1<len(s1)):
            # |= is bit-wise operator for OR
            ans |= self.is_Interleave(s1,n1+1,s2,n2,res+s1[n1],s3)
        if (n2<len(s2)):
            ans |= self.is_Interleave(s1,n1,s2,n2+1,res+s2[n2],s3)
        return ans
