class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #recursion solution by dannyluozp
        
        res = []
        
        #depth-first search
        def dfs(total, count_left, count_right, comb):
            #make sure that close parathesis does not come first
            if total < 0 or count_left < 0 or count_right < 0:
                return
            #if count_left = count_right = 0, sum automatically = 0
            if count_left == 0 and count_right == 0:
                res.append(comb)
            
            dfs(total+1, count_left-1, count_right, comb+'(')
            dfs(total-1, count_left, count_right-1, comb+')')
        
        dfs(0, n, n , '')
        
        return res
