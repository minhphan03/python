class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        idx = 0
        while idx < len(strs[0]):
            char = strs[0][idx]
            for s in strs:
                if idx >= len(s) or s[idx] != char:
                    return strs[0][:idx]
            
            idx +=1
        
        return strs[0]
