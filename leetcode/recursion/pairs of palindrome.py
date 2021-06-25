class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        l = []
        for i in range(0,len(words)-1):
            for j in range(i+1,len(words),1):
                if self.checkPalindrome(words[i]+words[j]):
                    l.append([i,j])
                if self.checkPalindrome(words[j]+words[i]):
                    l.append([j,i])
        
        return l
    
    def checkPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        if (s[0] != s[len(s)-1]):
            return False
        
        return self.checkPalindrome(s[1:len(s)-1])
