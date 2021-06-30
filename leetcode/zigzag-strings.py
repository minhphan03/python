class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #attempt very easy approach by eliesikh
        
        if numRows == 1 or len(s) < numRows:
            return s
        
        #we start at first row
        pos = 1
        step = 1
        
        #lines is a dict
        lines = {}
        
        for char in s:
            if pos not in lines:
                lines[pos] = char
            else:
                lines[pos] +=char
            
            pos += step
            if pos == 1 or pos == numRows:
                #switch direction
                step *= -1
            
        sol = ""
        
        for i in range(1, numRows +1):
            sol += lines[i]
        
        return sol
