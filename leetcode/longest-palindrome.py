class Solution:
    def longestPalindrome(self, s: str) -> str:
        #algorithm by Nick White on YouTube
        #check from middle and expand based from the hints
        
        #the first and last index of the longest substring
        start,end= 0,0
        
        #two cases: mid has no pair (racecar) and a pair (aabbaa)
        #for loop based to checkMiddle (middle index at every index)
        for i in range(len(s)):
            int1 = self.checkMiddle(s, i, i)
            int2 = self.checkMiddle(s, i, i + 1)
            length = max(int1, int2)
            if length > end - start:
                if length == int1:
                    start = i - int(length / 2)
                    end = i + int(length / 2)
                else:
                    start = i - int(length / 2) + 1
                    end = i + int(length / 2)
        
        return s[int(start):int(end+1)]
            
        
    def checkMiddle(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right +=1

        
        #return the length of the longest palindrome (prev case)
        return right - left -1
