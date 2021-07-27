class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"}": "{", "]": "[", ")": "("}
        
        for c in s:
            if c in d.values():
                stack.append(c)
            
            if c in d.keys():
                if len(stack) == 0 or stack.pop() != d[c]:
                    return False
        
        if len(stack) != 0:
            return False
        return True
            
